import matplotlib.pyplot as plt

pro_capite_doctors_regions = {
    "Flanders": (1886609+1543865+ 1209011+ 885951+ 1173440)/9204,
    'Wallonia': (409782+1351127+ 499454+ 1110989+ 291143)/5460,
    "Brussels":  1222637/1599
}

colors = [
    (0.9437139561707035, 0.25667051134179164, 0.18869665513264128, 1.0),    # Red
    (1.0, 0.9607843137254902, 0.9411764705882353, 1.0),
    (0.403921568627451, 0.0, 0.05098039215686274, 1.0)]

def pro_capite_region_get_values():
    sorted_pro_capite_dict_regions = dict(sorted(pro_capite_doctors_regions.items(), key=lambda item: item[1]))
    values = list(sorted_pro_capite_dict_regions.values())
    return values

colors_dict = {}

for key in pro_capite_doctors_regions:
    colors_dict[key] = colors.pop(0)
