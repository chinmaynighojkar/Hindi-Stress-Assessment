import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Set up Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('C:\ChinmayProjects\HappiMynd\happimynd-3460553cc66f.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheets document by its title
spreadsheet = client.open_by_key("1YpIAgkk9nkpczG6U9k-f2aafMy0Tn3Fmu-JJ-O278TY")
worksheet = spreadsheet.get_worksheet(0)  # Assuming the data is in the first worksheet

def categorize_stress_level(total_score):
    if total_score <= 13:
        return "आपका तनाव स्तर कम  है।"
    elif 14 <= total_score <= 26:
        return "आपका तनाव स्तर मध्यम है।"
    else:
        return "आपका तनाव स्तर अत्यधिक है।"

def submit_survey_data(name, email, mobile, total_score, stress_level):
    data = [name, email, mobile, total_score, stress_level]
    worksheet.append_row(data)
    st.success("Data submitted successfully!")
    
def survey_question_1():
    st.markdown("पिछले महीने, कितनी बार आपने अचानक कुछ होने के कारण  चिड़चिड़ेपन का अहसास किया है?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 1 के लिए एक विकल्प चुनें:", options, index=None, key="question1")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "अक्सर": 3, "लगभग हमेशा": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_2():
    st.markdown("पिछले महीने, कितनी बार आपने महसूस किया है कि आप अपनी जीवन की महत्वपूर्ण चीजों को नियंत्रित  नहीं कर पा रहे थे?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 2 के लिए एक विकल्प चुनें:", options, index=None, key="question2")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "अक्सर": 3, "लगभग हमेशा": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_3():
    st.markdown("पिछले महीने, कितनी बार आपने घबराहट और तनाव महसूस किया है?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 3 के लिए एक विकल्प चुनें:", options, index=None, key="question3")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "अक्सर": 3, "लगभग हमेशा": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_4():
    st.markdown("पिछले महीने, कितनी बार आपने आत्मविश्वास महसूस किया है कि आप अपनी व्यक्तिगत समस्याओं को संभालने की क्षमता रखते हैं?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 4 के लिए एक विकल्प चुनें:", options, index=None, key="question4")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "अक्सर": 3, "लगभग हमेशा": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_5():
    st.markdown("पिछले महीने, कितनी बार आपने महसूस किया है कि चीजें आपके अनुरूप हो रही हैं?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 5 के लिए एक विकल्प चुनें:", options, index=None, key="question5")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "अक्सर": 3, "लगभग हमेशा": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_6():
    st.markdown(" पिछले महीने, कितनी बार आपने महसूस किया है कि जो आपको करना था  उन सभी चीजों को संभाल नहीं सकते थे")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 6 के लिए एक विकल्प चुनें:", options, index=None, key="question6")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 0, "लगभग कभी नहीं": 1, "कभी-कभी": 2, "अक्सर": 3, "लगभग हमेशा": 4}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_7():
    st.markdown("पिछले महीने, कितनी बार आपने अपने जीवन में चिड़चिड़ापन को नियंत्रित कर पाए हैं?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 7 के लिए एक विकल्प चुनें:", options, index=None, key="question7")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 4, "लगभग कभी नहीं": 3, "कभी-कभी": 2, "अक्सर": 1, "लगभग हमेशा": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_8():
    st.markdown("पिछले महीने, कितनी बार आपने अपने जीवन में चिड़चिड़ापन को नियंत्रित कर पाए हैं?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 8 के लिए एक विकल्प चुनें:", options, index=None, key="question8")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 4, "लगभग कभी नहीं": 3, "कभी-कभी": 2, "अक्सर": 1, "लगभग हमेशा": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_9():
    st.markdown("पिछले महीने में, आप कितनी बार उन चीजों के कारण क्रोधित हुए हैं जो आपके नियंत्रण से बाहर थीं?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 9 के लिए एक विकल्प चुनें:", options, index=None, key="question9")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 4, "लगभग कभी नहीं": 3, "कभी-कभी": 2, "अक्सर": 1, "लगभग हमेशा": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_10():
    st.markdown("पिछले महीने, कितनी बार आपने यह महसूस किया है कि समस्याएं इतनी  ज़्यादा हैं कि आप उनसे उभर नहीं सकते?")
    options = ["कभी नहीं", "लगभग कभी नहीं", "कभी-कभी", "काफी अक्सर", "बहुत अक्सर"]
    selected_option = st.radio("प्रश्न 10 के लिए एक विकल्प चुनें:", options, index=None, key="question10")

    # Assign scores based on the selected option
    scores = {"कभी नहीं": 4, "लगभग कभी नहीं": 3, "कभी-कभी": 2, "अक्सर": 1, "लगभग हमेशा": 0}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def get_user_info():
    name = st.text_input("आपका नाम:")
    email = st.text_input("आपका ईमेल:")
    mobile_number = st.text_input("आपका मोबाइल नंबर:")

    # Validate that name, email, and mobile_number are not empty
    if not name.strip():
        st.warning("कृपया अपना नाम दर्ज करें।")
        return None, None, None

    if not email.strip():
        st.warning("कृपया अपना ईमेल दर्ज करें।")
        return None, None, None

    if not mobile_number.strip():
        st.warning("कृपया अपना मोबाइल नंबर दर्ज करें।")
        return None, None, None

    return name, email, mobile_number    
  
def main():
    st.image("HLS-removebg-preview.png", width = 150)
    st.title("तनाव जांच")
    
    # Collect user information
    name, email, mobile_number = get_user_info()

    # First question
    score1 = survey_question_1()

    # Second question
    score2 = survey_question_2()

    # Third question
    score3 = survey_question_3()

    # Fourth question
    score4 = survey_question_4()

    # Fifth question
    score5 = survey_question_5()

    # Sixth question
    score6 = survey_question_6()

    # Seventh question
    score7 = survey_question_7()

    # Eighth question
    score8 = survey_question_8()

    # Ninth question
    score9 = survey_question_9()

    # Tenth question
    score10 = survey_question_10()

    # Handle the case where no option is selected for any question
    if any(score is None for score in [score1, score2, score3, score4, score5, score6, score7, score8, score9, score10]):
        st.warning("Please select an option for all questions.")
        return

    # Calculate total score
    total_score = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10
    
    # Display total score
    st.write(f"Total Score: {total_score}")

    # Categorize stress level and display result
    stress_level = categorize_stress_level(total_score)
    st.write(f"तनाव स्तर: {stress_level}")

# Submit data to Google Sheets
    if st.button("Submit"):
        submit_survey_data(name, email, mobile_number, total_score, stress_level)
 
if __name__ == "__main__":
    main()

