class MoveCharacter:
    def move_fwd(self):
        print("Move forward 1 step")

    def move_bwd(self):
        print("Move backward 1 step")


class JumpCharacter:
    def jump_1level(self):
        print("Jump character 1 level")

    def jump_2level(self):
        print("jump character 2 level")


class Pokemon(MoveCharacter, JumpCharacter):
    pass


p = Pokemon()
p.move_bwd()
p.jump_1level()
print(Pokemon.mro())
