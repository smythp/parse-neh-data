import sys
import sqlite3
import xml.etree.ElementTree as ET


tree = ET.parse(sys.argv[1])
# tree = ET.parse('NEH_Grants2010s.xml')
root = tree.getroot()

fields = (
    'ApplicantType',
    'Institution',
    'OrganizationType',
    'InstCity',
    'InstState',
    'InstPostalCode',
    'InstCountry',
    'CouncilDate',
    'YearAwarded',
    'ProjectTitle',
    'Program',
    'Division',
    'ApprovedOutright',
    'ApprovedMatching',
    'AwardOutright',
    'AwardMatching',
    'OriginalAmount',
    'BeginGrant',
    'EndGrant',
    'ProjectDesc',
    'ToSupport',
    'PrimaryDiscipline',
    'SupplementCount',
    'ParticipantCount',
    'DisciplineCount'
    )

explicit_fields = ''

for field in fields:
    explicit_fields += field
    explicit_fields += ', '

explicit_fields = explicit_fields[:-2]    

conn = sqlite3.connect('grants.db')
cur = conn.cursor()


for grant in root:
    data_list = []
    for field in fields:

        data_list.append(grant.find(field).text)
        # print(data_list)
    # print(len(tuple(data_list)))
    # print(type(tuple(data_list)))
    
    cur.execute("INSERT INTO grants (%s) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);" % explicit_fields, tuple(data_list))

conn.commit()    




    
# for grant in root:
#     state = grant.find('InstState').text
#     matching = float(grant.find('AwardMatching').text)
#     outright = float(grant.find('AwardOutright').text)
#     award = matching + outright


#     if state == 'CA' or state == 'ca':
#         # print(state)
#         print(matching)
#         print(outright)
#         print(award)
#         print()
#         ca_total += award
#         ca_total_matching += matching
#         ca_total_outright += outright

# print("Total all", ca_total)
# print("Total matching", ca_total_matching)
# print("Total outright", ca_total_outright)
