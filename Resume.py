# Text Variables
Header = '>> Made in Python using Matplolib'
Name = 'UJJWAL KSHIRSAGAR'
Title = ' PROGRAMMER'
Contact = 'Flat no-204,Mayfair Elegant Tadiwala road\nPune - 411001\nujjwalkshirsagar@gmail.com\nhttps://www.linkedin.com/in/ujjwalkshirsa\ngar/'
ProjectsHeader = 'PARTICIPATION'
ProjectOneTitle = 'Nakshatra Club MESCOE'
ProjectOneDesc = '- Discussions About Astrophysics\n- Routine Cosmos Quizes\n- Updates of Space Events  '
ProjectTwoTitle = 'ETSA Innerve 2020'
ProjectTwoDesc = '- Event Head of "Sherlock Holmes" Event\n- Non-technical Event Co-ordinator '
ProjectThreeTitle = 'Python Projects'
ProjectThreeDesc = '- "Tic Tac Toe Game" using jupyter notebook\n-  Coin Flip Guessing and Average Calculaor'
Portfolio = ''
WorkHeader = 'Education'
WorkOneTitle = 'Modern Education Societies College of Engineering Pune'
WorkOneTime = ''
WorkOneDesc = '- Pursuing\n- Graduating with 7.392 SGPA (Till Sem 6)\n'
WorkTwoTitle = 'KTHM Nashik'
WorkTwoTime = ''
WorkTwoDesc = '    - H.S.C From Maharastra State Board\n \n'
WorkThreeTitle = 'Good Shephard Academy English Medium Sakri'
WorkThreeTime = ''
WorkThreeDesc = '- S.S.C From Maharastra State Board \n'
EduHeader = 'CERTIFICATIONS'
EduOneTitle = '\n \nPython Programming - From Basics to Advanced level [2021]'
EduOneTime = ''
EduOneDesc = ''
EduTwoTitle = 'The Fundamental of Digital Marketing'
EduTwoTime = ''
SkillsHeader = 'Skills'
SkillsDesc = '- Python\n- C Programming\n- C++ Programming \n- HTML5\n- Github\n- Excel\n- Team Managment\n- Communication'
ExtrasTitle = ''
ExtrasDesc = 'Enthusiastic and eager to \ncontribute to team success \nthrough hard work,attention\nto detail and organizational \nskills . Looking forward to \nClear understanding of Team \nCo-ordination and training , \nMotivated to learn, grow and \nexcel'
CodeTitle = 'View Profile'

# Setting style for bar graphs
import matplotlib.pyplot as plt
%matplotlib inline

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

fig, ax = plt.subplots(figsize=(8.5, 11))
# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add text
plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.6)
plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)
plt.annotate(Contact, (.7,.906), weight='regular', fontsize=8, color='#ffffff')
plt.annotate(WorkHeader, (.02,.86), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(WorkOneTitle, (.02,.832), weight='bold', fontsize=10)
plt.annotate(WorkOneDesc, (.04,.78), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02,.745), weight='bold', fontsize=10)
plt.annotate(WorkTwoDesc, (.02,.70), weight='regular', fontsize=9)
plt.annotate(WorkThreeTitle, (.02,.672), weight='bold', fontsize=10)
plt.annotate(WorkThreeDesc, (.04,.638), weight='regular', fontsize=9)
plt.annotate(Portfolio, (.02,.6), weight='bold', fontsize=10)

plt.annotate(ProjectsHeader, (.02,.54), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(ProjectOneTitle, (.02,.508), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02,.493), weight='regular', fontsize=9, alpha=.6)
plt.annotate(ProjectOneDesc, (.04,.445), weight='regular', fontsize=9)
plt.annotate(ProjectTwoTitle, (.02,.4), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02,.385), weight='regular', fontsize=9, alpha=.6)
plt.annotate(ProjectTwoDesc, (.04,.337), weight='regular', fontsize=9)
plt.annotate(ProjectThreeTitle, (.02,.295), weight='bold', fontsize=10)
plt.annotate(WorkThreeTime, (.02,.28), weight='regular', fontsize=9, alpha=.6)
plt.annotate(ProjectThreeDesc, (.04,.247), weight='regular', fontsize=9)
plt.annotate(EduHeader, (.02,.185), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(EduOneTitle, (.02,.155), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (.02,.14), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduOneDesc, (.04,.125), weight='regular', fontsize=9)
plt.annotate(EduTwoTitle, (.02,.08), weight='bold', fontsize=10)
plt.annotate(EduTwoTime, (.02,.065), weight='regular', fontsize=9, alpha=.6)
plt.annotate(SkillsHeader, (.7,.80), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7,.65), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(ExtrasTitle, (.7,.43), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(ExtrasDesc, (.7,.345), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(CodeTitle, (.7,.2), weight='bold', fontsize=10, color='#ffffff')

#add qr code
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
arr_code = mpimg.imread('QR.png')
imagebox = OffsetImage(arr_code, zoom=0.3)
ab = AnnotationBbox(imagebox, (0.84, 0.12))
ax.add_artist(ab)

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('svg', 'pdf')
plt.savefig('resumeexample.png', dpi=400, bbox_inches='tight')
