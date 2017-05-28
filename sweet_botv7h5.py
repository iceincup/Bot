import discord
import asyncio
import json



client = discord.Client()
members_dic = {}


filename = 'members_dic.json'
with open(filename) as f_obj:
    members_dic = json.load(f_obj)

administrators = ["181942382583873538", "188004756059455492", "181704150734602240",] 

king = ["181704150734602240", ]


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.event
async def on_member_update(before, after):
    if before.id in king and before.is_afk == True and after.is_afk == False:
        await client.send_message(before.server, 'Long Live King Usifan!')



@client.event
@asyncio.coroutine
async def on_message(message):
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Pong!')

    if message.content.startswith('!scoreboard'):
        # Prints the top 10 scores
        scoreboard = [(points, members_dic[points]) for points in sorted(members_dic, key=members_dic.get, reverse=True)][:10]
        await client.send_message(message.channel, "These are the Top 10 scores:")
        for points, v in scoreboard:
            await client.send_message(message.channel, str(points) + " has " + str(v) + " points!")
            

    if message.content.startswith('!fullscoreboard'):
        #Prints the full scoreboard in a Private Message
        scoreboard = [(points, members_dic[points]) for points in sorted(members_dic, key=members_dic.get, reverse=True)]
        await client.send_message(message.author, "Here is the full scoreboard:")
        for points, v in scoreboard:
            await client.send_message(message.author, str(points) + " has " + str(v) + " points!")
        


    if message.content.startswith('!help'):
        help_msg = "Type '!register' to register yourself\nType '!myscore' to view your score "
        help_msg += "\nType '!scoreboard' to view the Top 10 scores!"
        help_msg += "\nType '!info' for information about the Crown Favour Points!"
        help_msg += "\nType '!fullscoreboard' to get the full scoreboard!"
        await client.send_message(message.channel, help_msg)

    if message.content.startswith('!info'):
        # Prints the infomation
        info_msg = "In an effort to increase the population of the Kingdom, his Majesty the King is announcing the “Crown Recruitment Initiative”.\nFor every 1 person recruited to the Kingdom, 1 point (called a Crown Favour) will be awarded. Crown Favour will then be exchangeable for real world prizes funded by our Majesty the King, Usifan. Prizes will include games on steam, IP points for CoE, among others."
        await client.send_message(message.channel, info_msg)
        

    if message.content.startswith('!perfect'):
        # For fun :)
        perfect_msg = "You're perfect!"
        perfect_msg += "\nYou're beautiful!"
        perfect_msg += "\nYou look like Linda Evangelista!"
        perfect_msg += "\nYou're a model!"
        
        await client.send_message(message.channel, perfect_msg)
    

    if message.content.startswith('!register'):
        # Registers a user

        name = message.author.display_name

        

        if name in members_dic:
            # Checks if a user is already registered
            await client.send_message(message.channel, "Sorry, you are already registered")
        else:
            
            members_dic[name] = 0
            filename = 'members_dic.json'
            with open(filename, 'w') as f_obj:
                json.dump(members_dic, f_obj)
            await client.send_message(message.channel, 'Thank you ' + str(message.author) + ", you are now registered!")
            await client.send_message(message.channel, 'You start off with ' + str(members_dic[name]) + " points!")

    if message.content.startswith('!myscore'):
        # Prints the score of the user that calls the function
        
        name = message.author.display_name
        myscoremessage = str(message.author) + ", you have: " + str(members_dic[name]) + " points!"
        await client.send_message(message.channel, myscoremessage)   

   
    if message.content.startswith('!addpoints'):
        # Function to add points - There is a BUG here
        if message.author.id in administrators:
            

            await client.send_message(message.channel, "Welcome admin! To add points, enter !name namehere and !amount of points")
        
            def check(msg):
                return msg.content.startswith('!name')

            message = await client.wait_for_message(author=message.author, check=check)
            name = message.content[len('!name'):].strip()
        

            def check(msg):
                return msg.content.startswith('!points')

            message = await client.wait_for_message(author=message.author, check=check)
            points = message.content[len('!points'):].strip()


            members_dic[name] += int(points)

            filename = 'members_dic.json'
            with open(filename, 'w') as f_obj:
                json.dump(members_dic, f_obj)


            scoremessage = name + " now has: " + str(members_dic[name]) + " points!"
            await client.send_message(message.channel, scoremessage)

        else:

            await client.send_message(message.channel, "Sorry, you don't have permission to add points.")

    

     


        



client.run('MzE2MjkxNDIxMzc0MjUxMDI5.DAeFlQ.u0h-HTVxp97FkM9sDptvpze7TM0')

            


            

 

            

        
        
        
        

