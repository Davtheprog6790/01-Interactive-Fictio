import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "36FFCEE8-26C3-4EC1-802F-C11EA68F5F64",
  "name": "Wolf man",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631412461555,
  "passages": [
    {
      "name": "Running Woman",
      "tags": "",
      "id": "1",
      "text": "Long ago, A Mother is running from a group of Death Tones in Forest with her new born baby. You are the mother. \n\n[[DIE->Just Stand there]]\n[[FIGHT->Stand and Fight ]]\n[[CRY->Cry for Help while running]]\n[[TURN LEFT->Turn Left]]\n[[HIDE->Hide under a tree]]",
      "links": [
        {
          "linkText": "DIE",
          "passageName": "Just Stand there",
          "original": "[[DIE->Just Stand there]]"
        },
        {
          "linkText": "FIGHT",
          "passageName": "Stand and Fight",
          "original": "[[FIGHT->Stand and Fight ]]"
        },
        {
          "linkText": "CRY",
          "passageName": "Cry for Help while running",
          "original": "[[CRY->Cry for Help while running]]"
        },
        {
          "linkText": "TURN LEFT",
          "passageName": "Turn Left",
          "original": "[[TURN LEFT->Turn Left]]"
        },
        {
          "linkText": "HIDE",
          "passageName": "Hide under a tree",
          "original": "[[HIDE->Hide under a tree]]"
        }
      ],
      "hooks": [],
      "cleanText": "Long ago, A Mother is running from a group of Death Tones in Forest with her new born baby. You are the mother."
    },
    {
      "name": "Just Stand there",
      "tags": "",
      "id": "2",
      "text": "She stands there and gets torn to pieces and eaten by the Death Tones but the baby is left alone. You are now the baby. \n\n[[CRY->Cry like a baby]]\n[[CRAWL->Crawl away]]\n[[FIGHT->Fight]]\n[[CHAINSAW->Find a chainsaw]]\n[[PARKOUR->Parkour]]",
      "links": [
        {
          "linkText": "CRY",
          "passageName": "Cry like a baby",
          "original": "[[CRY->Cry like a baby]]"
        },
        {
          "linkText": "CRAWL",
          "passageName": "Crawl away",
          "original": "[[CRAWL->Crawl away]]"
        },
        {
          "linkText": "FIGHT",
          "passageName": "Fight",
          "original": "[[FIGHT->Fight]]"
        },
        {
          "linkText": "CHAINSAW",
          "passageName": "Find a chainsaw",
          "original": "[[CHAINSAW->Find a chainsaw]]"
        },
        {
          "linkText": "PARKOUR",
          "passageName": "Parkour",
          "original": "[[PARKOUR->Parkour]]"
        }
      ],
      "hooks": [],
      "cleanText": "She stands there and gets torn to pieces and eaten by the Death Tones but the baby is left alone. You are now the baby."
    },
    {
      "name": "Stand and Fight ",
      "tags": "",
      "id": "3",
      "score":20,
      "text": "She punches a death tone. The death tone falls in love and the other death tones drags her back to their cave. They leave the baby. You are the baby.\n\n[[CRY->Cry like a baby]]\n[[CRAWL->Crawl away]]\n[[GROW UP->Grow up in the forest]]\n[[SLEEP->Just sleep]]\n[[ANIMALS->Talk to animals]]",
      "links": [
        {
          "linkText": "CRY",
          "passageName": "Cry like a baby",
          "original": "[[CRY->Cry like a baby]]"
        },
        {
          "linkText": "CRAWL",
          "passageName": "Crawl away",
          "original": "[[CRAWL->Crawl away]]"
        },
        {
          "linkText": "GROW UP",
          "passageName": "Grow up in the forest",
          "original": "[[GROW UP->Grow up in the forest]]"
        },
        {
          "linkText": "SLEEP",
          "passageName": "Just sleep",
          "original": "[[SLEEP->Just sleep]]"
        },
        {
          "linkText": "ANIMALS",
          "passageName": "Talk to animals",
          "original": "[[ANIMALS->Talk to animals]]"
        }
      ],
      "hooks": [],
      "cleanText": "She punches a death tone. The death tone falls in love and the other death tones drags her back to their cave. They leave the baby. You are the baby."
    },
    {
      "name": "Turn Left",
      "tags": "",
      "id": "4",
      "score": 20,
      "text": "She jumps off a water fall into a river but gets shot mid air by the Death Tones because they have guns. The baby falls inside the river and floats to land. You are now the baby\n\n[[CRY->Cry like a baby]]\n[[CRAWL->Crawl away]]\n[[PUNCH->Punch the ground]]\n[[SLEEP->Just sleep]]\n[[ANIMALS->Talk to animals]]",
      "links": [
        {
          "linkText": "CRY",
          "passageName": "Cry like a baby",
          "original": "[[CRY->Cry like a baby]]"
        },
        {
          "linkText": "CRAWL",
          "passageName": "Crawl away",
          "original": "[[CRAWL->Crawl away]]"
        },
        {
          "linkText": "PUNCH",
          "passageName": "Punch the ground",
          "original": "[[PUNCH->Punch the ground]]"
        },
        {
          "linkText": "SLEEP",
          "passageName": "Just sleep",
          "original": "[[SLEEP->Just sleep]]"
        },
        {
          "linkText": "ANIMALS",
          "passageName": "Talk to animals",
          "original": "[[ANIMALS->Talk to animals]]"
        }
      ],
      "hooks": [],
      "cleanText": "She jumps off a water fall into a river but gets shot mid air by the Death Tones because they have guns. The baby falls inside the river and floats to land. You are now the baby"
    },
    {
      "name": "Cry for Help while running",
      "tags": "",
      "id": "5",
      "text": "She crys for help but to no avail. The Death Tones reach her and maul her to death, but they leave the baby alone. You are the baby",
      "links": [],
      "hooks": [],
      "cleanText": "She crys for help but to no avail. The Death Tones reach her and maul her to death, but they leave the baby alone. You are the baby"
    },
    {
      "name": "Cry like a baby",
      "tags": "",
      "id": "6",
      "text": "Baby cries and attracts animals to it. You are the animals.\n\n[[EAT->Eat Baby]]\n[[CARE->Take care of it]]",
      "links": [
        {
          "linkText": "EAT",
          "passageName": "Eat Baby",
          "original": "[[EAT->Eat Baby]]"
        },
        {
          "linkText": "CARE",
          "passageName": "Take care of it",
          "original": "[[CARE->Take care of it]]"
        }
      ],
      "hooks": [],
      "cleanText": "Baby cries and attracts animals to it. You are the animals."
    },
    {
      "name": "Crawl away",
      "tags": "",
      "id": "7",
      "text": "Baby crawls away and bumps into a tree. The tree turns around about to zap the baby. You are the tree\n\n[[OLDER->Tree zaps the baby and turns him into a teenager]]\n[[ERASE->Erases the baby from existence]]\n[[DRAG->Archer comes out of nowhere and drags the baby to safety]]\n[[SAVE->Archer comes out of nowhere and carries baby to safety]]\n[[POWERS->Baby gains the ability to fly to another kingdom]]",
      "links": [
        {
          "linkText": "OLDER",
          "passageName": "Tree zaps the baby and turns him into a teenager",
          "original": "[[OLDER->Tree zaps the baby and turns him into a teenager]]"
        },
        {
          "linkText": "ERASE",
          "passageName": "Erases the baby from existence",
          "original": "[[ERASE->Erases the baby from existence]]"
        },
        {
          "linkText": "DRAG",
          "passageName": "Archer comes out of nowhere and drags the baby to safety",
          "original": "[[DRAG->Archer comes out of nowhere and drags the baby to safety]]"
        },
        {
          "linkText": "SAVE",
          "passageName": "Archer comes out of nowhere and carries baby to safety",
          "original": "[[SAVE->Archer comes out of nowhere and carries baby to safety]]"
        },
        {
          "linkText": "POWERS",
          "passageName": "Baby gains the ability to fly to another kingdom",
          "original": "[[POWERS->Baby gains the ability to fly to another kingdom]]"
        }
      ],
      "hooks": [],
      "cleanText": "Baby crawls away and bumps into a tree. The tree turns around about to zap the baby. You are the tree"
    },
    {
      "name": "Just sleep",
      "tags": "",
      "id": "8",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Fight",
      "tags": "",
      "id": "9",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Find a chainsaw",
      "tags": "",
      "id": "10",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Parkour",
      "tags": "",
      "id": "11",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Talk to animals",
      "tags": "",
      "id": "12",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Hide under a tree",
      "tags": "",
      "id": "13",
      "text": "She hides under the tree but the death tones finds her and eats her. The baby is left alone. You are the baby.\n\n[[CRY->Cry like a baby]]\n[[CRAWL->Crawl away]]\n[[FIGHT->Fight]]\n[[SLEEP->Just sleep]]\n[[ANIMALS->Talk to animals]]",
      "links": [
        {
          "linkText": "CRY",
          "passageName": "Cry like a baby",
          "original": "[[CRY->Cry like a baby]]"
        },
        {
          "linkText": "CRAWL",
          "passageName": "Crawl away",
          "original": "[[CRAWL->Crawl away]]"
        },
        {
          "linkText": "FIGHT",
          "passageName": "Fight",
          "original": "[[FIGHT->Fight]]"
        },
        {
          "linkText": "SLEEP",
          "passageName": "Just sleep",
          "original": "[[SLEEP->Just sleep]]"
        },
        {
          "linkText": "ANIMALS",
          "passageName": "Talk to animals",
          "original": "[[ANIMALS->Talk to animals]]"
        }
      ],
      "hooks": [],
      "cleanText": "She hides under the tree but the death tones finds her and eats her. The baby is left alone. You are the baby."
    },
    {
      "name": "Grow up in the forest",
      "tags": "",
      "id": "14",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Punch the ground",
      "tags": "",
      "id": "15",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Eat Baby",
      "tags": "",
      "id": "16",
      "text": "Animals eats baby. THE END",
      "links": [],
      "hooks": [],
      "cleanText": "Animals eats baby. THE END"
    },
    {
      "name": "Take care of it",
      "tags": "",
      "id": "17",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Tree zaps the baby and turns him into a teenager",
      "tags": "",
      "id": "18",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Erases the baby from existence",
      "tags": "",
      "id": "19",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Archer comes out of nowhere and drags the baby to safety",
      "tags": "",
      "id": "20",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Archer comes out of nowhere and carries baby to safety",
      "tags": "",
      "id": "21",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Baby gains the ability to fly to another kingdom",
      "tags": "",
      "id": "22",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: " + str(moves) + ", Score: " + str(score))
		print("You are at the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "West of House"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves =+ 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score += current_location["score"]
	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")