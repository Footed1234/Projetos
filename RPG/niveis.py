def up_nivel(xp, nivel, atk, max_hp, max_xp, crit, crit_dano, i_xp):
    xp += i_xp
    while xp >= max_xp:
        nivel += 1
        atk += 1
        max_hp += 5
        max_xp = int(max_xp * 1.3)
        if (crit_dano + 0.5) < 20:
            crit_dano += 0.5
        elif (crit_dano + 0.5) >= 20:
            crit_dano = 20
        if int(crit * 1.04) < 30:
            crit = int(crit * 1.04)
        elif int(crit * 1.04) >= 30:
            crit = 30
        xp -= max_xp
    return xp, nivel, atk, max_hp, max_xp, crit, crit_dano