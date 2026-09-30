from cards import Deck, hand_value


class Blackjack:
    def __init__(self):
        self.chips = 100

    def show(self, player, dealer, hide=True):
        shown_dealer = ["??"] if hide else [f"{r}{s}" for r, s in dealer]
        if(hide==False):
            print("Dealer:", " ".join(shown_dealer), "=", hand_value(dealer))
        else:
            print("Dealer:", " ".join(shown_dealer))
        print("Player:", " ".join(f"{r}{s}" for r, s in player),
              "=", hand_value(player))

    def round(self,wager):
        deck = Deck()
        player = [deck.draw(), deck.draw()]
        dealer = [deck.draw(), deck.draw()]
        self.show(player, dealer)

        while hand_value(dealer) < 17:
            dealer.append(deck.draw())

        while hand_value(player) < 21:
            key = input("[h]it [s]tand [q]uit: ").strip().lower()
            if key == "q":
                return False
            if key == "s":
                break
            if key == "h":
                player.append(deck.draw())
                if hand_value(player) == 21:
                    self.show(player, dealer, hide=False)
                    if hand_value(dealer) == 21:
                        print("Push.")
                        return True
                    else:
                        print("Player Wins.")
                        self.chips +=wager
                        return True
                    
                elif hand_value(player) > 21:
                    self.show(player, dealer, hide=False)
                    if hand_value(player) > hand_value(dealer):
                        print("Bust.")
                        self.chips -= wager
                        return True
                    elif hand_value(player) == hand_value(dealer):
                        print("Push.")
                        return True
                    else:
                        print("Player Wins.")
                        self.chips += wager
                        return True
                else:
                    self.show(player, dealer)
                        

        self.show(player, dealer, hide=False)
        pv, dv = hand_value(player), hand_value(dealer)
        if dv > 21 or pv > dv:
            self.chips += wager
            print("Player wins.")
        elif pv < dv:
            self.chips -= wager
            print("Dealer wins.")
        else:
            print("Push.")
        return True

    def run(self):
        print("Blackjack — starting chips:", self.chips)
        while self.chips > 0:
            print("Chips Left: ",self.chips)
            wager= int(input("Enter wager: "))
            if(wager>self.chips):
                print("Please wager at most what you own. No loans")
                continue
            elif(wager<=0):
                print("Wager a positive amount")
                continue
            elif not self.round(wager):
                print("Chips Left = ",self.chips)
                return
            if self.chips==0:
                print("No more chips left")
                return
            if input("Play again? [y/n]: ").strip().lower() != "y":
                print("Chips Left = ",self.chips)
                return
