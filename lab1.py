import csv

def read_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def write_csv(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'view'])
        writer.writeheader()
        if data:  
            writer.writerows(data)
        else:
            print(f"Warning: No data to write to {file_name}")

def handle_votes(votes, blocks, chain):
    print("Votes received:", votes)
    
    for vote in votes:
        block_id = vote['block_id']
        block_to_add = None
        
        for block in blocks:  
            if block['id'] == block_id:
                block_to_add = block
                break
        
        if block_to_add:
            last_block = chain[-1] if chain else None
            if last_block and int(block_to_add['view']) == int(last_block['view']) + 1:
                chain.append(block_to_add)
                print(f"Block {block_to_add['id']} added to the chain.")
            elif not last_block: 
                chain.append(block_to_add)
                print(f"Block {block_to_add['id']} added as first block in the chain.")
        else:
            print(f"Block with id {block_id} not found.")

def create_chain(blocks, votes):
    chain = []
    
    for block in blocks:
        block['view'] = int(block['view'])  
        if block['view'] == 0:
            chain.append(block)
            break
    
    print(f"Initial chain with view 0: {chain}")  
    
    handle_votes(votes, blocks, chain)

    return chain

if __name__ == '__main__':
    blocks = read_csv('block.csv') 
    votes = read_csv('blok_id.csv')  

    print("Data from blocks.csv:", blocks)
    print("Data from votes.csv:", votes)

    chain = create_chain(blocks, votes)

    print(f"Final chain: {chain}")


    write_csv('output_chain.csv', chain)

    print("csv файли створено :)")