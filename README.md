<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Korean Word of the Day</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }

        body {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-image: url('assets/bg.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        /* Dark overlay to ensure text is readable against bright backgrounds */
        body::before {
            content: '';
            position: absolute;
            top:0; left:0; width:100%; height:100%;
            background: rgba(0, 0, 0, 0.45);
            z-index: -1;
        }

        /* Sleek Glassmorphism card */
        .card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            padding: 40px;
            border-radius: 24px;
            width: 400px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
            border: 1px solid rgba(255,255,255,0.3);
            color: #fff;
            position: relative;
            overflow: hidden;
            animation: fadeIn 0.8s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 {
            font-size: 22px;
            margin-bottom: 25px;
            font-weight: 700;
            letter-spacing: 1px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
            color: #fff;
        }

        .word-section {
            transition: opacity 0.3s ease;
        }

        .word {
            font-size: 44px;
            font-weight: 700;
            margin-bottom: 5px;
            text-shadow: 0 2px 8px rgba(0,0,0,0.4);
            letter-spacing: -1px;
        }

        .pronunciation {
            font-size: 15px;
            color: rgba(255, 255, 255, 0.8);
            margin-bottom: 10px;
            font-style: italic;
            font-weight: 300;
        }

        .meaning {
            font-size: 22px;
            font-weight: 500;
            margin-bottom: 25px;
            text-shadow: 0 1px 3px rgba(0,0,0,0.4);
            color: #ffdeeb;
            background: rgba(0,0,0,0.2);
            display: inline-block;
            padding: 4px 16px;
            border-radius: 20px;
        }

        .sentence-box {
            background: rgba(0, 0, 0, 0.3);
            padding: 18px;
            border-radius: 16px;
            margin-bottom: 25px;
            font-size: 14px;
            text-align: left;
            border-left: 4px solid #ff9a9e;
            box-shadow: inset 0 2px 5px rgba(0,0,0,0.2);
        }

        .sentence {
            font-weight: 500;
            margin-bottom: 6px;
            line-height: 1.4;
        }

        .sentence-meaning {
            color: rgba(255,255,255,0.7);
            font-weight: 300;
        }

        .actions {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-bottom: 10px;
        }

        /* Improved Listen Option */
        .btn-listen {
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
            color: #333;
            width: 56px;
            height: 56px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            border: none;
            box-shadow: 0 4px 15px rgba(255, 154, 158, 0.4);
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
        }

        .btn-listen::before {
            content: '';
            position: absolute;
            top: -4px; left: -4px; right: -4px; bottom: -4px;
            border-radius: 50%;
            border: 2px solid rgba(255, 154, 158, 0.5);
            opacity: 0;
            transition: all 0.3s;
        }

        .btn-listen:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(255, 154, 158, 0.6);
        }

        .btn-listen:hover::before {
            opacity: 1;
            transform: scale(1.1);
        }
        
        .btn-listen svg {
            width: 26px;
            height: 26px;
            fill: #c01a5b;
            margin-left: 2px;
        }

        .btn-nav {
            padding: 12px 24px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            background: rgba(255,255,255,0.2);
            color: white;
            font-weight: 500;
            transition: all 0.3s;
            border: 1px solid rgba(255,255,255,0.3);
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 1px;
        }

        .btn-nav:hover {
            background: rgba(255,255,255,0.35);
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }

        .btn-nav:active {
            transform: translateY(0);
        }

        /* Quiz UI Elements */
        .quiz-section {
            display: none; 
            flex-direction: column;
            align-items: center;
            animation: fadeIn 0.4s ease-out;
        }
        
        .quiz-title {
            font-size: 20px;
            margin-bottom: 15px;
            color: #ffdeeb;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .quiz-prompt {
            font-size: 14px;
            margin-bottom: 10px;
            opacity: 0.9;
        }

        .quiz-question {
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 25px;
            background: rgba(0,0,0,0.3);
            padding: 10px 30px;
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.2);
        }

        .quiz-options {
            display: flex;
            flex-direction: column;
            gap: 12px;
            width: 100%;
        }

        .quiz-option {
            background: rgba(255,255,255,0.15);
            border: 1px solid rgba(255,255,255,0.4);
            padding: 14px;
            border-radius: 14px;
            cursor: pointer;
            color: white;
            font-size: 15px;
            font-weight: 500;
            transition: all 0.2s ease;
        }

        .quiz-option:hover {
            background: rgba(255,255,255,0.3);
            transform: scale(1.02);
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }

        .quiz-option.correct {
            background: rgba(74, 222, 128, 0.8) !important;
            border-color: #4ade80 !important;
            color: #fff;
            transform: scale(1.05);
        }

        .quiz-option.incorrect {
            background: rgba(248, 113, 113, 0.8) !important;
            border-color: #f87171 !important;
            color: #fff;
            animation: shake 0.4s cubic-bezier(.36,.07,.19,.97) both;
        }

        @keyframes shake {
            10%, 90% { transform: translate3d(-1px, 0, 0); }
            20%, 80% { transform: translate3d(2px, 0, 0); }
            30%, 50%, 70% { transform: translate3d(-4px, 0, 0); }
            40%, 60% { transform: translate3d(4px, 0, 0); }
        }
        
        .quiz-feedback {
            margin-top: 20px;
            font-size: 16px;
            font-weight: 700;
            min-height: 24px;
            text-shadow: 0 1px 2px rgba(0,0,0,0.5);
        }

    </style>
</head>
<body>

<div class="card">
    <h1>🇰🇷 Daily Korean</h1>

    <div class="word-section" id="wordSection">
        <div class="word" id="word"></div>
        <div class="pronunciation" id="pronunciation"></div>
        <div class="meaning" id="meaning"></div>

        <div class="sentence-box">
            <div class="sentence" id="sentence"></div>
            <div class="sentence-meaning" id="sentenceMeaning"></div>
        </div>

        <div class="actions">
            <button class="btn-nav" onclick="changeDay(-1)">Prev</button>
            <button class="btn-listen" onclick="speakWord()" title="Listen to pronunciation">
                <svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
            </button>
            <button class="btn-nav" onclick="changeDay(1)">Next</button>
        </div>
    </div>

    <!-- Quiz Engine Interface -->
    <div class="quiz-section" id="quizSection">
        <div class="quiz-title">✨ Knowledge Check ✨</div>
        <div class="quiz-prompt">What does this word mean?</div>
        <div class="quiz-question" id="quizWord"></div>
        <div class="quiz-options" id="quizOptions">
            <!-- Dynamically populated options -->
        </div>
        <div class="quiz-feedback" id="quizFeedback"></div>
    </div>
</div>

<script>
// Exhaustive dictionary with example sentences mapped to everyday scenarios.
const words = [
{ word: "안녕하세요", pronunciation: "annyeong-haseyo", meaning: "Hello", sentence: "안녕하세요, 만나서 반갑습니다.", sentenceMeaning: "Hello, nice to meet you." },
{ word: "안녕", pronunciation: "annyeong", meaning: "Hi (casual)", sentence: "안녕, 오랜만이야!", sentenceMeaning: "Hi, long time no see!" },
{ word: "감사합니다", pronunciation: "gam-sa-ham-ni-da", meaning: "Thank you", sentence: "도와주셔서 감사합니다.", sentenceMeaning: "Thank you for your help." },
{ word: "고마워", pronunciation: "go-ma-wo", meaning: "Thanks (casual)", sentence: "항상 고마워.", sentenceMeaning: "Thanks always." },
{ word: "죄송합니다", pronunciation: "joe-song-ham-ni-da", meaning: "Sorry", sentence: "늦어서 죄송합니다.", sentenceMeaning: "I am sorry for being late." },
{ word: "미안해", pronunciation: "mi-an-hae", meaning: "Sorry (casual)", sentence: "내가 정말 미안해.", sentenceMeaning: "I am really sorry." },
{ word: "네", pronunciation: "ne", meaning: "Yes", sentence: "네, 알겠습니다.", sentenceMeaning: "Yes, I understand." },
{ word: "아니요", pronunciation: "a-ni-yo", meaning: "No", sentence: "아니요, 괜찮습니다.", sentenceMeaning: "No, it's fine." },
{ word: "괜찮아요", pronunciation: "gwaen-chan-a-yo", meaning: "It's okay", sentence: "의사는 괜찮아요.", sentenceMeaning: "The intention is fine / I'm okay." },
{ word: "좋아요", pronunciation: "jo-a-yo", meaning: "Good", sentence: "날씨가 정말 좋아요.", sentenceMeaning: "The weather is really good." },
{ word: "이름", pronunciation: "i-reum", meaning: "Name", sentence: "이름이 뭐예요?", sentenceMeaning: "What is your name?" },
{ word: "저는", pronunciation: "jeo-neun", meaning: "I am", sentence: "저는 학생입니다.", sentenceMeaning: "I am a student." },
{ word: "학생", pronunciation: "hak-saeng", meaning: "Student", sentence: "대학생이에요.", sentenceMeaning: "I am a college student." },
{ word: "학교", pronunciation: "hak-gyo", meaning: "School", sentence: "학교에 가요.", sentenceMeaning: "I am going to school." },
{ word: "선생님", pronunciation: "seon-saeng-nim", meaning: "Teacher", sentence: "선생님, 질문 있어요.", sentenceMeaning: "Teacher, I have a question." },
{ word: "친구", pronunciation: "chin-gu", meaning: "Friend", sentence: "제 가장 친한 친구예요.", sentenceMeaning: "This is my best friend." },
{ word: "사람", pronunciation: "sa-ram", meaning: "Person", sentence: "정말 좋은 사람이에요.", sentenceMeaning: "He/She is a really good person." },
{ word: "사랑", pronunciation: "sa-rang", meaning: "Love", sentence: "당신을 사랑해요.", sentenceMeaning: "I love you." },
{ word: "가족", pronunciation: "ga-jok", meaning: "Family", sentence: "가족이 모두 모였어요.", sentenceMeaning: "The whole family gathered." },
{ word: "물", pronunciation: "mul", meaning: "Water", sentence: "얼음 물 좀 주세요.", sentenceMeaning: "Please give me some ice water." },
{ word: "밥", pronunciation: "bap", meaning: "Meal", sentence: "밥 먹었어요?", sentenceMeaning: "Did you have a meal/eat?" },
{ word: "음식", pronunciation: "eum-sik", meaning: "Food", sentence: "저는 매운 음식을 좋아해요.", sentenceMeaning: "I like spicy food." },
{ word: "커피", pronunciation: "keo-pi", meaning: "Coffee", sentence: "커피 한 잔 마실래요?", sentenceMeaning: "Would you like a cup of coffee?" },
{ word: "차", pronunciation: "cha", meaning: "Tea", sentence: "따뜻한 녹차 주세요.", sentenceMeaning: "Please give me warm green tea." },
{ word: "시간", pronunciation: "shi-gan", meaning: "Time", sentence: "지금 시간이 없어요.", sentenceMeaning: "I don't have time right now." },
{ word: "오늘", pronunciation: "o-neul", meaning: "Today", sentence: "오늘은 쉬는 날이에요.", sentenceMeaning: "Today is my day off." },
{ word: "내일", pronunciation: "nae-il", meaning: "Tomorrow", sentence: "내일 다시 봐요.", sentenceMeaning: "Let's see each other again tomorrow." },
{ word: "어제", pronunciation: "eo-je", meaning: "Yesterday", sentence: "어제 뭐 했어요?", sentenceMeaning: "What did you do yesterday?" },
{ word: "지금", pronunciation: "ji-geum", meaning: "Now", sentence: "지금 어디예요?", sentenceMeaning: "Where are you right now?" },
{ word: "여기", pronunciation: "yeo-gi", meaning: "Here", sentence: "여기에 앉으세요.", sentenceMeaning: "Please sit here." },
{ word: "저기", pronunciation: "jeo-gi", meaning: "There", sentence: "저기요, 주문할게요!", sentenceMeaning: "Excuse me (over there), I'd like to order!" },
{ word: "어디", pronunciation: "eo-di", meaning: "Where", sentence: "어디로 가요?", sentenceMeaning: "Where are you going?" },
{ word: "가다", pronunciation: "ga-da", meaning: "To go", sentence: "이제 집에 가요.", sentenceMeaning: "I'm going home now." },
{ word: "오다", pronunciation: "o-da", meaning: "To come", sentence: "잠깐 이리 와요.", sentenceMeaning: "Come here for a second." },
{ word: "먹다", pronunciation: "meok-da", meaning: "To eat", sentence: "저녁을 맛있게 먹어요.", sentenceMeaning: "Enjoy your dinner." },
{ word: "마시다", pronunciation: "ma-shi-da", meaning: "To drink", sentence: "매일 물을 많이 마셔요.", sentenceMeaning: "I drink a lot of water every day." },
{ word: "보다", pronunciation: "bo-da", meaning: "To see", sentence: "주말에 영화를 봐요.", sentenceMeaning: "I watch a movie on the weekend." },
{ word: "하다", pronunciation: "ha-da", meaning: "To do", sentence: "지금 숙제를 해요.", sentenceMeaning: "I am doing my homework now." },
{ word: "공부하다", pronunciation: "gong-bu-ha-da", meaning: "To study", sentence: "매일 한국어를 공부해요.", sentenceMeaning: "I study Korean every day." },
{ word: "일하다", pronunciation: "il-ha-da", meaning: "To work", sentence: "회사에서 늦게까지 일해요.", sentenceMeaning: "I work late at the company." },
{ word: "쉬다", pronunciation: "shwi-da", meaning: "To rest", sentence: "오늘은 집에서 쉴 거예요.", sentenceMeaning: "I will rest at home today." },
{ word: "크다", pronunciation: "keu-da", meaning: "Big", sentence: "이 신발은 너무 커요.", sentenceMeaning: "These shoes are too big." },
{ word: "작다", pronunciation: "jak-da", meaning: "Small", sentence: "사이즈가 좀 작아요.", sentenceMeaning: "The size is a bit small." },
{ word: "빠르다", pronunciation: "ppa-reu-da", meaning: "Fast", sentence: "한국의 인터넷은 정말 빨라요.", sentenceMeaning: "The internet in Korea is really fast." },
{ word: "느리다", pronunciation: "neu-ri-da", meaning: "Slow", sentence: "차가 많아서 너무 느려요.", sentenceMeaning: "It's too slow because there are many cars." },
{ word: "좋다", pronunciation: "jo-ta", meaning: "Good", sentence: "이 노래 참 좋네요.", sentenceMeaning: "This song is really good." },
{ word: "나쁘다", pronunciation: "na-ppeu-da", meaning: "Bad", sentence: "기분이 나빠요.", sentenceMeaning: "I feel in a bad mood." },
{ word: "쉽다", pronunciation: "swip-da", meaning: "Easy", sentence: "한국어 발음은 비교적 쉬워요.", sentenceMeaning: "Korean pronunciation is relatively easy." },
{ word: "어렵다", pronunciation: "eo-ryeop-da", meaning: "Difficult", sentence: "수학은 너무 어려워요.", sentenceMeaning: "Math is too difficult." },
{ word: "덥다", pronunciation: "deop-da", meaning: "Hot", sentence: "오늘 날씨가 진짜 덥네요.", sentenceMeaning: "The weather is really hot today." },
{ word: "춥다", pronunciation: "chup-da", meaning: "Cold", sentence: "겨울은 추워요.", sentenceMeaning: "Winter is cold." },
{ word: "왼쪽", pronunciation: "oen-jjok", meaning: "Left", sentence: "왼쪽으로 쭉 가세요.", sentenceMeaning: "Go straight to the left." },
{ word: "오른쪽", pronunciation: "o-reun-jjok", meaning: "Right", sentence: "오른쪽으로 도세요.", sentenceMeaning: "Turn to the right." },
{ word: "앞", pronunciation: "ap", meaning: "Front", sentence: "건물 앞에 편의점이 있어요.", sentenceMeaning: "There is a convenience store in front of the building." },
{ word: "뒤", pronunciation: "dwi", meaning: "Back", sentence: "제 뒤에 줄을 서세요.", sentenceMeaning: "Please line up behind me." },
{ word: "위", pronunciation: "wi", meaning: "Up", sentence: "책상 위에 휴대폰이 있어요.", sentenceMeaning: "The phone is on the desk." },
{ word: "아래", pronunciation: "a-rae", meaning: "Down", sentence: "의자 아래에 고양이가 있어요.", sentenceMeaning: "There is a cat under the chair." },
{ word: "얼마", pronunciation: "eol-ma", meaning: "How much", sentence: "이거 전부 얼마예요?", sentenceMeaning: "How much is all of this?" },
{ word: "왜", pronunciation: "wae", meaning: "Why", sentence: "왜 그렇게 생각해요?", sentenceMeaning: "Why do you think so?" },
{ word: "언제", pronunciation: "eon-je", meaning: "When", sentence: "우리 언제 만날까요?", sentenceMeaning: "When shall we meet?" },
{ word: "어떻게", pronunciation: "eo-tteo-ke", meaning: "How", sentence: "거기에 어떻게 가요?", sentenceMeaning: "How do I get there?" },
{ word: "주세요", pronunciation: "ju-se-yo", meaning: "Please give me", sentence: "메뉴판 좀 주세요.", sentenceMeaning: "Please give me the menu." },
{ word: "도와주세요", pronunciation: "do-wa-ju-se-yo", meaning: "Help me", sentence: "길을 잃었어요, 도와주세요.", sentenceMeaning: "I'm lost, please help me." },
{ word: "잠시만요", pronunciation: "jam-shi-man-yo", meaning: "Wait", sentence: "잠시만요, 길 좀 지나갈게요.", sentenceMeaning: "Excuse me (wait a moment), passing through." },
{ word: "다시", pronunciation: "da-shi", meaning: "Again", sentence: "다시 한 번 말해주세요.", sentenceMeaning: "Please say it again." },
{ word: "알겠습니다", pronunciation: "al-get-seum-ni-da", meaning: "I understand", sentence: "네, 명심하겠습니다. 알겠습니다.", sentenceMeaning: "Yes, I'll keep it in mind. I understand." },
{ word: "몰라요", pronunciation: "mol-la-yo", meaning: "I don’t know", sentence: "저는 정말 단어를 몰라요.", sentenceMeaning: "I really don't know the word." },
{ word: "행복", pronunciation: "haeng-bok", meaning: "Happiness", sentence: "가족과 함께라 행복해요.", sentenceMeaning: "I am happy to be with my family." },
{ word: "슬픔", pronunciation: "seul-peum", meaning: "Sadness", sentence: "영화가 너무 슬퍼요.", sentenceMeaning: "The movie is too sad." },
{ word: "피곤하다", pronunciation: "pi-gon-ha-da", meaning: "Tired", sentence: "일이 많아서 피곤해요.", sentenceMeaning: "I am tired because of a lot of work." },
{ word: "배고프다", pronunciation: "bae-go-peu-da", meaning: "Hungry", sentence: "배가 너무 고파요.", sentenceMeaning: "I am so hungry." },
{ word: "목마르다", pronunciation: "mok-ma-reu-da", meaning: "Thirsty", sentence: "운동해서 목이 마르네요.", sentenceMeaning: "I am thirsty after exercising." },
{ word: "돈", pronunciation: "don", meaning: "Money", sentence: "돈을 절약해야 해요.", sentenceMeaning: "We should save money." },
{ word: "버스", pronunciation: "beo-seu", meaning: "Bus", sentence: "버스를 타고 학교에 가요.", sentenceMeaning: "I take the bus to school." },
{ word: "지하철", pronunciation: "ji-ha-cheol", meaning: "Subway", sentence: "지하철역이 어디에 있어요?", sentenceMeaning: "Where is the subway station?" },
{ word: "택시", pronunciation: "taek-shi", meaning: "Taxi", sentence: "비가 오니까 택시를 타요.", sentenceMeaning: "Since it's raining, let's take a taxi." },
{ word: "집", pronunciation: "jip", meaning: "House", sentence: "집에 가고 싶어요.", sentenceMeaning: "I want to go home." },
{ word: "방", pronunciation: "bang", meaning: "Room", sentence: "제 방은 2층이에요.", sentenceMeaning: "My room is on the 2nd floor." },
{ word: "전화", pronunciation: "jeon-hwa", meaning: "Phone", sentence: "전화번호가 뭐예요?", sentenceMeaning: "What is your phone number?" },
{ word: "컴퓨터", pronunciation: "keom-pyu-teo", meaning: "Computer", sentence: "컴퓨터 게임을 좋아해요.", sentenceMeaning: "I like computer games." },
{ word: "인터넷", pronunciation: "in-teo-net", meaning: "Internet", sentence: "인터넷 연결이 안 돼요.", sentenceMeaning: "The internet connection is not working." },
{ word: "날씨", pronunciation: "nal-ssi", meaning: "Weather", sentence: "오늘 날씨가 맑아요.", sentenceMeaning: "The weather is clear today." },
{ word: "비", pronunciation: "bi", meaning: "Rain", sentence: "우산을 챙기세요, 비가 오고 있어요.", sentenceMeaning: "Take an umbrella, it is raining." },
{ word: "눈", pronunciation: "nun", meaning: "Snow", sentence: "겨울에는 눈이 예쁘게 내려요.", sentenceMeaning: "In winter, the snow falls beautifully." },
{ word: "바람", pronunciation: "ba-ram", meaning: "Wind", sentence: "바람이 차가워요.", sentenceMeaning: "The wind is cold." },
{ word: "아침", pronunciation: "a-chim", meaning: "Morning", sentence: "아침 7시에 일어나요.", sentenceMeaning: "I wake up at 7 in the morning." },
{ word: "점심", pronunciation: "jeom-shim", meaning: "Lunch", sentence: "점심 메뉴 정하셨어요?", sentenceMeaning: "Have you decided on the lunch menu?" },
{ word: "저녁", pronunciation: "jeo-nyeok", meaning: "Evening", sentence: "저녁 식사 약속이 있어요.", sentenceMeaning: "I have a dinner appointment." },
{ word: "밤", pronunciation: "bam", meaning: "Night", sentence: "밤하늘의 별이 예뻐요.", sentenceMeaning: "The stars in the night sky are beautiful." }
];

let globalIndex = 0;              // Current position in our simulated continuous feed
let interactionsSinceQuiz = 0;    // Tracks progression towards next quiz
let wordsViewed = new Set();      // Memory bank for Quiz options
let isQuizActive = false;
let currentQuizWord = null;

const wordSection = document.getElementById("wordSection");
const quizSection = document.getElementById("quizSection");

function updateUI() {
    // Math to smoothly wrap around arrays
    const index = (globalIndex % words.length + words.length) % words.length;
    const selected = words[index];
    wordsViewed.add(selected);

    document.getElementById("word").innerText = selected.word;
    document.getElementById("pronunciation").innerText = selected.pronunciation;
    document.getElementById("meaning").innerText = selected.meaning;
    document.getElementById("sentence").innerText = selected.sentence || "";
    document.getElementById("sentenceMeaning").innerText = selected.sentenceMeaning || "";
}

function triggerQuiz() {
    isQuizActive = true;
    wordSection.style.display = "none";
    quizSection.style.display = "flex";
    document.getElementById("quizFeedback").innerText = "";

    // Pick a random word from the user's recently viewed words
    const viewedArray = Array.from(wordsViewed);
    currentQuizWord = viewedArray[Math.floor(Math.random() * viewedArray.length)];

    document.getElementById("quizWord").innerText = currentQuizWord.word;

    // Generate 3 random wrong options + the 1 correct option
    let options = new Set();
    options.add(currentQuizWord);
    while(options.size < 4) {
        let randWord = words[Math.floor(Math.random() * words.length)];
        options.add(randWord);
    }

    // Shuffle options
    let optionsArray = Array.from(options).sort(() => Math.random() - 0.5);
    const optionsContainer = document.getElementById("quizOptions");
    optionsContainer.innerHTML = "";

    optionsArray.forEach(opt => {
        let btn = document.createElement("button");
        btn.className = "quiz-option";
        btn.innerText = opt.meaning;
        btn.onclick = () => handleQuizAnswer(btn, opt === currentQuizWord);
        optionsContainer.appendChild(btn);
    });
}

function handleQuizAnswer(btn, isCorrect) {
    let allBtns = document.querySelectorAll(".quiz-option");
    allBtns.forEach(b => b.disabled = true);

    if (isCorrect) {
        btn.classList.add("correct");
        document.getElementById("quizFeedback").innerText = "Correct! ✨";
        document.getElementById("quizFeedback").style.color = "#4ade80";
        setTimeout(() => {
            isQuizActive = false;
            interactionsSinceQuiz = 0;
            quizSection.style.display = "none";
            wordSection.style.display = "block";
            updateUI(); // Display the next scheduled word
        }, 1200);
    } else {
        btn.classList.add("incorrect");
        document.getElementById("quizFeedback").innerText = "Not quite. Try again!";
        document.getElementById("quizFeedback").style.color = "#f87171";
        setTimeout(() => {
            btn.classList.remove("incorrect");
            allBtns.forEach(b => b.disabled = false);
            document.getElementById("quizFeedback").innerText = "";
        }, 1000);
    }
}

function changeDay(step) {
    if (isQuizActive) return;

    globalIndex += step;
    
    // Only accumulate points towards a quiz when moving forward
    if (step > 0) {
        interactionsSinceQuiz++;
    } else {
        interactionsSinceQuiz--;
    }

    // Trigger quiz every exactly 10 progressions forward
    if (interactionsSinceQuiz >= 10 && wordsViewed.size > 0) {
        triggerQuiz();
    } else {
        updateUI();
    }
}

function speakWord() {
    const word = document.getElementById("word").innerText;
    const utterance = new SpeechSynthesisUtterance(word);
    utterance.lang = "ko-KR";
    utterance.rate = 0.85; // slightly slower for language learning
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(utterance);
}

// Initial hydration based on start day seed offset
// Setting start offset based on the day of the year
const now = new Date();
const startOfYear = new Date(now.getFullYear(), 0, 0);
const diff = now - startOfYear;
const oneDay = 1000 * 60 * 60 * 24;
globalIndex = Math.floor(diff / oneDay);

updateUI();
</script>

</body>
</html>
