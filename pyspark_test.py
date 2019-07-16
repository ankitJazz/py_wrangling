spark = SparkSession.builder.master("local").appName("spark").getOrCreate()
df = spark.read.json("people.json")
df.show()
