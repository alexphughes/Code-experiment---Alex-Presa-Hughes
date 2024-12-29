from psychopy import gui, event, core, visual, data
import pandas as pd
import random
import hashlib
import string
import os
import re

win = visual.Window(color = "white", size = (1536, 864))



def introduction():
    introduction_message = visual.TextStim(win, text = "Welcome to this experiment. You will be shown headlines from news articles.", color = "black")
    introduction_message.draw()
    win.flip()
    core.wait(3)
    consent_message_1 = visual.TextStim(win, text = "Your consent is needed to proceed.", color = "black", pos = (0, 0.5), bold = True)
    consent_message_2 = visual.TextStim(win, text = "Press 'Y' to accept the conditions or 'N' to deny approval.", color = "black", pos = (0, 0))
    consent_message_3 = visual.TextStim(win, text = "To see conditions press 'C'.", color = "black", pos = (0, -0.5))
    consent_message_1.draw()
    consent_message_2.draw()
    consent_message_3.draw()
    win.flip()
    consent_keys = event.waitKeys(keyList = ["y", "n", "c"])
    if "y" in consent_keys:
        approved_consent = visual.TextStim(win, text = "You have given your consent.", color = "black", pos = (0, 0))
        approved_consent.draw()
        win.flip()
        core.wait(3)
    elif "n" in consent_keys:
        denied_consent = visual.TextStim(win, text = "You have not given your consent. Therefore, you will exit this experiment.", color = "black", pos = (0, 0))
        denied_consent.draw()
        win.flip()
        core.wait(3)
        core.quit()
    elif "c" in consent_keys:
        consent_title_1 = visual.TextStim(win, text = "Analysis of Recall Performance for News Headlines across Variables: Word Count, Readability, Polarity and Subjectivity ", color = "black", italic = True, pos = (0, 0.65), height = 0.06)
        consent_title_2 = visual.TextStim(win, text = "CONSENT FORM", color = "black", bold = True, pos = (0, 0.8))
        consent_information_1 = visual.TextStim(win, text = "I hereby confirm that I have voluntarily signed up for this experiment and that I am fully aware of and agree with the purpose of the experiment and conditions that this entails, which are the following:\n\n1) The data collected from participants will always be anonimized and their personal identities will never be at risk.\n2) The data collected will be strictly used for scientific purposes and will never be shared for other purposes.\n3) Participants may withdraw their consent at any time as this experiment is completely voluntary.\n\nThis experiment will be carried out by Alex Presa Hughes (202409807@post.au.dk).", color = "black", pos = (0, -0.3), height = 0.05, wrapWidth = 1.5)
        consent_information_2 = visual.TextStim(win, text = "Press 'space' to return to consent screen.", color = "black", bold = True, pos = (0, -0.75))
        consent_information_3 = visual.TextStim(win, text = "The purpose of this experiment is to analyse the influence of various factors in headlines like word length, readability, subjectivity and polarity on reading time and recall accuracy. Participants' reaction times and accuracy scores when recalling headlines will be stored to conduct the analyses. There are not any known risks. You will be contributing to the field of Cognitive Science.", color = "black", height = 0.05, pos = (0, 0.35), wrapWidth = 1.5)
        consent_information_4 = visual.TextStim(win, text = "In this experiment, there are three rounds. In each round, you will be shown 4 headlines initially to be remembered, and you will have to recall them out of a group of 8 headlines consisting of the 4 initial headlines and 4 unseen ones. You will repeat this for each round. The experiment will roughly take 4 to 5 minutes.", color = "black", height = 0.05, pos = (0, 0.1), wrapWidth = 1.5)
        au_logo = visual.ImageStim(win, image = "C:/Users/Alex Presa Hughes/Pictures/RandomPhotos/aarhus-university.png", pos = (-0.75, -0.75))
        consent_title_1.draw()
        consent_title_2.draw()
        consent_information_1.draw()
        consent_information_2.draw()
        consent_information_3.draw()
        consent_information_4.draw()
        au_logo.size = 0.3
        au_logo.draw()
        win.flip()
        event.waitKeys()
        consent_message_after_condition = visual.TextStim(win, text = "Press 'Y' to accept the conditions or 'N' to deny approval.", color = "black", pos = (0, 0))
        consent_message_after_condition.draw()
        win.flip()
        consent_keys = event.waitKeys(keyList = ["y", "n"])
        if "y" in consent_keys:
            approved_consent = visual.TextStim(win, text = "You have given your consent.", color = "black", pos = (0, 0))
            approved_consent.draw()
            win.flip()
            core.wait(3)
        elif "n" in consent_keys:
            denied_consent = visual.TextStim(win, text = "You have not given your consent. Therefore, you will exit this experiment.", color = "black", pos = (0, 0))
            denied_consent.draw()
            win.flip()
            core.wait(3)
            core.quit()
    preparation_message_1 = visual.TextStim(win, text = "You are about to see a series of headlines you will have to remember and then recall.", color = "black", pos = (0, 0.6))
    preparation_message_2 = visual.TextStim(win, text = "Press 'space' to start the experiment!", color = "black", pos = (0, -0.6), bold = True)
    flag_image = visual.ImageStim(win, image = "C:/Users/Alex Presa Hughes/Downloads/Screenshot 2024-11-07 133239.png", pos = (0, 0))
    preparation_message_1.draw()
    preparation_message_2.draw()
    flag_image.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    return

def identification():
    return "".join(random.choice(string.ascii_uppercase + string.digits) for character in range(6))

def countdown():
    countdown_text = visual.TextStim(win, text = "countdown", color = "black", pos = (0, 0))
    for i in range(3, 0, -1):
        countdown_text.setText(f"Round will begin in: " + str(i))
        countdown_text.draw()
        win.flip()
        core.wait(1)

def randomize_round_order():
    rounds = ["C:/Users/Alex Presa Hughes/Downloads/COGSCI24/Cognition and Communication/CogComm_Experiment/News_Articles_Analysis_2024-11-20_11h22.47.169.csv",
    "C:/Users/Alex Presa Hughes/Downloads/COGSCI24/Cognition and Communication/CogComm_Experiment/News_Articles_Analysis_2024-11-20_11h23.54.805.csv",
    "C:/Users/Alex Presa Hughes/Downloads/COGSCI24/Cognition and Communication/CogComm_Experiment/News_Articles_Analysis_2024-11-20_11h25.18.841.csv"]
    random.shuffle(rounds)
    return rounds

def show_headlines(csv_path):
    show_articles = pd.read_csv(csv_path)
    shown_articles = []
    informative_message = visual.TextStim(win, text = "After the countdown, memorize the articles.", color = "black", pos = (0, 0))
    informative_message.draw()
    win.flip()
    core.wait(3)
    countdown()
    show_articles = show_articles.sample(frac = 1).reset_index(drop = True)
    for index, article in show_articles.head(4).iterrows():
        show_headline = visual.TextStim(win, text = article["title"], color = "black", pos = (0, 0))
        show_headline.draw()
        win.flip()
        core.wait(3)
        shown_articles.append(article["title"])
    return shown_articles

def recall_headlines(shown_articles, csv_path, round_number):
    id_df = pd.read_csv("C:/Users/Alex Presa Hughes/Downloads/COGSCI24/Cognition and Communication/CogComm_Experiment/News_Articles_Analysis_2024-11-20_11h20.44.846.csv")
    reaction_times = []
    recall_articles = pd.read_csv(csv_path)
    shuffled_recall_headlines = recall_articles.sample(frac=1).reset_index(drop=True)
    headline_question = visual.TextStim(win, text = "Have you seen the following headlines?\n\nPress 'Y' for Yes.\n\nPress 'N' for No.", color = "black", pos = (0, 0.4))
    photo_question = visual.ImageStim(win, image = "C:/Users/Alex Presa Hughes/Pictures/RandomPhotos/thinking-emoji-doodle-emoticon-symbols-chat-sticker-face-and-thumb-free-vector-removebg-preview.png", pos = (0, -0.2))
    photo_question.size = 0.5
    wait_message = visual.TextStim(win, text = "Wait.", color = "black", pos = (0, -0.6), bold = True)
    headline_question.draw()
    photo_question.draw()
    wait_message.draw()
    win.flip()
    core.wait(5)
    for index, article in shuffled_recall_headlines.iterrows():
        recall_headline = visual.TextStim(win, text = article["title"], color = "black", pos = (0, 0))
        recall_headline.draw()
        win.flip()
        stopwatch = core.Clock()
        recall_keys = event.waitKeys(keyList = ["y", "n"])
        reaction_time = stopwatch.getTime()
        if recall_keys[0] == "y" and article["title"] in shown_articles:
            response = "correct"
            correct_answer = visual.TextStim(win, text = "Correct!", pos = (0, 0), color = "green")
            correct_answer.draw()
            win.flip()
            core.wait(1)
        elif recall_keys[0] == "n" and article["title"] not in shown_articles:
            response = "correct"
            correct_answer = visual.TextStim(win, text = "Correct!", pos = (0, 0), color = "green")
            correct_answer.draw()
            win.flip()
            core.wait(1)
        else:
            response = "incorrect"
            incorrect_answer = visual.TextStim(win, text = "Incorrect!", pos = (0, 0), color = "red")
            incorrect_answer.draw()
            win.flip()
            core.wait(1)
        if article["title"] in shown_articles:
            shown_or_not = "shown"
        else:
            shown_or_not = "not_shown"
        reaction_times.append({
        "headline": article["title"],
        "response": response,
        "reaction_time": reaction_time,
        "round_number": round_number,
        "shown_or_not": shown_or_not,
        "number_of_words": article["number_of_words"],
        "readability": article["readability"],
        "polarity": article["polarity"],
        "subjectivity": article["subjectivity"]
        })
    return reaction_times

def farewell():
    farewell_adress = visual.TextStim(win, text = "Thank you for participanting!\nYou have promoted the field of Cognitive Science.", pos = (0, 0), color = "black")
    farewell_adress.draw()
    win.flip()
    core.wait(3)

def save_data(reaction_times, ID):
    dataframe = pd.DataFrame(reaction_times)
    dataframe["ID"] = ID
    folder_path = "C:/Users/Alex Presa Hughes/Downloads/COGSCI24/Cognition and Communication/Participant_Data_CogComm"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file = os.path.join(folder_path, "Experiment_Data_Headlines.csv")
    file_exists = os.path.isfile(file)
    dataframe.to_csv(file, mode = "a", header = not file_exists, index = False)
    print("Dataframe saved!")

def run_experiment():
    introduction()
    participant_ID = identification()
    rounds = randomize_round_order()
    for round_index, csv_path in enumerate(rounds, 1):
        shown_articles = show_headlines(csv_path)
        reaction_times = recall_headlines(shown_articles, csv_path, round_index)
        save_data(reaction_times, participant_ID)
    farewell()
    core.quit()

run_experiment()