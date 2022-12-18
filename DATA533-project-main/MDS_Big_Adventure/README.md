# MDS BIG ADVENTURE DESCRIPTIONS

### character
| FUNCTION NAME | DESCRIPTIONS |
| ------ | ------ |
|display()| display current power and health|
|fight()| return the power value|
|wound(damage)|deduct health by the alien attack|
### alien
| FUNCTION NAME | DESCRIPTIONS |
| ------ | ------ |
|getName()| return alien name|
|setName()| set alien name|
|die()|change alien attributes when alien is dead|
|isdead()|check if the alien is dead|
|display()|display |
|dropMoney()|when alien is dead, drop the money|
### player
| FUNCTION NAME | DESCRIPTIONS |
| ------ | ------ |
|advance()| advance one position if player does not reach to final position|
|retreat()| retreat one position if player does not reach to tim horton|
|locate()|return current position |
|buy()|if at tim horton return current money|
|defeat()|print the lines when player is defeated |
|display()|display health, power and money according to player's identity |
|showMoney()|return current money value|
|pay(price)|deduct money when buying items in tim horton|
|transform()|upgrade player identity to Ultraman when player gets spark lance|
|isdefeated()|check if player is dead|
|getidentity()|return player's identity|
|getMoney(money)|get the money from the dead alien|
### item
| FUNCTION NAME | DESCRIPTIONS |
| ------ | ------ |
|gethp()| return health bonus of the item|
|getpo()| return power bonus of the item|
|getprice()|return item price |
|getname()|return the item name|
|getamount()|return item amount|
|display()|display item name and price|
|setamount(value)|set item amount|
|addhealth(player)|add health to the player|
|addpower(player)|add power to the player |
### sparkLance
| FUNCTION NAME | DESCRIPTIONS |
| ------ | ------ |
|getplot()|get the plot when sparklance is activated|
|check()|add status|
|getstatus()|return status|
|betaTransform(player)| multiply the health value to the player|
|getSpacium(player)| multiply the power value to the player|
### level
| FUNCTION NAME | DESCRIPTIONS |
| ------ | ------ |
|getLoc()| return location |
|visit()| set status to 1 if the level is visited|
|getstatus()|return status|
|isVisited()|check if current level is visited|
|getAlien()|return alien at the current level|
|getplot()|return the lines based on level status|
|unlock()|unlock the level if alien is dead|
|islocked()|check if the level is locked|
### timHortons
| FUNCTION NAME | DESCRIPTIONS |
| ------ | ------ |
|sell(item)| update item amount when the item is sold  |
|checkStock(name)| check item stock|
|getInv()|return inventory|

### play
| FUNCTION NAME | DESCRIPTIONS |
| ------ | ------ |
|buyItem()| buy items at tim horton, display items at tim horton, ask player for what to order,update player's health, power and money|
|fight()|utilize random method to get random advantages for both player and allien calculate the fight result; output scripture and fighting result depends on player's identity and calculated power; unlock the level, and get the moeny when alien at that level is dead|
|win()|if player arrive at 4 location and alien's power at 4 location is 0, then player win the game|
|advance()|advance one level up when the level is unlocked, display the alien and set the location status visited; report error when the level us locked|
|play| display the scripture and ask the player for 5 options of next steps; option 1: advance; option 2: retreat; option 3: buy item at tim horton; option 4: fight against alien; option 0: exit the game|
