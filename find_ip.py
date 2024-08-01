import pandas as pd
import easygui
import time


# This will take an IP from the provided list and return a corresponding mac address (if found in the ise database export also uploaded to the script)
def find_ip(ip):
	try:
		mac = iseList[ip]
		return mac
	except:
		return 'Not Found'

# Main function calls the find_ip function and exports the results as an excel file
def main():
	ipDF['MAC'] = ipDF.apply(lambda row:find_ip(row['IP']), axis=1)
	t = time.strftime("%m-%d-%Y-%H-%M")
	ipDF.to_excel(f'IP-List-{t}.xlsx')


# We grab 2 docs from the user - ISE database export (Context Visibility) and the list of IP addresses we want the MAC for.
if __name__ == '__main__':

	print('Please provide the ISE database export file in a csv format')
	iseDF = pd.read_csv(easygui.fileopenbox())

	print('Please provide the IP list file in a xlsx format')
	ipDF = pd.read_excel(easygui.fileopenbox())

	# Create an empty dict for ip to mac binding
	iseList = {}

	# Removing extra data from the ISE database file
	cols = ['ip','MACAddress']
	iseDF = iseDF[cols]

	# Looping thru ISE database and assigning a key
	for ip,mac in zip(iseDF['ip'],iseDF['MACAddress']):
		if ip not in iseList:
			iseList[ip] = mac
		else:
			pass
	main()
