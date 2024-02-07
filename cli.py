import click
from manage_json import read_json, write_json

# this is like creating the cli
@click.group()
def cli():
  pass
  
#getting all users
@cli.command()
def users(): 
  data = read_json('users.json')
  for user in data:
    print(user)

# creating a new user
@cli.command()
@click.option('--name', required=True, help='name of the user')
@click.option('--age', required=True, help='age of the user', type=int)
@click.pass_context
def new(ctx, name, age):
  if name and age:
    data = read_json('users.json')
    new_id = len(data) + 1
    new_user = {
      'id': new_id,
      'name': name,
      'age': age
    }
    data.append(new_user)  # Assign the value of data.append(new_user) to new_data
    write_json(data)
    print(f'user {name} created succesfully')
  else:
    ctx.fail('name and age are required')

#finding a user by it's id
@cli.command()
@click.argument('id', type=int) #this is like an option with -- but without it, you just pass the value next to the command
def user(id): 
  data = read_json('users.json')
  user = next((x for x in data if x['id'] == id), None) # in data, if x['id'] is equal to id return that, else return None
  
  if user is None: print(f"user with id: {id} was not found")
  else: print(user)


@cli.command()
@click.argument('id', type=int)
@click.option('--name', help='name of the user')
@click.option('--age', help='age of the user', type=int)
@click.pass_context
def update(ctx, id, name, age):
  data = read_json('users.json')
  if not id or not name or not age:
    return print("""you're missing arguments: 
          cli.py update <id> --name <new_name> --age <new_age>""")
  if id not in [user['id'] for user in data]:
    ctx.fail(f'user with id: {id} was not found')
  for user in data:
    if user['id'] == id:
      user['name'] = name
      user['age'] = age
      break
  write_json(data)
  print(f'user with id: {id} was updated successfully')



#deleting a user by it's id
@cli.command()
@click.argument('id', type=int) #this is like an option with -- but without it, you just pass the value next to the command
def delete(id): 
  data = read_json('users.json')
  user = next((x for x in data if x['id'] == id), None) # in data, if x['id'] is equal to id return that, else return None
  
  if user is None: print(f"user with id: {id} was not found")
  else: 
    data.remove(user) #removing the user from the file
    write_json(data, file='users.json')
  
if __name__ == '__main__':
  cli()
  
