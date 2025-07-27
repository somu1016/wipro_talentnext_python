def analyze_purchase(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        total_items = 0
        free_items = 0
        total_amount = 0.0
        discount = 0.0
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            
            if line.lower().startswith('discount'):
                try:
                    discount = float(line.split()[1])
                except (IndexError, ValueError):
                    continue
                continue
            
            
            try:
                
                last_space = line.rfind(' ')
                if last_space == -1:
                    continue
                
                item = line[:last_space].strip()
                price_str = line[last_space+1:].strip()
                
                
                if price_str.lower() == 'free':
                    price = 0
                else:
                    price = float(price_str)
                
                total_items += 1
                if price == 0 or 'free' in item.lower():
                    free_items += 1
                    price = 0  # Treat as free item
                total_amount += price
            except ValueError:
                continue
        
        final_amount = max(0, total_amount - discount)
        
        print(f"No of items purchased: {total_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount:.0f}")
        print(f"Discount given: {discount:.0f}")
        print(f"Final amount paid: {final_amount:.0f}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

filename = input("Enter the file name: ").strip()
if not filename.endswith('.txt'):
    filename += '.txt'
analyze_purchase(filename)