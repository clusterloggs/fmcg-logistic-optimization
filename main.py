import pandas as pd

fmcg_data = pd.DataFrame({
    "sku": [
        "Indomie Noodles Carton",
        "Peak Milk Tin Pack",
        "Golden Penny Spaghetti",
        "Coca-Cola PET 50cl",
        "Milo Refill Pack",
        "Dangote Sugar 1kg",
        "Power Oil 3L",
        "Trophy Lager Carton",
        "Eva Water Pack"
    ],
    "profit_naira": [
        52000, 48000, 41000, 60000, 55000, 45000, 50000, 62000, 30000
    ],
    "volume_units": [
        3.5, 2.8, 2.2, 4.0, 3.0, 2.5, 3.8, 4.5, 1.8
    ]
})



## FMCG Item Class
class FMCGItem:
    def __init__(self, sku, profit, volume):
        self.sku = sku
        self.profit = profit
        self.volume = volume

    def getValue(self):
        return self.profit

    def getCost(self):
        return self.volume

    def density(self):
        return self.profit / self.volume

    def __str__(self):
        return f"{self.sku}: <profit=₦{self.profit}, volume={self.volume}>"


## Build SKU List
def build_inventory(df):
    items = []
    for _, row in df.iterrows():
        items.append(FMCGItem(
            row['sku'],
            row['profit_naira'],
            row['volume_units']
        ))
    return items

items = build_inventory(fmcg_data)



## Greedy Optimization Function
def greedy_allocate(items, max_volume, key_function):
    sorted_items = sorted(items, key=key_function, reverse=True)

    selected = []
    used_volume = 0
    total_profit = 0

    for item in sorted_items:
        if used_volume + item.getCost() <= max_volume:
            selected.append(item)
            used_volume += item.getCost()
            total_profit += item.getValue()

    return selected, total_profit, used_volume


## Run Optimization Scenarios

TRUCK_CAPACITY = 15  # volume units

# Strategy 1: Greedy by Profit
by_profit = greedy_allocate(items, TRUCK_CAPACITY, FMCGItem.getValue)

# Strategy 2: Greedy by Lowest Volume
by_volume = greedy_allocate(items, TRUCK_CAPACITY, lambda x: 1/x.getCost())

# Strategy 3: Greedy by Profit Density
by_density = greedy_allocate(items, TRUCK_CAPACITY, FMCGItem.density)

if __name__ == "__main__":
    print("=== FMCG Truck Loading Optimization ===\n")

    print("Strategy 1: Greedy by Profit")
    for item in by_profit[0]:
        print(f"  - {item}")
    print(f"Total Profit: ₦{by_profit[1]}, Total Volume: {by_profit[2]} units\n")

    print("Strategy 2: Greedy by Lowest Volume")
    for item in by_volume[0]:
        print(f"  - {item}")
    print(f"Total Profit: ₦{by_volume[1]}, Total Volume: {by_volume[2]} units\n")

    print("Strategy 3: Greedy by Profit Density")
    for item in by_density[0]:
        print(f"  - {item}")
    print(f"Total Profit: ₦{by_density[1]}, Total Volume: {by_density[2]} units\n")