import mariadb

class Databases(object,db_name):
	def __inti__(self):
		self.x = [0.0]
		self.y = [0.0]
		self.z = [0.0]
	def __del__(self):
		
	def connect(self):
		try:
			conn = mariadb.connect(
				user="admin",
				password="Admin1",
				host="192.0.2.1",
				port=3306,
				database=db_name
				conn.autocommit = False
			)
			cur = conn.cursor()
			
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB Platform: {e}")
			sys.exit(1)
		
		def write_points(self, arg_prefix, x, y, z):
			try:
				self.arg1_name = arg_prefix + "x"
				self.arg2_name = arg_prefix + "y"
				self.arg3_name = arg_prefix + "z"
				self.x.append(x)
				self.y.append(y)
				self.z.append(z)
				cur.execute("INSERT INTO point_cloud (?,?,?) VALUES (?, ?, ?)", (arg1_name,arg2_name,arg3_name,x,y,z)) 
				conn.commit()
				
			except mariadb.Error as e: 
				print(f"Error: {e}")
				
		def read_points(self, arg_prefix):
			
				
