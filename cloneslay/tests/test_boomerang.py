from cloneslay.actor import Actor
from cloneslay.cards.sword_boomerang import Sword_boomerang
from cloneslay.cards.defense import Defense

def test_strike():
    my_defense = Defense()
    batmerang = Sword_boomerang()
    actor1 = Actor([batmerang, my_defense])
    actor2 = Actor([])
    batmerang.activate(actor1, actor2)
    assert actor2.live_points == 41
    my_defense.activate(actor2)
    assert actor2.block_points == 5
    batmerang.activate(actor1, actor2)
    assert actor2.block_points == 0
    assert actor2.live_points == 37