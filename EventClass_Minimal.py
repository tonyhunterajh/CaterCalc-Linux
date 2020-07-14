
		
class Event:
	
	def __init__(self):
		
		# ----------------------------------------
		# Initialize Attributes and Variables.
		# ----------------------------------------
		
		# Attributes of the class.
		self.event_id = ""
		self.event_name = ""
		self.event_date = ""
		self.guest_count = ""
		self.base_cost = ""
		self.labor_cost = ""
		
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
		
		self.cooked_lbs_needed = 0.00
		self.raw_lbs_needed = 0.00
		self.raw_cost = 0.00
		self.packs_needed = 0
		self.yield_pct = 0.00
		self.serving_size = 0
		self.price_per_lb = 0.00
		self.pieces_per_pack = 0
		self.pieces_per_person = 0
		self.price_per_pack = 0.00
		self.servings_per_pack = 0
		self.servings_per_person = 0
		self.meat_name = ""
		self.side_name = ""
		self.hasPerPoundItems = False
		self.hasPerPieceItems = False
		self.hasSideItems = False
		
	# ----------------------------------------
	# Add a Per Pound Meat.
	# ----------------------------------------
	def add_per_pound_meat(self, meat_name, serving_size, price_per_lb, yield_pct):
		
		self.meat_name = meat_name
		self.serving_size = serving_size
		self.price_per_lb = price_per_lb
		self.yield_pct = yield_pct
		
		# Calculate the meat information.
		self.cooked_lbs_needed = round((self.guest_count * self.serving_size) / 16)
		self.raw_lbs_needed = (self.cooked_lbs_needed - (self.cooked_lbs_needed * (self.yield_pct * 0.01))) + self.cooked_lbs_needed
		self.raw_cost = self.price_per_lb * self.raw_lbs_needed
		self.cost += self.raw_cost
		self.per_pound_item_count += 1
		
	# ----------------------------------------
	# Add a Per Piece Meat.
	# ----------------------------------------
	def add_per_piece_meat(self, meat_name, price_per_pack, pieces_per_pack, pieces_per_person):
		
		self.meat_name = meat_name
		self.price_per_pack = price_per_pack
		self.pieces_per_pack = pieces_per_pack
		self.pieces_per_person = pieces_per_person
		
		# Calculate the meat information.
		self.packs_needed = round((self.guest_count * self.pieces_per_person) / self.pieces_per_pack)
		self.raw_cost = self.price_per_pack * self.packs_needed
		self.cost += self.raw_cost
		self.per_piece_item_count += 1
		
	# ----------------------------------------
	# Add a Side Item.
	# ----------------------------------------
	def add_side_item(self, side_name, price_per_pack, servings_per_pack, servings_per_person):
		
		self.side_name = side_name
		self.price_per_pack = price_per_pack
		self.servings_per_pack = servings_per_pack
		self.servings_per_person = servings_per_person
		
		# Calculate the side information.
		self.packs_needed = round((self.guest_count * self.servings_per_person) / self.servings_per_pack)
		self.raw_cost = self.price_per_pack * self.packs_needed
		self.cost += self.raw_cost
		self.side_item_count += 1
		
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
	# Reset the entire event object.
	# ----------------------------------------
	def reset_event(self):	
		
		self.event_id = ""
		self.event_name = ""
		self.event_date = ""
		self.guest_count = ""
		self.base_cost = ""
		self.labor_cost = ""
		
		# Attributes calculated later.
		self.cost = 0.00
		self.revenue = 0.00
		self.profit = 0.00
		self.profit_margin = 0.00
		self.cost_per_person = 0.00
		self.deposit = 0.00
		
		self.cooked_lbs_needed = 0.00
		self.raw_lbs_needed = 0.00
		self.raw_cost = 0.00
		self.packs_needed = 0
		self.yield_pct = 0.00
		self.serving_size = 0
		self.price_per_lb = 0.00
		self.pieces_per_pack = 0
		self.pieces_per_person = 0
		self.price_per_pack = 0.00
		self.servings_per_pack = 0
		self.servings_per_person = 0
		self.meat_name = ""
		self.side_name = ""
		self.hasPerPoundItems = False
		self.hasPerPieceItems = False
		self.hasSideItems = False
		
		self.per_pound_item_count = 0
		self.per_piece_item_count = 0
		self.side_item_count = 0
