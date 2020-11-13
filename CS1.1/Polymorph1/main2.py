class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class seagull(Bird):
    def flight(self):
        print("seagulles fly over water.")


obj_bird = Bird()
obj_spr = sparrow()
obj_seagul = seagull()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_seagul.intro()
obj_seagul.flight()
