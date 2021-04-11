import streamlit as st

st.title('Gift Help')
st.title('Made by Colin Murphy')
st.subheader('Maddox , Everett , Henry ')
st.text('Gift Help is a website to help find that perfect gift.')
interest_dict = {}
interest_dict['Origami'] = [
    [
    'Traditional Japanese Folding Papers and Projects',
    'org1.jpg',
    'https://www.amazon.com/Amazing-Origami-Kit-Traditional-Japanese/dp/0804841918/ref=sr_1_3?dchild=1&keywords=origami&qid=1618078443&sr=8-3'
    ],

    [
    'Origami for Beginners: Origami Kit',
    'org2.jpg',
    'https://www.amazon.com/Origami-Beginners-Projects-Animals-Parties/dp/B08B7RGWV3/ref=sr_1_7_sspa?dchild=1&keywords=origami&qid=1618081111&sr=8-7-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFSSTU3UFpTMkVZOE8mZW5jcnlwdGVkSWQ9QTA3ODQ1MzdVOENYWUdUN0dGOTkmZW5jcnlwdGVkQWRJZD1BMTAyMTM0NjI2UERJWkY4S1RYSkQmd2lkZ2V0TmFtZT1zcF9tdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
    ],

    ['The Complete Book of Origami',
    'org3.jpg',
    'https://www.amazon.com/Complete-Book-Origami-Step-Instructions/dp/0486258378/ref=sr_1_18_sspa?dchild=1&keywords=origami&qid=1618081325&sr=8-18-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySTVMNTJPVVU0SVc4JmVuY3J5cHRlZElkPUEwMzE5NDE1Mkc4MjRNNllBTUdXRyZlbmNyeXB0ZWRBZElkPUEwOTM2MTI5MVhOVFVaTDkwR05DMiZ3aWRnZXROYW1lPXNwX2F0Zl9uZXh0JmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ'
    ]
    ]

interest_dict['Gardening'] = [
    [
    'Vegetable Gardening for Beginners',
    'org4jpg.jpeg',
    'https://www.amazon.com/Vegetable-Gardening-Beginners-Hydroponics-Homesteading-ebook/dp/B0897W7GC2/ref=sr_1_4?dchild=1&keywords=gardening&qid=1618081602&sr=8-4'
    ],

    [
    'Garden Tools Set',
    'org5.jpg',
    'https://www.amazon.com/scuddles-Garden-Tools-Set-Gardening/dp/B07QF9TLFZ/ref=sxin_9_ac_d_rm?ac_md=1-1-Z2FyZGVuaW5nIHRvb2xz-ac_d_rm&cv_ct_cx=gardening&dchild=1&keywords=gardening&pd_rd_i=B07QF9TLFZ&pd_rd_r=45d6cb4b-9fac-45f4-9d03-f7e4a30ce9c2&pd_rd_w=d8XRT&pd_rd_wg=WgjBu&pf_rd_p=b0625ac1-ea22-4a1c-8206-57129b08e075&pf_rd_r=76PKCW0SHWV6TQTHYYAC&psc=1&qid=1618081740&sr=1-2-12d4272d-8adb-4121-8624-135149aa9081'
    ],

    ['Gardening for Kids',
    'org6.jpg',
    'https://www.amazon.com/Gardening-Kids-Learn-Messy-Projects-ebook/dp/B08NWDKQNJ/ref=sr_1_1_sspa?dchild=1&keywords=gardening&qid=1618081990&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE0Vk44VVlESlpHQTgmZW5jcnlwdGVkSWQ9QTA1MzIxNzlXREpZWDVBNDQ3U1YmZW5jcnlwdGVkQWRJZD1BMTA0ODA5NDM2WDFOWDBXUTIzTkkmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
    ]
    ]

interest_dict['Sports'] = [
    [
    'Franklin Sports Basketball Arcade Game',
    'org7.jpg',
    'https://www.amazon.com/Franklin-Sports-Electronic-Basketball-Bounce/dp/B009APUTS4/ref=sr_1_4?dchild=1&keywords=sports&qid=1618082192&sr=8-4'
    ],

    ['Sport Squad Endzone Challenge',
    'org8.jpg',
    'https://www.amazon.com/Sport-Squad-Football-Challenge-Backyard/dp/B071DQQW34/ref=sr_1_6?dchild=1&keywords=sports&qid=1618082390&sr=8-6'
    ],

    ['Franklin Sports MLB Electronic Baseball Pitching Machine',
    'org9.jpg',
    'https://www.amazon.com/Franklin-Sports-Electronic-Baseball-Pitching/dp/B0007DHT8Q/ref=sr_1_3?dchild=1&keywords=sports&qid=1618082498&sr=8-3'
    ]

    ['The Sports Gene',
    'org21.jpg',
    'https://www.amazon.com/Sports-Gene-Extraordinary-Athletic-Performance-ebook/dp/B00AEDDQKE/ref=sr_1_17?dchild=1&keywords=sports&qid=1618147181&sr=8-17'
    ]

    ['Spalding Basketball',
    'org22.jpg',
    'https://www.amazon.com/Spalding-74796-TF-500-Basketball/dp/B00F9KVFSM/ref=sr_1_1_sspa?dchild=1&keywords=basketball&qid=1618147325&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFTSEtZWlI1SkZRU00mZW5jcnlwdGVkSWQ9QTA4NjA4OTU4VTlGTEdUVDUxTTUmZW5jcnlwdGVkQWRJZD1BMDc3ODEzMzEzVlQzNEhKTUk0MUMmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
    ]
    ]

interest_dict['Fishing'] = [

    ['Fishing Vest',
    'org11.jpg',
    'https://www.amazon.com/Bassdash-Fishing-Adjustable-Outdoor-Activities/dp/B07CT13RKB/ref=sr_1_13?dchild=1&keywords=fishing&qid=1618082722&sr=8-13'
    ],

    ['Fishing Lures',
    'org12.jpg',
    'https://www.amazon.com/XTON-Including-Topwater-Freshwater-Saltwater/dp/B08P1TLR3T/ref=sr_1_28?dchild=1&keywords=fishing&qid=1618082722&sr=8-28'
    ]

    ['Fishing Rod',
    'org18.jpg',
    'https://www.amazon.com/PLUSINNO-Telescopic-Spinning-Saltwater-Freshwater/dp/B08Q7GBJTD/ref=sr_1_25?dchild=1&keywords=fishing&qid=1618146738&sr=8-25'
    ]

    ['The Total Fishing Manual',
    'org19.jpg',
    'https://www.amazon.com/Total-Fishing-Manual-Paperback-Essential/dp/1681882639/ref=sr_1_1_sspa?dchild=1&keywords=fishing+book&qid=1618146891&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUTNXSUdTUjI1RkhBJmVuY3J5cHRlZElkPUEwOTc4MzI1OVVYUVJEMzVGNllTJmVuY3J5cHRlZEFkSWQ9QTA2OTI0MzUyRTJEWlJTSEo0UlhCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    ]

    ['How to Think Like a Fish',
    'org20.jpg',
    'https://www.amazon.com/How-Think-Like-Fish-Lifetime-ebook/dp/B07H2BQ741/ref=sr_1_8?dchild=1&keywords=fishing+book&qid=1618147023&sr=8-8'
    ]
    ]

interest_dict['Travel'] = [

    [
    'Electronic Organizers',
    'org13.jpg',
    'https://www.amazon.com/Electronic-Organizers-Storage-Electronics-Accessories/dp/B0886BVQWY/ref=sr_1_19?dchild=1&keywords=travel&qid=1618082963&sr=8-19'
    ],

    ['Travel Organizer',
    'org14.jpg',
    'https://www.amazon.com/AmazonBasics-4-Piece-Packing-Cube-Set/dp/B014VBIEZQ/ref=sr_1_22?dchild=1&keywords=travel&qid=1618083136&sr=8-22'
    ],

    ['Toiletry Bag',
    'org15.jpg',
    'https://www.amazon.com/Toiletry-OMYSTYLE-Portable-Waterproof-Organizer/dp/B07Y9F7WXD/ref=sr_1_56_sspa?dchild=1&keywords=travel&qid=1618083136&sr=8-56-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFGRUZCWERDNlFKTE4mZW5jcnlwdGVkSWQ9QTAxMTE4MzgxN0xON1lTNzdXVzkyJmVuY3J5cHRlZEFkSWQ9QTA4MTkwNTAzSVRSMlgzNDc4NlAwJndpZGdldE5hbWU9c3BfYnRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    ]

    ['Softside Luggage',
    'org16.jpg',
    'https://www.amazon.com/SwissGear-Sion-24-Dark-Grey/dp/B014TDH23G/ref=sr_1_2_sspa?dchild=1&keywords=travel+suitcase&qid=1618146248&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUE0zMDZBT005R0xPJmVuY3J5cHRlZElkPUEwNTQ3OTI0MVkxTkdBV1I2UUdDRCZlbmNyeXB0ZWRBZElkPUEwMTU4NjI0M0NIVFZCRjk5NjdNSyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    ]

    ['Travel Pillow',
    'org17.jpg',
    'https://www.amazon.com/DYD-Airplane-Breathable-Washable-Ergonomic/dp/B07P8CDZ1Z/ref=sr_1_7?dchild=1&keywords=airplane+pillow&qid=1618146464&sr=8-7'
    ]
    ]



st.sidebar.header("Interests")
list = list(interest_dict.keys())
list.insert(0,'')
product = st.sidebar.selectbox('Choose a Interest', list)
if product == '':
    st.markdown('---')
else:
    items = interest_dict[product]
    x = len(items)

    for i in range (x):
        st.markdown('---')
        st.subheader(items[i][0])
        st.image(items[i][1], width=250)
        link = '[Link]('+ (items[i][2]) + ')'
        st.markdown(link, unsafe_allow_html=True)
