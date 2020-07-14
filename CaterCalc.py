

import console
import ui
import EventClass_Minimal
import datetime
from prettytable import PrettyTable

# ----------------------------------------	
# Main View Functions.
# ----------------------------------------
#
def btnClose_Click(self):
	vwCC_Main.close()

def btnAdd_Per_Pound_Item_Click(self):
	
	# Display the screen.
	txtPerPoundItemName.text = ''
	txtPerPoundServingSize.text = ''
	txtPricePerPound.text = ''
	txtYieldPct.text = ''
	
	vwCC_PerPoundItem.present('sheet')
	
def btnAdd_Per_Piece_Item_Click(self):
	
	# Display the screen.
	txtPerPieceItemName.text = ''
	txtPerPiecePricePerPack.text = ''
	txtPerPiecePcsPerPack.text = ''
	txtPerPiecePcsPerPerson.text = ''
	
	vwCC_PerPieceItem.present('sheet')
		
def btnAdd_Side_Item_Click(self):
	
	# Display the screen.
	txtSideItemName.text = ''
	txtSidePricePerPack.text = ''
	txtSideServingsPerPack.text = ''
	txtSideServingsPerPerson.text = ''
	
	vwCC_SideItem.present('sheet')

def btnCalculate_Click(self):
	
	#
	# Perform Screen/Event Validation Before Calculation Attempts.
	#	
	hasEntryErrors = False
	
	if txtGuestCount.text == '0' or txtGuestCount.text == '':
		result = console.alert('Message...', 'Please Enter a Value for Guest Count.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
		
	if txtBaseCost.text == '0' and not hasEntryErrors or txtBaseCost.text == '' and not hasEntryErrors:
		result = console.alert('Message...', 'Please Enter a Value for Base Cost.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
		
	if txtLaborCost.text == '0' and not hasEntryErrors or txtLaborCost.text == '' and not hasEntryErrors:
		result = console.alert('Message...', 'Please Enter a Value for Labor Cost.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True			
		
	if (NewEvent.per_pound_item_count + NewEvent.per_piece_item_count + NewEvent.side_item_count) == 0 and not hasEntryErrors:
		result = console.alert('Message...', 'Please Add Items Before Calculating.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
			
	if not hasEntryErrors:
			
		# Calculate the Event.	
		populateEventInput()
		NewEvent.calculate_event()
		populateEventOutput()
		
		# Build the display HTML string based on the items entered by the user.
		strHTML = ''
		
		if NewEvent.hasPerPoundItems == True:
			strHTML += '<B>Per Pound Items</B>' + pt_per_pound_item.get_html_string()
			
		if NewEvent.hasPerPieceItems == True:
			strHTML += '<B>Per Piece Items</B>' + pt_per_piece_item.get_html_string()
			
		if NewEvent.hasSideItems == True:
			strHTML += '<B>Side Items</B>' + pt_side_item.get_html_string()
		
		wvEventDetails.load_html(strHTML)
		
def populateEventInput():
	
	# Populate the event object fields with what is entered on the screen.
	NewEvent.event_name = txtEventName.text
	NewEvent.guest_count = int(txtGuestCount.text)
	NewEvent.base_cost = float(txtBaseCost.text)
	NewEvent.labor_cost = float(txtLaborCost.text)
	
def populateEventOutput():
	
	# Populate the event object fields with the results of the calculation.
	txtCost.text = "${:,.2f}".format(NewEvent.cost)
	txtRevenue.text = "${:,.2f}".format(NewEvent.revenue)
	txtProfit.text = "${:,.2f}".format(NewEvent.profit)
	txtProfitMargin.text = "{:,.0f}%".format(NewEvent.profit_margin)
	txtCostPerPerson.text = "${:,.2f}".format(NewEvent.cost_per_person)
	txtDeposit.text = "${:,.2f}".format(NewEvent.deposit)
	
def btnPrintEventDetails_Click(self):
	
	# Print the Event data in table format.
	print("Customer Name: " + txtCustomerName.text)
	print("Event Name: " + txtEventName.text)
	print("Guest Count: " + txtGuestCount.text)
	print("Base Cost/Person: " + "${:,.2f}".format(float(txtBaseCost.text)))
	print("Labor Cost: " + "${:,.2f}".format(float(txtLaborCost.text)))
	print("")
	print("Cost/Person: " + txtCost.text)
	print("Revenue: " + txtRevenue.text)
	print("Pofit: " + txtProfit.text)
	print("Profit Margin: " + txtProfitMargin.text)
	print("Deposit: " + txtDeposit.text)
	print("")
	print(pt_per_pound_item)
	print("")
	print(pt_per_piece_item)
	print("")
	print(pt_side_item)
		
def btnResetEvent_Click(self):
	
	# Reset the Event data and screen.
	NewEvent.reset_event()
	
	# Set default values for the reset display of the screen.
	txtCustomerName.text = '(Enter a Customer Name)'
	txtEventName.text = '(Enter a Catering Event)'
	
	dtDateTime = datetime.datetime.now()
	txtEventDate.text = dtDateTime.strftime('%x')
	
	txtGuestCount.text = '25'
	txtBaseCost.text = '3.00'
	txtLaborCost.text = '50.00'
	
	txtCost.text = '0.00'
	txtRevenue.text = '0.00'
	txtProfit.text = '0.00'
	txtProfitMargin.text = '0.00'
	txtCostPerPerson.text = '0.00'
	txtDeposit.text = '0.00'
	
	lblPerPoundItemCount.text = '0'
	lblPerPieceItemCount.text = '0'
	lblSideItemCount.text = '0'
	
	hasEntryErrors = False
	wvEventDetails.load_html('')
	
	pt_per_pound_item.clear_rows()
	pt_per_piece_item.clear_rows()
	pt_side_item.clear_rows()
	
# ----------------------------------------	
# Date Picker View Functions.
# ----------------------------------------
#					
def btnDatePicker_Click(self):
	
	# Display the main screen.
	vwCC_Date.present('sheet')
				
def btnAcceptDate_Click(self):
	
	# Populate the Event Date with the selected date.
	dtSelectedDate = dtDatePicker.date
	txtEventDate.text = dtSelectedDate.strftime('%x')
	vwCC_Date.close()

def btnCancel_Click(self):
	
	# Close the date picker view.
	vwCC_Date.close()

# ----------------------------------------	
# Per Pound Item View Functions.
# ----------------------------------------
#					
def btnPerPoundItemSave_Click(self):
	
	#
	# Perform Screen Validation Before Accepting Input.
	#	
	hasEntryErrors = False
	
	if txtPerPoundItemName.text == '':
		result = console.alert('Message...', 'Please Enter a Value for Item Name.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
		
	if txtPerPoundServingSize.text == '0' and not hasEntryErrors or txtPerPoundServingSize.text == '' and not hasEntryErrors:
		result = console.alert('Message...', 'Please Enter a Value for Serving Size.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
		
	if txtPricePerPound.text == '0' and not hasEntryErrors or txtPricePerPound.text == '' and not hasEntryErrors:
		result = console.alert('Message...', 'Please Enter a Value for Price Per Pound.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
		
	if txtYieldPct.text == '0' and not hasEntryErrors or txtYieldPct.text == '' and not hasEntryErrors:
		result = console.alert('Message...', 'Please Enter a Value for Yield%.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True		
		
	if not hasEntryErrors:	
		# Per Pound Items
		# Parameters: Item Name, Serving Size, Price/Lb., Yeild %
		#
		populateEventInput()
		
		NewEvent.add_per_pound_meat(txtPerPoundItemName.text, int(txtPerPoundServingSize.text), float(txtPricePerPound.text), float(txtYieldPct.text))
		pt_per_pound_item.add_row([NewEvent.meat_name, NewEvent.serving_size, NewEvent.price_per_lb, NewEvent.yield_pct, NewEvent.cooked_lbs_needed, NewEvent.raw_lbs_needed, NewEvent.raw_cost])
		
		NewEvent.hasPerPoundItems = True
		lblPerPoundItemCount.text = str(NewEvent.Per_Pound_Item_Count)
	
		# Close the view.
		vwCC_PerPoundItem.close()
	
def btnPerPoundItemCancel_Click(self):
	
	# Close the view.
	vwCC_PerPoundItem.close()	
	
# ----------------------------------------	
# Per Piece Item View Functions.
# ----------------------------------------
#					
def btnPerPieceItemSave_Click(self):
	
	#
	# Perform Screen Validation Before Accepting Input.
	#	
	hasEntryErrors = False
	
	if txtPerPieceItemName.text == '':
		result = console.alert('Message...', 'Please Enter a Value for Item Name.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
		
	if txtPerPiecePricePerPack.text == '0' and not hasEntryErrors or txtPerPiecePricePerPack.text == '' and not hasEntryErrors:
		result = console.alert('Message...', 'Please Enter a Value for Price Per Pack.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
		
	if txtPerPiecePcsPerPack.text == '0' and not hasEntryErrors or txtPerPiecePcsPerPack.text == '' and not hasEntryErrors:
		result = console.alert('Message...', 'Please Enter a Value for Pieces Per Pack.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
		
	if txtPerPiecePcsPerPerson.text == '0' and not hasEntryErrors or txtPerPiecePcsPerPerson.text == '' and not hasEntryErrors:
		result = console.alert('Message...', 'Please Enter a Value for Pieces Per Person.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True		
		
	if not hasEntryErrors:
		# Per Piece Items
		# Parameters: Item Name, Price/Pack, Pieces/Pack, Pieces/Person
		#	
		populateEventInput()
		NewEvent.add_per_piece_meat(txtPerPieceItemName.text, float(txtPerPiecePricePerPack.text), int(txtPerPiecePcsPerPack.text), int(txtPerPiecePcsPerPerson.text))
		pt_per_piece_item.add_row([NewEvent.meat_name, NewEvent.price_per_pack, NewEvent.pieces_per_pack, NewEvent.pieces_per_person, NewEvent.packs_needed, NewEvent.raw_cost])
		
		NewEvent.hasPerPieceItems = True
		lblPerPieceItemCount.text = str(NewEvent.Per_Piece_Item_Count)
		
		# Close the view.
		vwCC_PerPieceItem.close()
	
def btnPerPieceItemCancel_Click(self):
	
	# Close the view.
	vwCC_PerPieceItem.close()		
	
# ----------------------------------------	
# Side Item View Functions.
# ----------------------------------------
#					
def btnSideItemSave_Click(self):
	
	#
	# Perform Screen Validation Before Accepting Input.
	#	
	hasEntryErrors = False
	
	if txtSideItemName.text == '':
		result = console.alert('Message...', 'Please Enter a Value for Item Name.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
		
	if txtSidePricePerPack.text == '0' and not hasEntryErrors or txtSidePricePerPack.text == '' and not hasEntryErrors:
		result = console.alert('Message...', 'Please Enter a Value for Price Per Pack.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
		
	if txtSideServingsPerPack.text == '0' and not hasEntryErrors or txtSideServingsPerPack.text == '' and not hasEntryErrors:
		result = console.alert('Message...', 'Please Enter a Value for Servings Per Pack.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True
		
	if txtSideServingsPerPerson.text == '0' and not hasEntryErrors or txtSideServingsPerPerson.text == '' and not hasEntryErrors:
		result = console.alert('Message...', 'Please Enter a Value for Servings Per Person.', hide_cancel_button=True, button1='OK')
		hasEntryErrors = True		
		
	if not hasEntryErrors:
		# Side Items
		# Parameters: Item Name, Price/Pack, Servings/Pack, Servings/Person
		#		
		populateEventInput()
		NewEvent.add_side_item(txtSideItemName.text, float(txtSidePricePerPack.text), int(txtSideServingsPerPack.text), int(txtSideServingsPerPerson.text))
		pt_side_item.add_row([NewEvent.side_name, NewEvent.price_per_pack, NewEvent.servings_per_pack, NewEvent.servings_per_person, NewEvent.packs_needed, NewEvent.raw_cost])
		
		NewEvent.hasSideItems = True
		lblSideItemCount.text = str(NewEvent.Side_Item_Count)
		
		# Close the view.
		vwCC_SideItem.close()
	
def btnSideItemCancel_Click(self):
	
	# Close the view.
	vwCC_SideItem.close()		
	
# ----------------------------------------	
# Main program flow.
# ----------------------------------------	

# Global variable definitions.
#
# Pretty Table definitions for printing results.
pt_per_pound_item = PrettyTable(["Item Name", "Serving Size", "Price/Lb.", "Yeild%", "Cooked Needed", "Raw Needed", "Raw Cost"])
pt_per_pound_item.align['Item Name'] = 'l'
pt_per_pound_item.align['Serving Size'] = 'c'
pt_per_pound_item.align['Price/Lb.'] = 'r'
pt_per_pound_item.align['Yeild%'] = 'c'
pt_per_pound_item.align['Cooked Needed'] = 'c'
pt_per_pound_item.align['Raw Needed'] = 'c'
pt_per_pound_item.align['Raw Cost'] = 'r'

pt_per_piece_item = PrettyTable(["Item Name", "Price/Pack", "Pieces/Pack", "Pieces/Person", "Packs Needed", "Raw Cost"])
pt_per_piece_item.align['Item Name'] = 'l'
pt_per_piece_item.align['Price/Pack'] = 'r'
pt_per_piece_item.align['Pieces/Pack'] = 'c'
pt_per_piece_item.align['Pieces/Person'] = 'c'
pt_per_piece_item.align['Packs Needed'] = 'c'
pt_per_piece_item.align['Raw Cost'] = 'r'

pt_side_item = PrettyTable(["Item Name", "Price/Pack", "Servings/Pack", "Servings/Person", "Packs Needed", "Raw Cost"])
pt_side_item.align['Item Name'] = 'l'
pt_side_item.align['Price/Pack'] = 'r'
pt_side_item.align['Servings/Pack'] = 'c'
pt_side_item.align['Servings/Person'] = 'c'
pt_side_item.align['Packs Needed'] = 'c'
pt_side_item.align['Raw Cost'] = 'r'

hasEntryErrors = False

# Create a new Event.
NewEvent = EventClass_Minimal.Event()

#----------------------------------------
# Load the main UI view
#----------------------------------------
vwCC_Main = ui.load_view('CaterCalcGUI')

# Define the main screen input fields.
txtCustomerName = vwCC_Main['txtCustomerName']
txtEventName = vwCC_Main['txtEventName']
txtEventDate = vwCC_Main['txtEventDate']
txtGuestCount = vwCC_Main['txtGuestCount']
txtBaseCost = vwCC_Main['txtBaseCost']
txtLaborCost = vwCC_Main['txtLaborCost']

# Define the output results fields.
txtCost = vwCC_Main['txtCost']
txtRevenue = vwCC_Main['txtRevenue']
txtProfit = vwCC_Main['txtProfit']
txtProfitMargin = vwCC_Main['txtProfitMargin']
txtCostPerPerson = vwCC_Main['txtCostPerPerson']
txtDeposit = vwCC_Main['txtDeposit']
wvEventDetails = vwCC_Main['wvEventDetails']
tvEventDetails = vwCC_Main['tvEventDetails']

lblPerPoundItemCount = vwCC_Main['lblPerPoundItemCount']
lblPerPieceItemCount = vwCC_Main['lblPerPieceItemCount']
lblSideItemCount = vwCC_Main['lblSideItemCount']

# Set default values for the first display of the screen.
txtCustomerName.text = '(Enter a Customer Name)'
txtEventName.text = '(Enter a Catering Event)'

dtDateTime = datetime.datetime.now()
txtEventDate.text = dtDateTime.strftime('%x')

txtGuestCount.text = '25'
txtBaseCost.text = '3.00'
txtLaborCost.text = '50.00'

txtCost.text = '0.00'
txtRevenue.text = '0.00'
txtProfit.text = '0.00'
txtProfitMargin.text = '0.00'
txtCostPerPerson.text = '0.00'
txtDeposit.text = '0.00'

lblPerPoundItemCount.text = '0'
lblPerPieceItemCount.text = '0'
lblSideItemCount.text = '0'

txtCost.enabled = False
txtRevenue.enabled = False
txtProfit.enabled = False
txtProfitMargin.enabled = False
txtCostPerPerson.enabled = False
txtDeposit.enabled = False

# Display the main screen.
vwCC_Main.present('sheet')

#----------------------------------------
# Load the Date Picker UI view
#----------------------------------------
vwCC_Date = ui.load_view('DatePicker')
dtDatePicker = vwCC_Date['dpEventDate']

#----------------------------------------
# Load the Per Pound Item screen.
#----------------------------------------
vwCC_PerPoundItem = ui.load_view('PerPoundItem')

txtPerPoundItemName = vwCC_PerPoundItem['txtItemName']
txtPerPoundServingSize = vwCC_PerPoundItem['txtServingSize']
txtPricePerPound = vwCC_PerPoundItem['txtPricePerPound']
txtYieldPct = vwCC_PerPoundItem['txtYieldPct']

#----------------------------------------
# Load the Per Piece Item screen.
#----------------------------------------
vwCC_PerPieceItem = ui.load_view('PerPieceItem')

txtPerPieceItemName = vwCC_PerPieceItem['txtItemName']
txtPerPiecePricePerPack = vwCC_PerPieceItem['txtPricePerPack']
txtPerPiecePcsPerPack = vwCC_PerPieceItem['txtPiecesPerPack']
txtPerPiecePcsPerPerson = vwCC_PerPieceItem['txtPiecesPerPerson']

#----------------------------------------
# Load the Side Item screen.
#----------------------------------------
vwCC_SideItem = ui.load_view('SideItem')

txtSideItemName = vwCC_SideItem['txtItemName']
txtSidePricePerPack = vwCC_SideItem['txtPricePerPack']
txtSideServingsPerPack = vwCC_SideItem['txtServingsPerPack']
txtSideServingsPerPerson = vwCC_SideItem['txtServingsPerPerson']
