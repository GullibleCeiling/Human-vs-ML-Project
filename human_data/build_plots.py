import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from protect.data.fetch_data import get_penguins_data

def make_plot(category1, category2):

    category1_label = category1.replace("_", " ").title()
    category2_label = category2.replace("_", " ").title()


    df, target_name = get_penguins_data()
    

    df = df.dropna(subset=[category1, category2, target_name])

    plot_dir = "./getting_started/plots"
    os.makedirs(plot_dir, exist_ok=True)


    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=df,   
        x=category1,
        y=category2,
        hue=target_name,
        style=target_name,
        s=30
    )
    
    plt.title(f"{category2_label} vs {category1_label}", fontsize=14)
    plt.xlabel(category1_label)
    plt.ylabel(category2_label)
    plt.legend(title=target_name.replace("_", " ").title())
    plt.grid(True, linestyle='--', alpha=0.6)


    file_name = f"{category1}_vs_{category2}.png"
    save_path = os.path.join(plot_dir, file_name)
    
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"Successfully saved plot to: {save_path}")

make_plot('culmen_depth_mm', 'flipper_length_mm')
make_plot('culmen_length_mm', 'body_mass_g')
make_plot('culmen_depth_mm', 'body_mass_g')
