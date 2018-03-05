id = []
first_name = []
last_name = []
ssn_new = []
state_new = []
dob_new = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

import os
csvpath = os.path.join('raw_data', 'employee_data2.csv')

import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #  Each row is read as a row
    for row in csvreader:
        if row[0] != "Emp ID":
            id.append(row[0])
        name = row[1].split(" ")
        if row[1] != "Name":
            first_name.append(name[0])
            last_name.append(name[1])
        if row[2] != "DOB":
            dob = row[2].split("-")
            year = dob.pop()
            dob.append(year)
            new_dob = "/".join(dob)
            dob_new.append(new_dob)
        if row[3] != "SSN":
            ssn = row[3].split("-")
            for i in ssn:
                ssn[0] = "***"
                ssn[1] = "**"
                new_ssn = "-".join(ssn)
            ssn_new.append(new_ssn)
        state = row[4]
        if state in us_state_abbrev:
            state_new.append(us_state_abbrev[state])

employee = zip(id, first_name, last_name, dob_new, ssn_new, state_new)

output_path = os.path.join('output', 'emp-data-2-rev.csv')

#  Open the output file
with open(output_path, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write in zipped rows
    writer.writerows(employee)