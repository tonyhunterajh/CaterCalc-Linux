

import sqlite3
from prettytable import PrettyTable


class SideItem:
	
	def __init__(self, event_id):
		
		# ----------------------------------------
		# Initialize Attributes and Variables.
		# ----------------------------------------
		
		# Attributes of the class.
		self.items_DICT = {}
		
		self.item_id = ""
		self.item_name = ""
		
		self.price_per_pack = ""
		self.servings_per_pack = ""
		self.servings_per_person = ""
		self.packs_needed = ""
		self.raw_cost = ""
		
	# ----------------------------------------
	# Get all items.
	# ----------------------------------------
	def get_all_items(self):	
		
		try:
		
			# Clear the items dictionary.
			self.items_DICT.clear()
			
			# Create a database connection.
			dbConn = sqlite3.connect("dbCaterCalc.db")
			dbCurs = dbConn.cursor()
			
			# SELECT all per piece items from the database.
			strSQL = "SELECT * FROM SideItems;"
			dbCurs.execute(strSQL)
			
			# Populate the dictionary from the database.
			for dbRec in dbCurs:
				
				# Initialize the dictionaries.
				self.item_id_DICT = {} 
				self.item_DICT = {}
				
				# Add an item dictionary to a dictionary for the item id.
				self.item_id_DICT[dbRec[0]] = self.item_DICT
				
				# Populate the item dictionary from the database.
				self.item_DICT["item_name"] = dbRec[1]
				self.item_DICT["price_per_pack"] = dbRec[2]
				self.item_DICT["servings_per_pack"] = dbRec[3]
				self.item_DICT["servings_per_person"] = dbRec[4]
				self.item_DICT["packs_needed"] = dbRec[5]
				self.item_DICT["raw_cost"] = dbRec[6]
			
				# Add the item dictionary to the main items dictionary.		
				self.items_DICT = self.item_id_DICT
			
			# Close the database connection.
			dbConn.close()
	
		except Exception as dbError:
			print(dbError)	
			
	# ----------------------------------------
	# Add an item.
	# ----------------------------------------
	def add_item(self):
		
		try:
		
			# Create a database connection.
			dbConn = sqlite3.connect("dbCaterCalc.db")
			dbCurs = dbConn.cursor()
			
			# INSERT a new item into the database.
			strSQL = "INSERT INTO SideItems (ItemName, PricePerPack, ServingsPerPack, ServingsPerPerson, PacksNeeded, RawCost, EventID) VALUES (" + self.item_name + "," + self.price_per_pack + "," + self.servings_per_pack + "," + self.servings_per_person + "," + self.packs_needed + "," + self.raw_cost + "," + event_id + ");"
			
			dbCurs.execute(strSQL)
			
			# Get the last row id as the item id.
			self.item_id = dbCurs.lastrowid()
			
			dbConn.commit()
			
			# Now we call get_all_items to populate the items object with the new item.
			self.get_all_items()
			
			# Close the database connection.
			dbConn.close()
	
		except Exception as dbError:
			print(dbError)
	
	# ----------------------------------------
	# Update an item.
	# ----------------------------------------
	def update_item(self):
		
		try:
		
			# Create a database connection.
			dbConn = sqlite3.connect("dbCaterCalc.db")
			dbCurs = dbConn.cursor()
			
			# UPDATE an item in the database.
			strSQL = "UPDATE SideItems SET ItemName = " + self.item_name + ", PricePerPack = " + self.price_per_pack + ", ServingsPerPack = " + self.servings_per_pack + ", ServingsPerPerson = " + self.servings_per_person + ", PacksNeeded = " + self.packs_needed + ", RawCost = " + self.raw_cost + " WHERE ItemID = " + self.item_id + ";"
			
			dbCurs.execute(strSQL)
			dbConn.commit()
			
			# Now we call get_all_items to update the items object with the updated item.
			self.get_all_items()
			
			# Close the database connection.
			dbConn.close()
	
		except Exception as dbError:
			print(dbError)	
		
	# ----------------------------------------
	# Delete an item.
	# ----------------------------------------
	def delete_item(self):
		
		try:
		
			# Create a database connection.
			dbConn = sqlite3.connect("dbCaterCalc.db")
			dbCurs = dbConn.cursor()
			
			# DELETE an item from the database.
			strSQL = "DELETE FROM SideItems WHERE ItemID = " + self.item_id + ";"
			
			dbCurs.execute(strSQL)
			dbConn.commit()
			
			# Now we call get_all_items to update the items object with the updated item.
			self.get_all_items()
			
			# Close the database connection.
			dbConn.close()
	
		except Exception as dbError:
			print(dbError)			
		
	# ----------------------------------------
	# Get a single item.
	# ----------------------------------------
	def get_item(self):	
		
		try:
		
			# Create a database connection.
			dbConn = sqlite3.connect("dbCaterCalc.db")
			dbCurs = dbConn.cursor()
			
			# SELECT all items from the database.
			strSQL = "SELECT * FROM SideItems WHERE ItemID = " + self.item_id + ";"
			dbCurs.execute(strSQL)
			
			# Populate the item dictionary from the database.
			for dbRec in dbCurs:
				self.item_id = dbRec[0]
				self.item_name = dbRec[1]
				self.price_per_pack = dbRec[2]
				self.servings_per_pack = dbRec[3]
				self.servings_per_person = dbRec[4]
				self.packs_needed = dbRec[5]
				self.raw_cost = dbRec[6]
			
			# Close the database connection.
			dbConn.close()
	
		except Exception as dbError:
			print(dbError)		
