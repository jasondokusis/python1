import random

#0 = άδειο κελί
#1 = μικρός δακτύλιος
#2 = μεσαίος δακτύλιος
#4 = μεγάλος δακτύλιος
#Επιτρέπονται οι προσθέσεις των παραπάνω, π.χ. : 7 σημαίνει ότι στο κελί υπάρχουν 1 + 2 + 4 άρα και οι τρεις δακτύλιοι

#Η τάξη που περιγράφει την κάθε θέση, στην οποία μπορούν να προστεθούν δακτύλιοι, δηλαδή το κάθε κελί του πίνακα 3x3
class cell:
    small = False
    medium = False
    large = False
    def __init__(self):
        pass
    def equal(self, obj):
        if(self.small == obj.small and self.medium == obj.medium and self.large == obj.large):
            return True
        return False
    def is_small(self):
        if(self.small == True and self.medium == False and self.large == False):
            return True
        return False
    def is_medium(self):
        if(self.medium == True and self.large == False):
            return True
        return False
    def is_large(self):
        if(self.large == True):
            return True
        return False
    def is_not_empty(self):
        if(self.small == True or self.medium == True or self.large == True):
            return True
        return False
    def print(self):
        print(boolean_to_int(self.large) * 4 + boolean_to_int(self.medium) * 2 + boolean_to_int(self.small), end=" ")

#Μετατροπή boolean σε int 
def boolean_to_int(val):
    if(val == True):
        return 1
    return 0

#Άδειος πίνακας (χωρίς καπάκια)
board = [[0, 0, 0], [0, 0, 0], [1, 2, 3]]

#Έλεγχος για το πότε το παιχνίδι πρέπει να τελειώσει και εμφάνιση στην οθόνη αντίστοιχου μηνύματος
def endcondition():
    for i in range(3):
        if ((board[i][0].is_small() and board[i][1].is_medium() and board[i][2].is_large()) or (board[i][0].is_large() and board[i][1].is_medium() and board[i][2].is_small())):
            print('horizontal increase/decrease in ' + str(i))
            return True
        if (board[i][0].equal(board[i][1]) and board[i][1].equal(board[i][2]) and board[i][0].is_not_empty()):
            print('horizontal equality in ' + str(i))
            return True
    for j in range(3):
        if ((board[0][j].is_small() and board[1][j].is_medium() and board[2][j].is_large()) or (board[0][j].is_large() and board[1][j].is_medium() and board[2][j].is_small())):
            print('vertical increase/decrease in ' + str(j))
            return True
        if (board[0][j].equal(board[1][j]) and board[1][j].equal(board[2][j]) and board[0][j].is_not_empty()):
            print('vertical equality in ' + str(j))
            return True
    if((board[0][0].is_small() and board[1][1].is_medium() and board[2][2].is_large()) or (board[0][0].is_large() and board[1][1].is_medium() and board[2][2].is_small())):
        print('diagonal increase/decrease from top left to bottom right')
        return True
    if(board[0][0].equal(board[1][1]) and board[1][1].equal(board[2][2]) and board[0][0].is_not_empty()):
        print('diagonal equality from top left to bottom right')
        return True
    if((board[2][0].is_small() and board[1][1].is_medium() and board[0][2].is_large()) or (board[2][0].is_large() and board[1][1].is_medium() and board[0][2].is_small())):
        print('diagonal increase/decrease from bottom left to top right')
        return True
    if(board[2][0].equal(board[1][1]) and board[1][1].equal(board[0][2]) and board[2][0].is_not_empty()):
        print('diagonal equality from bottom left to top right')
        return True
    #Αν δεν ισχύει τίποτα από τα παραπάνω, επίστρεψε false
    return False

#Σύνολο κινήσεων στα 100 παιχνίδια
Sum = 0

#Για κάθε παιχνίδι
for i in range(100):

    #Αρχικοποίηση των κελιών
    for i in range(3):
        for j in range(3):
            board[i][j] = cell()

    #Αρχικοποίηση των αριθμών δακτυλίων
    number_of_rings = {
        "small" : 9,
        "medium" : 9,
        "large" : 9
    }

    #Αν δεν είναι τώρα να τελειώσει
    while(not(endcondition())):
        #Πήγαινε σε τυχαία θέση
        pos_i = random.randint(0, 2)
        pos_j = random.randint(0, 2)

        #Διάλεξε τυχαίο δακτύλιο
        ringtype = random.randint(1, 3)

        #Αν μπορεί να μπει ο δακτύλιος, κάντο και αφαίρεσε ένα από τους δακτυλίους
        if(ringtype == 1 and board[pos_i][pos_j].small == False and number_of_rings["small"] > 0):
            Sum = Sum + 1
            board[pos_i][pos_j].small = True
            number_of_rings["small"] = number_of_rings["small"] - 1
        if(ringtype == 2 and board[pos_i][pos_j].medium == False and number_of_rings["medium"] > 0):
            Sum = Sum + 1
            board[pos_i][pos_j].medium = True
            number_of_rings["medium"] = number_of_rings["medium"] - 1
        if(ringtype == 3 and board[pos_i][pos_j].large == False and number_of_rings["large"] > 0):
            number_of_rings["large"] = number_of_rings["large"] - 1
            Sum = Sum + 1
            board[pos_i][pos_j].large = True

    #Στο τέλος του παιχνιδιού, γράψε την κατάσταση
    for i in range(3):
        for j in range(3):
            board[i][j].print()
        print('')

#Υπολογισμός μέσου αριθμού κινήσεων και εμφάνιση στην οθόνη
print('Average number of moves : ' + str(Sum / 100))