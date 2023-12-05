def answer1():
    possible_games = []
    #cubes = {'red': 0, 'green': 0, 'blue': 0}
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}

    with open ("day2/input.txt") as input:
        #https://stackoverflow.com/questions/17569679/python-attributeerror-io-textiowrapper-object-has-no-attribute-split
        games_separated = [lines.rstrip('\n') for lines in input]
        
        #ngl from this part onwards, i did use chatgpt for ideas and for more explanation
        for game in games_separated:
            game_id, game_info = game.split(':') 
            game_id = int(game_id.split()[1])

            subsets = game_info.split(';')
            is_possible = True

            for subset in subsets: 
                subset_cubes = subset.strip().split(',')
                cube_count = {cube.split()[1]: int(cube.split()[0]) for cube in subset_cubes}

                for colour, count in cube_count.items():
                    if max_cubes.get(colour, 0) < count:
                        is_possible = False
                        break

                if not is_possible: 
                    break

            if is_possible:
                possible_games.append(game_id)
    
     
        print(f' Possible Games: {possible_games}')
        print(f' Sum of Game IDs: {sum(possible_games)}')

answer1()


    


   