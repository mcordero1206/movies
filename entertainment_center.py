import media
import fresh_tomatoes
"""
The 6 movies to be displayed on my page 
in list form.
"""
scott_pilgrim = media.Movie("Scott Pilgrim vs. The World", ">As bass guitarist \
for a garage-rock band, Scott Pilgrim (Michael Cera) has never had trouble getting a girlfriend; \
usually, the problem is getting rid of them. But when Ramona Flowers (Mary Elizabeth Winstead) \
skates into his heart, he finds she has the most troublesome baggage of all: an army of ex-boyfriends \
who will stop at nothing to eliminate him from her list of suitors.", "images/scott.jpg", "https://youtu.be/7wd5KEaOtm4", 112)

the_matrix = media.Movie("The Matrix", "Neo (Keanu Reeves) believes that Morpheus (Laurence Fishburne), \
an elusive figure considered to be the most dangerous man alive, can answer his question -- What is the \
Matrix? Neo is contacted by Trinity (Carrie-Anne Moss), a beautiful stranger who leads him into an underworld \
where he meets Morpheus. They fight a brutal battle for their lives against a cadre of viciously intelligent secret \
agents. It is a truth that could cost Neo something more precious than his life.", "images/matrix.jpg", "https://youtu.be/m8e-FF8MsqU", 150)

life_of_pi = media.Movie("Life of Pi", "After deciding to sell their zoo in India and move to Canada, Santosh and Gita Patel \
board a freighter with their sons and a few remaining animals. Tragedy strikes when a terrible storm sinks the ship, leaving the \
Patels' teenage son, Pi (Suraj Sharma), as the only human survivor. However, Pi is not alone; a fearsome Bengal tiger has also found \
refuge aboard the lifeboat. As days turn into weeks and weeks drag into months, Pi and the tiger must learn to trust each other if both \
are to survive.", "images/pi.jpg", "https://youtu.be/mZEZ35Fhvuc", 127)

inception = media.Movie("Inception", "Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people's dreams and steal \
their secrets from their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him \
everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in someone's mind. If \
he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobb's every move.", "images/inception.jpg", "https://youtu.be/66TuSJo4dZM", 140)

ip_man = media.Movie("Ip Man", "Dramatizes the life of Yip Man (Donnie Yen) in the mid to late 1930s. Foshun is a prosperous city with many \
martial arts schools. Yip, who practices Wing Chun, is the local master. When a rough gang comes to town, it's Yip they must challenge. Then, \
Japan invades China. Yip and his family live in poverty, with Yip taking any work for food. General Miura, now in charge, stages martial arts \
fights between Chinese and his men: winners get extra rice. When the general's attaché murders a colleague of Yip's, Yip must step forward. At \
the same time, the ruffians return to town, this time threatening a local cotton mill. Can Yip protect the mill and also face Miura and certain \
death?", "images/ip.jpg", "https://youtu.be/1AJxXQ7xojE", 106)

interstellar = media.Movie("Interstellar", "In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. \
Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a \
wormhole. But first, Brand must send former NASA pilot Cooper (Matthew McConaughey) and a team of researchers through the wormhole and across the galaxy \
to find out which of three planets could be mankind's new home.", "images/interstellar.jpg", "https://youtu.be/Lm8p5rlrSkY", 169)
# The list of titles for the movie instances.
movies = [scott_pilgrim, the_matrix, life_of_pi, inception, ip_man, interstellar]

# This string uses the list of movie instances as input to generate an HTML file and open it in the browser.
fresh_tomatoes.open_movies_page(movies)