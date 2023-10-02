import circlify
import matplotlib.pyplot as plt

data = [{'id': 'World', 'datum': 16263, 'children': [
    {'id': "Belgium", 'datum': 16263,
     'children': [
         {'id': "Flanders", 'datum': 9204, 'children': [
                {'id': "Antwerp", 'datum': 2387},
                {'id': "East Flanders", 'datum': 2104},
                {'id': "West Flanders", 'datum': 1661},
                {'id': "Limburg", 'datum': 1177},
                {'id': "Vlaams Brabant", 'datum': 1875}
         ]},
         {'id': "Wallonia", 'datum': 5460},
         {'id': "Brussels", 'datum': 1599}
     ]}
]}]

# Compute circle positions thanks to the circlify() function
circles = circlify.circlify(
    data,
    show_enclosure=False,
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)



# Create just a figure and only one subplot
fig, ax = plt.subplots(figsize=(14, 14))

# Title
ax.set_title('Repartition of Belgium population')

# Remove axes
ax.axis('off')

# Find axis boundaries
lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

# Print circle the highest level (continents):
for circle in circles:
    if circle.level != 2:
        continue
    x, y, r = circle
    ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="lightblue"))

# Print labels for the continents
for circle in circles:
    if circle.level != 2:
        continue
    x, y, r = circle
    label = circle.ex["id"]


# Print circle and labels for the highest level:
for circle in circles:
    if circle.level != 3:
        continue
    x, y, r = circle
    label = circle.ex["id"]
    ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="#69b3a2"))
    plt.annotate(label, (x, y), ha='center', color="white")


for circle in circles:
    if circle.level != 4:
        continue
    x, y, r = circle
    ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, color="lightblue"))


for circle in circles:
    if circle.level != 4:
        continue
    x, y, r = circle
    label = circle.ex["id"]
    plt.annotate(label, (x, y), va='center', ha='center')

plt.show()