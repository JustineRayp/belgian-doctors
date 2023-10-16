import circlify
import matplotlib.pyplot as plt
import pro_capite_data
import pro_capite_region
from statistics import mean

data = [{'id': 'World', 'datum': 16263, 'children': [
    {'id': "Belgium", 'datum': 16263,
     'children': [
         {'id': "Flanders", 'datum': 9204, 'children': [
             {'id': "Antwerp", 'datum': 2387},
             {'id': "East Flanders", 'datum': 2104},
             {'id': "Vlaams Brabant", 'datum': 1875},
             {'id': "West Flanders", 'datum': 1661},
             {'id': "Limburg", 'datum': 1177}
         ]},
         {'id': "Wallonia", 'datum': 5460, 'children': [
             {'id': "Hainaut", 'datum': 1701},
             {'id': "Liège", 'datum': 1661},
             {'id': "Namur", 'datum': 895},
             {'id': "Walloon Brabant", 'datum': 799},
             {'id': "Luxembourg", 'datum': 404}
         ]},
         {'id': "Brussels", 'datum': 1599}
     ]}
]}]

colors_dict = {'Hainaut': [0.9686274509803922, 0.9882352941176471, 0.9607843137254902, 1.0],
 'Antwerp': [0.9641983852364475, 0.9865128796616687, 0.9556170703575548, 1.0],
 'Brussels': [0.9287658592848904, 0.9727335640138408, 0.9142791234140715, 1.0],
 'Limburg': [0.9132641291810842, 0.9667051134179162, 0.8961937716262975, 1.0],
 'East Flanders': [0.8754325259515571, 0.9517416378316033, 0.8543175701653211, 1.0],
 'West Flanders': [0.8606689734717416, 0.9458362168396771, 0.8385697808535179, 1.0],
 'Luxembourg': [0.8422145328719723, 0.9384544405997693, 0.818885044213764, 1.0],
 'Liège': [0.6716955017301038, 0.8679584775086505, 0.6471049596309112, 1.0],
 'Vlaams Brabant': [0.46874279123414075, 0.7750865051903114, 0.47412533640907345, 1.0],
 'Namur': [0.11249519415609383, 0.5238754325259515, 0.2529027297193387, 1.0],
 'Walloon Brabant': [0.0, 0.26666666666666666, 0.10588235294117647, 1.0]}

colors_dict_region = {'Brussels': (0.403921568627451, 0.0, 0.05098039215686274, 1.0),
 'Flanders': (0.9437139561707035, 0.25667051134179164, 0.18869665513264128, 1.0),
 'Wallonia': (1.0, 0.9607843137254902, 0.9411764705882353, 1.0)}


def print_corresponding_color(id):
    try:
        return colors_dict[id]
    except:
        return '#cacae2'


def get_correct_alpha(id):
    if id == 'Brussels':
        return 1
    else:
        return 0.5

def label_position(id):
    if id == "East Flanders":
        return "top"
    else:
        return "center"

# Compute circle positions thanks to the circlify() function
circles = circlify.circlify(data, show_enclosure=False, target_enclosure=circlify.Circle(x=0, y=0, r=1))

fig, ax = plt.subplots(figsize=(14, 14))
ax.set_title('Patient-to-Doctor ratios across belgian provinces')
ax.axis('off')

# Find axis boundaries
lim = max(max(abs(circle.x) + circle.r, abs(circle.y) + circle.r) for circle in circles)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

for circle in circles:
    if circle.level != 2:
        continue
    x, y, r = circle
    ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=0, color="lightblue"))

for circle in circles:
    if circle.level != 2:
        continue
    x, y, r = circle
    label = circle.ex["id"]

for circle in circles:
    if circle.level != 3:
        continue
    x, y, r = circle
    label = circle.ex["id"]
    if label in colors_dict_region:  # Check if the label is in the colors_dict
        color = colors_dict_region[label]  # Get the color from colors_dict
        ax.add_patch(plt.Circle((x, y), r, alpha=get_correct_alpha(label), linewidth=0, color=color))
    #ax.add_patch(plt.Circle((x, y), r, alpha=get_correct_alpha(circle.ex['id']), linewidth=0,
                            #color=print_corresponding_color(circle.ex['id'])))
    if label == "Flanders":
        plt.annotate(label, (x - r * 0.8, y - r * 0.45), va='top', ha='left', color="black",
                     bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.2), fontsize=14)
    elif label == "Wallonia":
        plt.annotate(label, (x + r * 0.75 , y- r*0.55), va='top', ha='right', color="black",
                     bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.2), fontsize=14)
    else:
        plt.annotate(label, (x, y), va='bottom', ha='center', color="black",
                     bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.2), fontsize=14)

    #plt.annotate(label, (x, y), va='bottom', ha='center', color="black",
                 #bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.2))

for circle in circles:
    if circle.level != 4:
        continue
    x, y, r = circle
    ax.add_patch(plt.Circle((x, y), r, alpha=1, linewidth=0, color=print_corresponding_color(circle.ex['id'])))

for circle in circles:
    if circle.level != 4:
        continue
    x, y, r = circle
    label = circle.ex["id"]
    if label == "Walloon Brabant":
        label_color = "white"  # Set label text color to white for "Walloon Brabant"
    else:
        label_color = "black"
    plt.annotate(label, (x, y), va=label_position(circle.ex['id']), ha='center', color= label_color)

list = pro_capite_get_values()
cmap = plt.get_cmap('Greens')
norm = plt.Normalize(min(list), max(list))
colors = cmap(norm(list))

list_red = pro_capite_region_get_values()
red_cmap = plt.get_cmap('Reds')
red_norm = plt.Normalize(min(list_red), max(list_red))
red_colors = red_cmap(norm(list_red))


print("Green Colors:", colors.tolist())
print("Red Colors:", red_colors.tolist())
#print(colors.tolist())

# Adding a colorbar to the plot
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
cbar.set_label('Patients for each doctor (Provinces)')
custom_ticks = [min(list), mean(list), max(list)]  # Add your custom tick values here
custom_labels = ["794 (Hainaut)", "712 (Belgian average)", "512 (Walloon Brabant)"]  # Add your custom tick labels here
cbar.set_ticks(custom_ticks)
cbar.set_ticklabels(custom_labels)


cbar_red = plt.colorbar(plt.cm.ScalarMappable(norm=red_norm, cmap=red_cmap), ax=ax, location='bottom', pad=0.15)
cbar_red.set_label('Patients for each doctor (Regions)')
min_val_red = min(list_red)
max_val_red = max(list_red)

# Set ticks and labels on the color bar
cbar_red_ticks = [ min_val_red, mean(list_red), max_val_red]
cbar_red_ticklabels = [f"{int(min_val_red)} (Wallonia)", "712 (Belgian average)", f"{int(max_val_red)} (Brussels)"]
cbar_red.set_ticks(cbar_red_ticks)
cbar_red.set_ticklabels(cbar_red_ticklabels)


#custom_ticks_red = [min(list_red), mean(list_red), max(list_red)]
#custom_labels_red = ["794 (Hainaut)", "712 (Belgian average)", "512 (Walloon Brabant)"]
#cbar_red.set_ticks(custom_ticks_red)
#cbar_red.set_ticklabels(custom_labels_red)

plt.figtext(0.45, 0.05, "Data from 2018 (https://overlegorganen.gezondheid.belgie.be/nl/documenten/hwf-statan-2018-detailstatistieken)", wrap=True, horizontalalignment='center', fontsize=9)
plt.show()
print(min(list_red))
