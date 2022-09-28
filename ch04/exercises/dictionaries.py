article = "Soccer has Fluid Play: Playing sports of any kind requires an eye for details so you can make the most out of every situation. That is one reason why soccer is one of the best sports in the world. The fluidity of the game means that there will be little or no occasional stops and distractions during the gameplay. Instead, both the clock/timing and the ball are in motion at all times. If for any reason the ball goes out of play, it will be put right back to play the next minute. Less Exposure to Injuries: Unlike football where injuries are sustainable, soccer doesn’t overly expose the players to injuries. The less likelihood of getting injured during a soccer game is because of the extra care taken during the team formation. When the injury rate is low, you can rest assured that more athletes will have a longer, healthier career." 


changes = {
  "soccer":"kickball",
  "Soccer":"Kickball",
  "ball":"puck",
  "players":"cool guys",
  "Players":"Cool Guys"
}

for key,value in changes.items():
  article = article.replace(key, value)

print(article)