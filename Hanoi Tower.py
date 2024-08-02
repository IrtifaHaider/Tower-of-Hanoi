NUMBER_OF_DISKS = int(input("Enter the number of disks: "))
A = list(range(NUMBER_OF_DISKS, 0, -1))  # Source rod
B = []  # Auxiliary rod
C = []  # Target rod

# Initialize a global move counter
move_counter = 0

def move(n, source, auxiliary, target, source_name, auxiliary_name, target_name):
    global move_counter
    if n <= 0:
        return
    
    # Move n - 1 disks from source to auxiliary, using target as auxiliary
    move(n - 1, source, target, auxiliary, source_name, target_name, auxiliary_name)
    
    # Move the nth disk from source to target
    disk = source.pop()
    target.append(disk)
    
    # Increment the move counter
    move_counter += 1
    
    # Display the move details
    print(f'Moving disk {disk} from {source_name} to {target_name}')
    print(f'A: {A}\nB: {B}\nC: {C}\n')
    
    # Move the n - 1 disks from auxiliary to target, using source as auxiliary
    move(n - 1, auxiliary, source, target, auxiliary_name, source_name, target_name)

def main():
    print('Source Rod: A')
    print('Target Rod: C\n')
    # Initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, A, B, C, 'A', 'B', 'C')
    # Print the total number of moves
    print(f'Total moves: {move_counter}')

main()
