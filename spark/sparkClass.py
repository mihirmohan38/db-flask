import math
from pyspark import SparkContext
#from pyspark.sql import SparkSession
from os import system

class rdd_model : 
  def __init__(self) : 
    self.data = None 
    self.metadata = None
    self.joined = None
    self.avg = None 
    self.sc = SparkContext.getOrCreate() 

  def load_data(self, metadata, data) : 
    #change to 2 for metadata
    if metadata!=None : 
        #self.metadata = self.sc.textFile(metadata).map(lambda line: (line.split(',')[0], float(line.split(',')[1])) if line.split(',')[1]!= "price" else (0,0))
        final_rdd = self.sc.textFile(metadata)
        self.metadata = final_rdd.map(lambda a : (a.split("=")[3].split(",")[0][2:-1],a.split("=")[7].split(",")[0]))
    # adding data 
    if data!=None : 
        data_rdd = self.sc.textFile(data)
        self.data = data_rdd.map(lambda x : (x.split("=")[1][:-1], x.split("=")[2][:-1], x.split("=")[3]) if len(x.split("="))>=4 else (0,0,""))
        #self.data = data_rdd.map(lambda x : (x.split("=")[1][:-1], x.split("=")[2][:-1], x.split("=")[3]))
        self.avg = self.data.map(lambda x: (x[0],(len(x[2]),1))).reduceByKey(lambda x,y: (x[0] + y[0],x[1]+y[1])).map(lambda x : (x[0], x[1][0]/x[1][1]))

    
  def get_pearson(self) : 
    if self.avg==None or self.metadata==None : 
        return 
    joined_rdd = self.avg.join(self.metadata).map(lambda x : (float(x[1][0]), float(x[1][1])) if x[1][1].replace(".","").isdecimal() else (0,0))
    count = joined_rdd.count()
    avg_NA = joined_rdd.map(lambda x: (0,x[0])).reduceByKey(lambda x,y: x + y).collect()[0][1]/count
    avg_EU = joined_rdd.map(lambda x: (1,x[1])).reduceByKey(lambda x,y: x + y).collect()[0][1]/count
    NA_dev = joined_rdd.map(lambda x: (0,(x[0]-avg_NA)**2)).reduceByKey(lambda x,y: x + y).collect()[0][1]
    EU_dev = joined_rdd.map(lambda x: (1,(x[1]-avg_EU)**2)).reduceByKey(lambda x,y: x + y).collect()[0][1]
    NA_EU_dev = joined_rdd.map(lambda x: (2,(x[0]-avg_NA)*(x[1]-avg_EU))).reduceByKey(lambda x,y: x + y).collect()[0][1]
    corr = NA_EU_dev/(NA_dev*EU_dev)**0.5
    system("echo {} > /home/hadoop/corr.txt".format(corr))
    return corr

  def get_tfidf(self):
    if self.data==None  :
        return
    data = self.data
    lines = data.map(lambda x : (x[0],x[2]))
    #lines = data.select("asin", "reviewText")
    map1 = lines.flatMap(lambda x: [((x[0],i),1) for i in x[1].split()])
    reduce = map1.reduceByKey(lambda x,y:x+y)
    tf = reduce.map(lambda x: (x[0][1],(x[0][0],x[1])))

    map3 = reduce.map(lambda x: (x[0][1],(x[0][0],x[1],1)))
    #map3.collect()

    map4 = map3.map(lambda x:(x[0],x[1][2]))
    #map4.collect()

    reduce2 = map4.reduceByKey(lambda x,y:x+y)
    #reduce2.collect()

    num_rows = data.count()
    idf = reduce2.map(lambda x: (x[0], math.log10(num_rows/x[1])))
    #idf.collect()

    rdd=tf.join(idf)
    rdd=rdd.map(lambda x: (x[1][0][0],(x[0],x[1][0][1],x[1][1],x[1][0][1]*x[1][1]))).sortByKey()
    #rdd.collect()
    
    rdd=rdd.map(lambda x: (x[0],x[1][0],x[1][1],x[1][2],x[1][3]))
    rdd.saveAsTextFile("hdfs://localhost:9000/user/hadoop/output/")
    #df = rdd.toDF(["DocumentId", "Token", "TF", "IDF", "TF-IDF"])


  def write_joined(self) : 
    joined_rdd = self.data.join(self.metadata).map(lambda x : (x[1][0], x[1][1]))
    #joined_rdd.saveAsTextFile("hdfs://localhost:9000/output/")
    joined_rdd.saveAsTextFile("test")


model = rdd_model()
model.load_data("hdfs://localhost:9000/user/hadoop/meta/", "hdfs://localhost:9000/user/hadoop/count/")
model.get_pearson()
#model.get_tfidf()