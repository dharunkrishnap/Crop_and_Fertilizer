import pandas as pd

# Dataset with soil types, crops, and fertilizers
data = {
    'soil': ['clay', 'sandy', 'loamy', 'peaty', 'saline', 'clay', 'loamy', 'sandy', 'peaty', 'saline'],
    'crop': ['rice', 'maize', 'wheat', 'barley', 'cotton', 'sugarcane', 'soybean', 'sorghum', 'millet', 'groundnut'],
    'fertilizer': ['Urea', 'DAP', 'MOP', 'Ammonium Nitrate', 'NPK', 'Nitrogenous Fertilizer', 'Rhizobium', 'Superphosphate', 'Potash', 'Calcium Ammonium Nitrate']
}

df = pd.DataFrame(data)

def recommend_crops_and_fertilizers(soil_type):
    filtered = df[df['soil'] == soil_type.lower()]
    if filtered.empty:
        return f"No recommendations available for soil type '{soil_type}'."
    
    recommendations = []
    for _, row in filtered.iterrows():
        recommendations.append((row['crop'], row['fertilizer']))
    return recommendations

# Input soil type
soil = input("Enter soil type (e.g., clay, sandy, loamy, peaty, saline): ")

# Get recommendations
result = recommend_crops_and_fertilizers(soil)

# Print results
if isinstance(result, str):
    print(result)
else:
    print(f"\nRecommended crops and fertilizers for soil type '{soil}':")
    for crop, fertilizer in result:
        print(f"- Crop: {crop.capitalize()}, Fertilizer: {fertilizer}")

