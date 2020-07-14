

import sqlite3
import json
from prettytable import PrettyTable

		
class Event:
	
	def __init__(self, customer_id):
		
		# ----------------------------------------
		# Initialize Attributes and Variables.
		# ----------------------------------------
		
		# Attributes of the class.
		self.events_DICT = {}
		
		self.customer_id = customer_id
		self.event_id = ""
		self.event_name = ""
		self.event_date = ""
		self.guest_count = ""
		self.base_cost = ""
		self.labor_cost = ""

		self.hasPerPoundItems = False
		self.hasPerPieceItems = False
		self.hasSideItems = False
		
		self.per_pound_item_count = 0
		self.per_piece_item_count = 0
		self.side_item_count = 0
		
		# Attributes calculated later.
		self.cost = 0.00
		self.revenue = 0.00
		self.profit = 0.00
		self.profit_margin = 0.00
		self.cost_per_person = 0.00
		self.deposit = 0.00
		
		# Pretty Table definitions for printing results.
		self.pt_per_pound_item = PrettyTable()
		self.pt_per_pound_item.field_names = ("Item Name", "Serving Size", "Price/Lb.", "Yeild%", "Cooked Needed", "Raw Needed", "Raw Cost")
		
		self.pt_per_piece_item = PrettyTable()
		self.pt_per_piece_item.field_names = ("Item Name", "Price/Pack", "Pieces/Pack", "Pieces/Person", "Packs Needed", "Raw Cost")
		
		self.pt_side_item = PrettyTable()
		self.pt_side_item.field_names = ("Item Name", "Price/Pack", "Servings/Pack", "Servings/Person", "Packs Needed", "Raw Cost")
		
	# ----------------------------------------
	# Get all events.
	# ----------------------------------------
	def get_all_events(self):	
		
		try:
		
			# Clear the Events dictionary.
			self.events_DICT.clear()
			
			# Create a database connection.
			dbConn = sqlite3.connect("dbCaterCalc.db")
			dbCurs = dbConn.cursor()
			
			# SELECT all events from the database.
			strSQL = "SELECT * FROM Events;"
			dbCurs.execute(strSQL)
			
			# Populate event class dictionary from the database.
			for dbRec in dbCurs:
				
				# Initialize the event dictionaries.
				self.eventID_DICT = {} 
				self.event_DICT = {}
				
				# Add an event dictionary to a dictionary for the event id.
				self.eventID_DICT[dbRec[0]] = self.event_DICT
				
				# Populate the custmer dictionary from the database.
				self.event_DICT["event_name"] = dbRec[1]
				self.event_DICT["event_date"] = dbRec[2]
				self.event_DICT["guest_count"] = dbRec[3]
				self.event_DICT["base_cost"] = dbRec[4]
				self.event_DICT["labor_cost"] = dbRec[5]
				self.event_DICT["cost_per_person"] = dbRec[6]
				self.event_DICT["revenue"] = dbRec[7]
				self.event_DICT["profit"] = dbRec[8]
				self.event_DICT["profit_margin"] = dbRec[9]
				self.event_DICT["deposit"] = dbRec[10]
				self.event_DICT["customer_id"] = dbRec[11]
			
				# Add the event dictionary to the main events dictionary.		
				self.events_DICT = self.eventID_DICT
			
			# Close the database connection.
			dbConn.close()
	
		except Exception as dbError:
			print(dbError)
				
	# ----------------------------------------
	# Add new event.
	# ----------------------------------------
	def add_event(self):
		
		try:
		
			# Create a database connection.
			dbConn = sqlite3.connect("dbCaterCalc.db")
			dbCurs = dbConn.cursor()
			
			# INSERT the current event into the database.
			strSQL = "INSERT INTO Events (EventName, EventDate, GuestCount, BaseCost, LaborCost, CostPerPerson, Revenue, Profit, ProfitMargin, Deposit, CustomerID) VALUES (" + "'" + self.event_name + "'" + "," + "{:,.0f}".format(self.guest_count) + "," + "{:,.2f}".format(self.base_cost) + "," + "{:,.2f}".format(self.labor_cost) + "," + "{:,.2f}".format(self.cost_per_person) + "," + "{:,.0f}".format(self.revenue) + "," + "{:,.2f}".format(self.profit) + "," + "{:,.0f}".format(self.profit_margin) + "," + "{:,.2f}".format(self.deposit) + "," + self.customer_id + ");"
			
			dbCurs.execute(strSQL)
			
			# Get the last row id as the event id.
			self.event_id = dbCurs.lastrowid()
			
			dbConn.commit()
			
			# Close the database connection.
			dbConn.close()
	
		except Exception as dbError:
			print(dbError)		

	# ----------------------------------------
	# Update a event.
	# ----------------------------------------9
	def update_event(self):
		
		try:
		
			# Create a database connection.
			dbConn = sqlite3.connect("dbCaterCalc.db")
			dbCurs = dbConn.cursor()
			
			# UPDATE an event in the database.
			strSQL = "UPDATE Events SET EventName = " + self.event_name + ", GuestCount = " + "{:,.0f}".format(self.guest_count) + ", BaseCost = " + "{:,.2f}".format(self.base_cost) + ", LaborCost = " + "{:,.2f}".format(self.labor_cost) + ", CostPerPerson = " + "{:,.2f}".format(self.cost_per_person) + ", Revenue = " + "{:,.0f}".format(self.revenue) + ", Profit = " + "{:,.2f}".format(self.profit) + ", ProfitMargin" + "{:,.0f}".format(self.profit_margin) + ", Deposit = " + "{:,.2f}".format(self.deposit) + ", CustomerID = " + self.customer_id + ");"
			
			dbCurs.execute(strSQL)
			dbConn.commit()
			
			# Now we call get_all_events to update the events object with the updated event.
			self.get_all_events()
			
			# Close the database connection.
			dbConn.close()
	
		except Exception as dbError:
			print(dbError)	
		
	# ----------------------------------------
	# Delete an event.
	# ----------------------------------------
	def delete_event(self):
		
		try:
		
			# Create a database connection.
			dbConn = sqlite3.connect("dbCaterCalc.db")
			dbCurs = dbConn.cursor()
			
			# DELETE an Event from the database.
			strSQL = "DELETE FROM Events WHERE EventID = " + self.event_id + ";"
			
			dbCurs.execute(strSQL)
			dbConn.commit()
			
			# Now we call get_all_events to update the events object with the deleted event.
			self.get_all_events()()
			
			# Close the database connection.
			dbConn.close()
	
		except Exception as dbError:
			print(dbError)			
		
	# ----------------------------------------
	# Get a single event.
	# ----------------------------------------
	def get_event(self):	
		
		try:
		
			# Create a database connection.
			dbConn = sqlite3.connect("dbCaterCalc.db")
			dbCurs = dbConn.cursor()
			
			# SELECT all events from the database.
			strSQL = "SELECT * FROM Events WHERE EventID = " + self.event_id + ";"
			dbCurs.execute(strSQL)
			
			# Populate the customer dictionary from the database.
			for dbRec in dbCurs:
				self.event_id = dbRec[0]
				self.event_name = dbRec[1]
				self.event_date = dbRec[2]
				self.guest_count = dbRec[3]
				self.base_cost = dbRec[4]
				self.labor_cost = dbRec[5]
				self.cost_per_person = dbRec[6]
				self.revenue = dbRec[7]
				self.profit = dbRec[8]
				self.profit_margin = dbRec[9]
				self.deposit = dbRec[10]
				self.customer_id = dbRec[11]
			
			# Close the database connection.
			dbConn.close()
	
		except Exception as dbError:
			print(dbError)
			
	# ----------------------------------------
	# Add a Per Pound Meat.
	# ----------------------------------------
	def add_per_pound_meat(self, meat_name, serving_size, price_per_lb, yield_pct, event_id):
		
		# Calculate the meat information.
		cooked_lbs_needed = round((self.guest_count * serving_size) / 16)
		raw_lbs_needed = (cooked_lbs_needed - (cooked_lbs_needed * (yield_pct * 0.01))) + cooked_lbs_needed
		raw_cost = price_per_lb * raw_lbs_needed
		self.cost += raw_cost
		
		# Add a row to the per pound items table for display and print.
		self.pt_per_pound_item.add_row([meat_name, serving_size, price_per_lb, yield_pct, cooked_lbs_needed, raw_lbs_needed, raw_cost])
		
	# ----------------------------------------
	# Add a Per Piece Meat.
	# ----------------------------------------
	def add_per_piece_meat(self, meat_name, price_per_pack, pieces_per_pack, pieces_per_person, event_id):
		
		# Calculate the meat information.
		packs_needed = round((self.guest_count * pieces_per_person) / pieces_per_pack)
		raw_cost = price_per_pack * packs_needed
		self.cost += raw_cost
		
		# Add a row to the per piece items table for display and print.
		self.pt_per_piece_item.add_row([meat_name, price_per_pack, pieces_per_pack, pieces_per_person, packs_needed, raw_cost])
		
	# ----------------------------------------
	# Add a Side Item.
	# ----------------------------------------
	def add_side_item(self, side_name, price_per_pack, servings_per_pack, servings_per_person, event_id):
		
		# Calculate the side information.
		packs_needed = round((self.guest_count * servings_per_person) / servings_per_pack)
		raw_cost = price_per_pack * packs_needed
		self.cost += raw_cost
		
		# Add a row to the per piece items table for display and print.
		self.pt_side_item.add_row([side_name, price_per_pack, servings_per_pack, servings_per_person, packs_needed, raw_cost])
		
	# ----------------------------------------
	# Calculate the event financials.
	# ----------------------------------------
	def calculate_event(self):
		
		# Calculate the event information.
		self.cost_per_person = round(((self.base_cost * self.guest_count) + self.labor_cost + self.cost) / self.guest_count)
		self.revenue = self.cost_per_person * self.guest_count
		self.profit = self.revenue - self.cost
		self.profit_margin = round(int(((self.profit / self.cost)-1) * 100))
		self.deposit = round(self.revenue / 2)
		
	# ----------------------------------------
	# Print the current event.
	# ----------------------------------------
	def print_event(self):
		
		# Print the Event data in table format.
		print("")
		print("Event Name: " + self.event_name)
		print("Guest Count: " + "{:,.0f}".format(self.guest_count))
		print("Base Cost/Person: " + "${:,.2f}".format(self.base_cost))
		print("Labor Cost: " + "${:,.2f}".format(self.labor_cost))
		print("")
		print("Cost/Person: " + "${:,.2f}".format(self.cost_per_person))
		print("Revenue: " + "{:,.0f}".format(self.revenue))
		print("Pofit: " + "${:,.2f}".format(self.profit))
		print("Profit Margin: " + "{:,.0f}%".format(self.profit_margin))
		print("Deposit: " + "${:,.2f}".format(self.deposit))
		print("")
		print(self.pt_per_pound_item)
		print("")
		print(self.pt_per_piece_item)
		print("")
		print(self.pt_side_item)
