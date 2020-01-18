"""Constants for application"""
LIVES = 3

ROBBER = 1
WARRIOR = 2
WIZARD = 3

ATTACK = {
    ROBBER: WIZARD,
    WARRIOR: ROBBER,
    WIZARD: WARRIOR
}
