from flask import Flask, render_template, request, redirect, url_for
from random import shuffle

app = Flask(__name__)

data = [
    [
        '31', '1) I was joking, but he took it l___________ .',
        '난 농담으로 얘기했지만, 그는 그것을 글자 그대로 받아들였다.', 'literally'
    ],
    [
        '31',
        '2) Only one third of the population of the country is l___________ . ',
        '그 나라 인구의 3분의 1만이 글을 읽고 쓸 수 있다.', 'literate'
    ],
    [
        '31', '3) James teaches 1st and 2nd grade l___________. ',
        '제임스는 1학년과 2학년에게 문학을 가르친다.', 'literature'
    ], ['31', '4) modern[contemporary] l___________ ', '현대 문학', 'literature'],
    ['31', '5) a l___________ newspaper[call] [ ]', '지역 신문 [시내 전화]', 'local'],
    [
        '31',
        '6) The Olympic games are scheduled to be shown at 7 p.m. l___________ time. ',
        '올림픽 경기는 현지 시각으로 저녁 7시에 중계될 예정이다.', 'local'
    ],
    [
        '31',
        '7) Lasik surgery is usually done under l___________ anesthetic. ',
        '라식 수술은 대개 국부 마취를 한 채 행해진다.', 'local'
    ],
    [
        '31',
        '8) This app can help you l___________ your keys if you lose them. ',
        '이 앱은 당신이 열쇠를 잃어버렸을 때 위치를 찾을 수 있도록 도와준다.', 'locate'
    ],
    [
        '31',
        '9) His apartment was l___________ right next to the police station. ',
        '그의 아파트는 경찰서 바로 옆에 있었다.', 'located'
    ],
    [
        '31', '10) The money was a___________ for building a new school. ',
        '새 학교를 건설하는 데에 자금이 할당되었다.', 'allocated'
    ],
    [
        '31',
        '11) He used sound l___________ and reasoning to win the debate. ',
        '그는 논쟁에서 이기기 위해 타당한 논리와 근거를 들었다.', 'logic'
    ],
    [
        '31',
        '12) Civic groups demanded a public a___________ for his remarks. ',
        '시민 단체들은 그의 발언에 대해 공식적인 사과를 요구했다.', 'apology'
    ],
    [
        '31',
        '13) In the p___________ of the book, the author quoted a passage from the Bible. ',
        '그 책의 서문에서, 작가는 성경의 한 구절을 인용하였다.', 'prologue'
    ],
    [
        '31',
        '14) E___________is the study of the relationship between living things and their environments. ',
        '생태학은 생물과 환경사이의 관례를 연구하는 학문이다.', 'Ecology'
    ],
    [
        '31', '15) experts in the field of developmental p___________ .',
        '발달 심리학 분야의 전문가들', 'psychology'
    ],
    [
        '31',
        '16) I l___________ f___________ the late summer sunsets of home. ',
        '나는 집에서 보는 늦여름의 노을을 고대하고 있다.', 'long, for'
    ],
    [
        '31',
        '17) B___________ l___________, the reality hit Jeremy hard. , Jeremy .',
        '얼마 후, 는 현실을 강하게 깨달았다.', 'Before long'
    ],
    [
        '31', '18) Whom does this cell phone b___________ to ? ',
        '이 핸드폰 누구 것이니?', 'belong'
    ],
    [
        '31',
        '19) I didn’t b___________ there, so I took my belongings and left. ',
        '나는 그곳 소속이 아니었기에, 나의 소지품들을 챙겨 떠났다.', 'belong'
    ],
    [
        '31',
        '20) He p___________ his vist to Korea by two weeks by shortening his stay in Japan. ',
        '그는 일본에 머무르는 기간을 줄여 한국 방문 기간을 2주 연장했다.', 'prolonged'
    ],
    [
        '31', '21) What is the l___________ and width of those curtains? ',
        '그 커튼의 길이와 폭이 얼마입니까?', 'length'
    ],
    [
        '31', '22) The dark clouds l___________ overhead. .',
        '먹구름이 머리 위에 오랫동안 머물러 있었다.', 'lingered'
    ],
    [
        '31',
        "23) Wearing all black gives the i___________ that we're taller and thinner than we really are. ",
        '모두 검은색으로 옷을 입으면 우리가 실제보다 더 키가 크고 날씬해 보인다는 착각을 일으킨다', 'illusion'
    ],
    [
        '31',
        '24) She was under the d___________ that there were ghosts in her house. .',
        '그녀는 집안에 귀신이 있다는 망상에 빠져 있었다.', 'delusion'
    ],
    [
        '32', '1) They do not recognize the m___________ of the problem. .',
        '그들은 그 문제의 중요성을 깨닫지 못하고 있다.', 'magnitude'
    ],
    [
        '32', '2) The microscope m___________ objects 500 times. ',
        '그 현미경은 물체를 500배로 확대하여 보여주었다.', 'magnified'
    ], ['32', "3) a m___________ 's degree ", '석사학위', 'master'],
    [
        '32',
        '4) Mr. Kim is a m___________ gayageum player who has m___________ the art of folk music. .',
        '김선생님은 민속 음악의 기예를 터득한 가야금 연주의 명인이다.', 'master, mastered'
    ],
    [
        '32',
        '5) The work is considered a m___________ of modern literature. .',
        '그 작품은 현대 문학의 걸작으로 평가된다.', 'masterpiece'
    ],
    [
        '32',
        '6) He m___________ in math while in college. Now, however, his m___________ interest is art. ',
        '그는 대학에서 수학을 전공했다. 그러나 지금 그의 주된 관심사는 미술이다.', 'majored, major'
    ],
    [
        '32', '7) She decided to run for m___________ of New York City. ',
        '그녀는 뉴욕 시장 선거에 출마하기로 결심했다.', 'mayor'
    ],
    [
        '32', '8) The palace was m___________ in its design. ',
        '그 궁전은 디자인이 웅장했다.', 'majestic'
    ],
    [
        '32',
        '9) Our goal is to achieve m___________ efficiency with minimum effort. ',
        '우리의 목표는 최소의 노력으로 최대의 효과를 얻는 것이다.', 'maximum'
    ],
    [
        '32', '10) The price changes according to supply and d___________ . ',
        '가격은 수요와 공급에 따라 변한다.', 'demand'
    ],
    [
        '32',
        '11) He c___________ that the house be built to c___________ a fine view of the sea. ',
        '그는 그 집을 바다의 멋진 전경이 내려다보이게 짓도록 명령했다.', 'commanded, command'
    ],
    [
        '32', '12) He had only a few soldiers at his c___________ . ',
        '그는 자신의 지휘 하에 겨우 몇 명의 병사만이 있었다.', 'command'
    ],
    [
        '32', '13) The president m___________ that people stay inside. ',
        '대통령은 국민들이 실내에 머무르도록 명령했다.', 'mandated'
    ],
    [
        '32',
        '14) The new m___________ requires factories to reduce air pollution. ',
        '새로운 규정은 공장들이 대기 오염을 줄이기를 요구한다.', 'mandate'
    ],
    [
        '32', '15) His doctor r___________ not taking any sleeping pills. .',
        '의사는 어떤 수면제도 복용하지 말 것을 권고했다.', 'recommended'
    ],
    [
        '32',
        '16) Does your new camera have automatic and m___________ functions? ',
        '네가 새로산 카메라는 자동 기능과 수동기능을 가지고 있니?', 'manual'
    ],
    [
        '32',
        '17) The first m___________ to teach "table manners" were written in the 12th century.',
        '‘식탁 예절’을 가르치는 최초의 안내서가 12세기에 쓰였다.', 'manuals'
    ],
    [
        '32', '18) She sent her m___________ to a publishing company. .',
        '그녀는 출판사에 원고를 보냈다.', 'manuscript'
    ],
    [
        '32',
        '19) Part of her job is to m___________ good relationships with our suppliers. ',
        '그녀가 하는 일의 일부는 우리의 공급처들과 좋은 관계를 유지하는 것이다.', 'maintain'
    ],
    [
        '32', '20) Throughout the trial, he m___________ his innocence. ',
        '재판받는 동안 내내 그는 자신의 무죄를 주장했다.', 'maintained'
    ],
    [
        '32', '21) They tried to m___________ public opinion. ',
        '그들은 여론을 조작하려 했다.', 'manipulate'
    ],
    [
        '32', '22) She m___________ the company while her father was away. ',
        '그녀는 아버지가 부재중인 동안 회사를 관리 한다.', 'managed'
    ],
    [
        '32',
        "23) He m___________ to fix the computer's hard drive and recover the data. ",
        '그는 결국 컴퓨터 하드 드라이브를 고쳐 데이터를 복원해냈다.', 'managed'
    ],
    [
        '32', '24) The inner m___________ of this clock is broken. ',
        '이 시계의 내부 기계 장치가 고장이다.', 'mechanism'
    ],
    [
        '32',
        '25) Every city has a m___________ for changing its regulations. ',
        '모든 도시를 각자의 규정을 변경하는 방법이 있다.', 'mechanism'
    ], ['32', '26) a defense m___________ ', '방어 기제', 'mechanism'],
    ['32', '27) a car m___________ ', '자동차 수리공', 'mechanic'],
    [
        '32',
        '28) Managers of each department must make sure that all dangerous equipment and m___________ are safely stored. .',
        '각 부서 관리자는 모든 위험한 장비와 기계가 안전하게 보관되도록 해야한다.', 'machinery'
    ], ['33', '1) mass m___________', '대중매체', 'media'],
    [
        '33',
        '2) Which m___________ of communication do you prefer the most? ',
        '어떤 통신 매체를 가장 선호하세요?', 'medium'
    ],
    [
        '33',
        '3) A: How would you like you steak? ? B: M___________ [Well-done/Rare], please. ',
        '스테이크를 어떻게 해드릴까요? 중간 정도로 익혀주세요. ', 'Medium'
    ],
    [
        '33',
        '4) M___________ history began with the fall of the Roman Empire. .',
        '중세사는 로마 제국의 몰락과 함께 시작되었다.', 'medieval'
    ],
    [
        '33',
        '5) My friend is trying to m___________ problems among other students. .',
        '내 친구는 다른 학생들 사이의 문제를 조정하려고 노력하고 있다.', 'mediate'
    ],
    [
        '33', '6) Our government must take i___________ action. .',
        '우리 정부는 즉각적인 조치를 취해야 한다.', 'immediate'
    ],
    [
        '33', "7) What's the i___________ problem? ", '가장 시급한[당면한] 문제는 무엇입니까?',
        'immediate'
    ],
    [
        '33', '8) Did you sign up for the i___________ course this month? ',
        '당신은 이번달에 중급 과정에 등록하셨습니까?', 'intermediate'
    ],
    [
        '33', "9) It m___________ that he's pleased with my behavior. .",
        '그것은 그가 내 행동에 만족한다는 것을 의미한다.', 'means'
    ],
    [
        '33',
        "10) He's not being m___________. He just wants you to learn something. , ",
        '.그는 못되게 구는 것이 아니야, 네가 무언가를 깨우치길 바라는 것뿐이야', 'mean'
    ],
    [
        '33', "11) I'll be back soon. M___________ , why not get some rest?",
        '곧 돌아올게, 그동안 좀 쉬는 게 어때?', 'Meanwhile'
    ],
    [
        '33',
        "12) I'm very forgetful lately. My m___________ isn't what it used to be. ",
        '나는 최근에 잘 잊는다. 기억력이 예전 같지 않다.', 'memory'
    ],
    [
        '33', '13) I can still r___________ the first day we met. .',
        '나는 여전히 우리가 처음 만난 날을 기억할 수 있다.', 'remember'
    ],
    [
        '33',
        '14) M___________problems are often very difficult to deal with. ',
        '대개 정신적인 문제는 대처하기 매우 어렵다', 'Mental'
    ],
    [
        '33', '15) As I m___________ yesterday, the class was canceled. , .',
        '어제 얘기했던 것처럼, 그 수업은 취소 되었습니다.', 'mentioned'
    ],
    [
        '33',
        '16) Please r___________ me to call the airline to reconfirm my flight. ',
        '항공사에 전화해 비행편을 재확인하도록 저에게 상기시켜주세요', 'remind'
    ],
    [
        '33',
        '17) That picture r___________ me o___________ my childhood home. .',
        '그 사진은 나에게 어린 시절의 집을 생각나게한다.', 'reminds of'
    ], ['33', '18) No c___________ .', '아무것도 말하지 않겠습니다.', 'comment'],
    [
        '33', '19) The critics c___________ favorably on his new book. .',
        '비평가들은 그의 새 책에 대해 호의적으로는 논평했다.', 'commented'
    ],
    [
        '33', '20) We build m___________ in honor of great people. .',
        '우리는 위대한 사람들에게 경의를 표하기 위해 기념물을 세운다.', 'monuments'
    ],
    [
        '33',
        '21) We use TV m___________ to watch everyone who enters our bank. ',
        '우리는 은행에 들어오는 모든 사람들을 관찰하기 위해 모니터를 사용한다.', 'monitors'
    ],
    [
        '33', '22) The security guard is m___________ the crowd. .',
        '안전 요원이 사람들을 감시하고 있다.', 'monitoring'
    ],
    [
        '33', '23) I demanded that he be s___________ to court. ',
        '나는 그에게 법정에 출두할 것을 요구했다. ★', 'summoned'
    ],
    [
        '33', '24) The prosecutor has issued a s___________ to the suspect. .',
        '검사는 그 용의자에게 소환장을 발부했다.', 'summons'
    ], ['33', '25) international c___________', '국제무역', 'commerce'],
    [
        '33', '26) A street m___________ sold me this watch at a discount. .',
        '한 노점 상인이 내게 할인가로 이 시계를 팔았다.', 'merchant'
    ],
    [
        '33', '27) The judge often showed m___________ to young prisoners. .',
        '그 판사는 종종 어린 죄수들에게 자비를 보였다.', 'mercy'
    ],
    [
        '33',
        '28) They were lost at sea, at the m___________ of harsh weather. ',
        '그들은 바다에서 항로를 잃어, 거친 날씨에 내맡겨졌다.', 'mercy'
    ],
    [
        '33',
        '29) This lane is going to m___________ i___________ the one to the left. .',
        '이 도로는 왼쪽에 있는 도로로 합쳐질 것이다.', 'merge into'
    ],
    [
        '33',
        '30) It took some time for the whale to e___________ f___________ the water. .',
        '고래가 물 속에서 모습을 드러낼 때까지 시간이 좀 걸렸다.', 'emerge from'
    ],
    [
        '33', '31) How does a submarine s___________? ', '잠수함은 어떻게 잠수하나요?',
        'submerge'
    ],
    [
        '34', '1) Drastic m___________should be taken to prevent crime. . ',
        '범죄를 예방하기 위한 과감한 조치가 취해져야 한다. ', 'measures'
    ],
    [
        '34', '2) Do you know how to m___________ the amount of rainfall? ',
        '강우량을 어떻게 측정하는지 알고 있나요?', 'measure'
    ],
    [
        '34', '3) What are the d___________ of the package you want to ship? ',
        '보내시려는 소포의 크기가 어떻게 됩니까?', 'dimensions'
    ],
    [
        '34', '4) The fundraiser was an i___________ success. .',
        '기금 마련 행사는 대성공이었다.', 'immense'
    ],
    [
        '34',
        '5) The researchers are studying the seasonal m___________ of birds. .',
        '연구자들은 조류의 계절성 이동에 대해 연구하고 있다.', 'migration'
    ],
    [
        '34',
        '6) As a child, he i___________ to this country from Ireland. , .',
        '어릴 때, 그는 아일랜드에서 이 나라로 이민 왔다.', 'immigrated'
    ],
    [
        '34', '7) Korea had more e___________ than immigrants in the past. .',
        '과거에 한국은 이민 오는 사람보다 이민 가는 사람이 더 많았다.', 'emigrants'
    ], ['34', '8) a m___________ injury[wound] []', '가벼운 부상[상처]', 'minor'],
    [
        '34', '9) They were married by a local church m___________ . .',
        '그들은 지역 교회 목사님 앞에서 결혼했다.', 'minister'
    ],
    [
        '34',
        '10) People who a___________ justice and punishment need to be fair and objective. .',
        '법과 처벌을 집행하는 사람들은 공정하고 객관적일 필요가 있다.', 'administer'
    ],
    [
        '34', '11) This medicine should not be a___________ to children. .',
        '이 약은 아이들에게 투여되면 안 된다.', 'administered'
    ],
    [
        '34', '12) Their enthusiasm d___________ as the class got harder. , .',
        '수업이 어려워지면서, 그들의 열의도 줄어들었다.', 'diminished'
    ],
    [
        '34', '13) He is an e___________ professor of anatomy. .',
        '그는 해부학에서 저명한 교수이다.', 'eminent'
    ],
    [
        '34', '14) There are few signs that war is i___________ . ',
        '전쟁이 임박했다는 징후는 거의 없다.★', 'imminent'
    ],
    [
        '34',
        "15) Her family's support played a p___________ part in ger recovery. .",
        '가족들의 지지는 그녀의 회복에 중요한 역할을 했다.', 'prominent'
    ],
    [
        '34', '16) Is there a p___________ building nearby? ',
        '근처에 눈에 잘 띄는 건물 있어?', 'prominent'
    ],
    [
        '34', '17) Please keep your expenses to a m___________ . .',
        '지출을 최소화해주시기 바랍니다.', 'minimum'
    ], ['34', '18) m___________wage ', '최저임금', 'minimum'],
    [
        '34',
        '19) It was m___________ that the girl survived the accident and made such a miraculous recovery. .',
        '그 소녀가 그 사고에서 살아남아 기적적으로 회복한 것은 놀라운 일이었다.', 'miracle'
    ],
    [
        '34', '20) She is a___________ for her great musical talent. .',
        '그녀는 뛰어난 음악적 재능으로 존경받는다.', 'admired'
    ],
    [
        '34', '21) A: What a m___________ marble building! ',
        '정말 훌륭한 대리석 건물인데!', 'marvelous'
    ],
    [
        '35', '1) He officially a___________(to) his mistake later. .',
        '그는 나중에 공식적으로 자신의 실수를 인정했다.', 'admitted'
    ],
    [
        '35', '2) After c___________a crime, he was c___________to prison. ,',
        '범죄를 저지른 후, 그는 감옥에 보내졌다.★', 'committing, committed'
    ], ['35', '3) an executive c___________ ', '집행 위원회', 'committee'],
    [
        '35', '4) The c___________ is composed of ten members. ',
        '그 위원회는 10명의 위원들로 구성되어 있다.', 'committee'
    ],
    [
        '35', '5) Stars e___________ a lot of energy as visible light. .',
        '별들은 많은 에너지를 가시광선으로 방출한다.', 'emit'
    ],
    [
        '35', '6) Several names were o___________ from the list by mistake. .',
        '몇 명의 이름이 실수로 명단에서 누락되었다.', 'omitted'
    ],
    [
        '35', '7) Viewers are not p___________ to photograph anything. .',
        '관람객들에게는 어떠한 사진 촬영도 허용되지 않습니다.', 'permitted'
    ],
    [
        '35', '8) A: Did you s___________ your paper to the teacher?',
        '너는 숙제를 선생님께 제출했니?', 'submit'
    ],
    [
        '35', '9) How is power t___________ from the engine to the wheels? ',
        '동력이 엔진에서 바퀴로 어떻게 전달됩니까?', 'transmitted'
    ],
    [
        '35',
        '10) His m___________ was to spread Christianity in Africa, so he went there as a missionary. , .',
        '그의 사명은 아프리카에 기독교를 전파하는 것이었기에, 그는 그곳에 선교사로서 갔다.', 'mission'
    ],
    [
        '35',
        '11) The Chilean government sponsored a trade m___________ to Korea. .',
        '칠레 정부는 한국으로 가는 무역 사절단을 지원했다.', 'mission'
    ],
    [
        '35', '12) He gets a 10% c___________ on everything he sells. 10% .',
        '그는 자신이 판매하는 모든 것에 대해 10% 수수료를 받는다.', 'commission'
    ],
    [
        '35',
        '13) She warned her children not to m___________ u___________ the room. .',
        '그녀는 자녀들에게 방을 어지럽히지 말라고 주의를 주었다.', 'mess, up'
    ],
    [
        '35',
        '14) A m___________ amount of stress can improve your mental and physical health. ',
        '적당한 정도의 스트레스는 정신적, 신체적 건강을 증진해 줄 수 있다.', 'moderate'
    ],
    [
        '35', '15) This medicine will help to m___________ your pain. ',
        '이 약은 고통을 완화하는 데 도움이 될 것이다. ★', 'moderate'
    ],
    [
        '35', '16) He m___________ the old house for his parents. .',
        '그는 부모님을 위해 낡은 집을 현대식으로 만들었다.', 'modernized'
    ],
    [
        '35', '17) He is in the habit of being m___________ . .',
        '그는 겸손이 몸에 배어 있다.', 'modest'
    ],
    [
        '35',
        '18) The design is perfect; there is nothing to m___________ . . .',
        '그 디자인은 완벽하다. 수정할 것이 없다.', 'modify'
    ],
    [
        '35',
        '19) A: How many people can this conference room hold? B: It a___________ up to 600 people.',
        '이 회의실은 몇 명을 수용할 수 있습니까? 600명까지 수용합니다.', 'accommodates'
    ],
    [
        '35', '20) A: What c___________ do you deal in? ', '어떤 상품을 취급하십니까?',
        'commodities'
    ],
    [
        '35', '21) She made candles by pouring wax into a m___________ . .',
        '그녀는 틀에 왁스를 부어 양초를 만들었다.', 'mold'
    ],
    [
        '35', '22) Man is m___________ , but art is immortal. , .',
        '인간은 죽어도, 예술은 영원하다.', 'mortal'
    ],
    [
        '35', '23) We took out a m___________ to purchase our home. .',
        '우리는 주택을 구매하기 위해 대출을 받았다.', 'mortgage'
    ],
    [
        '35', '24) It turned out that the actor was m___________ . . ',
        '그 배우는 살해당한 것으로 밝혀졌다. ', 'murdered'
    ],
    [
        '36',
        '1) The subway was so crowded that I could hardly m___________. .',
        '지하철이 혼잡해서 거의 움직일 수 없었다.', 'move'
    ],
    [
        '36', '2) The audience was m___________ to tears. .',
        '관객은 감동해서 눈물을 흘렸다.', 'moved'
    ],
    [
        '36', "3) Police don't know the m___________ for the crime. .",
        '경찰은 그 범행의 동기를 알지 못한다.', 'motive'
    ],
    [
        '36', '4) The m___________ of the boat made Jake feel dizzy. ',
        '배의 움직임 때문에 는 어지러움을 느꼈다.', 'motion'
    ],
    [
        '36', '5) I had mixed e___________ about the news. .',
        '나는 그 소식에 복잡한 감정이 들었다.', 'emotions'
    ],
    [
        '36', '6) The activity p___________ team spirit among the students. .',
        '그 활동은 학생들 간의 협동심을 길러주었다.', 'promoted'
    ],
    [
        '36', '7) Susan was p___________ to a supervisor. .',
        '수잔은 총지배인으로 승진했다.', 'promoted'
    ], ['36', '8) a r___________ area ,', '외딴 지역,', 'remote'],
    [
        '36', '9) It was a m___________ to remember. .', '기억할 만한 순간이었다.',
        'moment'
    ],
    [
        '36', "10) I'm not busy at the m___________. .", '나는 지금 바쁘지 않다.',
        'moment'
    ], ['36', '11) a sense of c___________ ', '공동체 의식', 'community'],
    [
        '36',
        '12) There will be a bake sale at the c___________ center next Saturday. .',
        '다음주 토요일에 지역 공동체 센터에서 빵 세일이 있을 것이다.', 'community'
    ],
    [
        '36', '13) Without language, we could not c___________. ',
        '언어가 없다면, 우리는 의사소통을 할 수 없을 것이다.', 'communicate'
    ], ['36', '14) c___________ sense ', '일반 상식', 'common'],
    [
        '36', '15) We have a lot i___________ c___________. .', '우리는 공통점이 많다.',
        'in common'
    ],
    [
        '36',
        "16) It's important to try to consider the other party's feelings when developing m___________ understanding. ",
        '상호 이해를 발전시킬 때에는 다른 쫏의 입장을 고려하려는 노력이 중요하다', 'mutual'
    ],
    [
        '36', '17) She c___________ from Suwon to Seoul every day. ',
        '그녀는 매일 수원에서 서울로 통근[통학]한다.', 'commutes'
    ],
    [
        '36', '18) She is a n___________ speaker of English. .',
        '그녀는 영어를 모국어로 하는 사람이다.', 'native'
    ],
    [
        '36', '19) We live in a divided n___________. .', '우리는 분단국가에 산다.',
        'nation'
    ],
    [
        '36', '20) Soccer brought our n___________ together at that time. .',
        '그 당시에 축구는 전 국민을 하나로 묶어 주었다.', 'nation'
    ],
    ['36', '21) n___________ conservation[preservation] ', '자연 보호', 'nature'],
    [
        '36', '22) He‘s a gentle person by n___________. .',
        '그는 천성적으로 친절한 사람이다.', 'nature'
    ],
    [
        '36', '23) My sister has an i___________ talent for drawing .',
        '내 여동생은 그림 그리기에 천부적인 재능이 있다.', 'innate'
    ],
    [
        '36', '24) We received a n___________reply to our offer. .',
        '우리는 우리의 제안에 대해 부정적인 답변을 받았다.', 'negative'
    ],
    [
        '36', '25) The results of the test were n___________ [positive]. ',
        '검사 결과는 음성[양성]입니다. ★', 'negative'
    ],
    [
        '36', '26) Bruce d___________ that he wrote the report. .',
        '브루스는 자신이 그 보고서를 썼다는 것을 부인했다.', 'denied'
    ],
    [
        '36', '27) I want to remain n___________. .', '나는 중립을 지키고 싶다.',
        'neutral'
    ],
    [
        '36', '28) Switzerland is a n___________ country. .', '스위스는 중립국이다.',
        'neutral'
    ], ['36', '29) n___________ life ,', '평범한 삶,', 'normal'],
    [
        '36',
        '30) E___________ mistakes are often caused by missing a tiny point. . ',
        '막대한 실수들은 작은 것을 놓치는 것에 기인한다. ', 'Enormous'
    ],
    [
        '37',
        "1) Richard Porson, one of Britain's most n___________ classical scholars, was born on Christmas day in 1759. Richard Porson 1759 .",
        '1759. 영국의 가장 주목할 만한 고전학자 중 한 사람인 은 1759년 크리스마스에 태어났다.', 'notable'
    ],
    [
        '37',
        '2) After I bought the skirt, I n___________ it had a stain. , .',
        '그 치마를 사고난 후에야, 얼룩이 있는 걸 알았다.', 'notice'
    ],
    [
        '37',
        "3) Don't t___________ any n___________ o___________ what they're saying about you. .",
        '그들이 너에 대해 하는 말은 신경 쓰지 마라.', 'take, notice of'
    ],
    [
        '37', '4) They n___________ his family o___________ his death. .',
        '그들은 그의 죽음을 가족에게 알렸다.', 'notified, of'
    ],
    [
        '37',
        '5) All new ideas come from combining existing n___________ in creative ways. .',
        '모든 새로운 아이디어는 기존의관념들을 창의적인 방법으로 결합하는 데에서 온다.', 'notions'
    ],
    [
        '37', '6) Have the winners been a___________? ?', '수상자가 발표되었습니까?',
        'announced'
    ],
    [
        '37', "7) The 'b' in 'debt' is not p___________. ",
        '‘debt’에서 ‘b’는 발음되지 않는다. ', 'pronounced'
    ],
    [
        '37', '8) The doctor p___________ him brain-dead. . ★',
        '의사는 그에게 뇌사판정을 내렸다. ★', 'pronounced'
    ],
    [
        '37', "9) It's a n___________ approach to the problem. .",
        '그 문제에 대한 새로운 접근이군요.', 'novel'
    ],
    [
        '37',
        '10) You have to challenge the conventional ways of doing things and search for opportunities to i___________. .',
        '당신은 일을 할 때 관습적인 방법에 이의를 제기하고 혁신할 기회를 찾아야한다.', 'innovate'
    ],
    [
        '37', "11) Don't neglect to r___________ your license. .",
        '면허증을 갱신하는 것을 잊지 말아라.', 'renew'
    ],
    [
        '37',
        '12) You should use a letter, a n___________, and a special character in your password.',
        '비밀번호에는 문자, 숫자, 특수문자를 사용해야합나다.', 'numeral'
    ],
    [
        '37', '13) The human body contains n___________ types of cells. .',
        '인간의 몸은 많은 종류의 세포를 포함하고 있다.', 'numerous'
    ],
    [
        '37', '14) There are i___________ species of fish in the ocean. ',
        '바다에는 셀 수 없이 많은 종의 물고기가 있다. ★', 'innumerable'
    ],
    [
        '37',
        '15) The body requires proper n___________ to maintain itself. .',
        '신체를 유지하기 위해서는 적절한 영양분이 필요하다.', 'nutrition'
    ], ['37', '16) a well-n___________ baby ', '영양 상태가 좋은 아기', 'nourished'],
    [
        '37', "17) She n___________ the students' artistic talent. .",
        '그녀는 학생들의 예술적 재능을 육성한다.', 'nourishes'
    ],
    [
        '37',
        '18) Who n___________ Evan through the worst of the illness? Evan ?',
        '이 가장 아플 때 누가 간호했나요?', 'nursed'
    ],
    [
        '37',
        '19) The interaction between nature and n___________ is highly complex. . ★',
        '천성과 양육 사이의 상호작용은 매우 복잡하다. ★', 'nurture'
    ],
    [
        '37', '20) The m___________ of the song still rings in my ears. .',
        '그 노래의 멜로디가 아직도 귓가에 선하다.', 'melody'
    ],
    [
        '37', '21) It was a t___________ he died so young. .',
        '그가 그렇게 어린 나이에 죽은 것은 비극이었다.', 'tragedy'
    ],
    [
        '37', '22) The machine is not o___________ properly. .',
        '그 기계는 제대로 작동하고 있지 않다.', 'operating'
    ],
    [
        '37', '23) The doctor decided to o___________ at once. ,',
        '그 의사는 당장 수술하기로 결정했다,', 'operate'
    ],
    [
        '37', '24) Learn how to c___________ with team members. .',
        '너는 팀원들과 협동하는 법을 배워야 한다.', 'cooperate'
    ],
    [
        '37', '25) I have no o___________ but to do it. .',
        '그것을 하는 것 외에는 선택의 여지가 없다.', 'option'
    ],
    [
        '37',
        '26) Consider a___________ a pet with medical or behavioral needs. .',
        '의료적 또는 행동적 도움이 필요한 반려동물의 입양을 고려해주세요.', 'adopting'
    ],
    [
        '37', '27) The school a___________ a new method of teaching. .',
        '그 학교는 새로운 교수법을 채택했다.', 'adopted'
    ],
    [
        '37', '28) Public o___________ is against[with] him. []. ',
        '여론은 그에게 불리하다[유리하다]. ', 'opinion'
    ],
    [
        '38', '1) The movie is about o___________ people like you and me. .',
        '그 영화는 당신과 나 같은 평범한 사람들의 이야기이다.', 'ordinary'
    ],
    [
        '38',
        "2) In the army, Jack was s___________ to Tom, but at work, Jack is Tom's superior. ★ , .",
        '군대에서 잭은 톰의 부하였지만, 직장에서는 잭이 톰의 상사이다.', 'subordinate, subordinate'
    ],
    [
        '38',
        '3) The manager needs to c___________ the work for her staff. . ★',
        '관리자는 직원들을 위해 일을 조직화해야 한다. ★', 'coordinate'
    ], ['38', '4) the o___________ of civilization ', '문명의 기원', 'origins'],
    [
        '38', '5) Their supervisor is a very detail-o___________ person. . ★',
        '그들의 감독관은 매우 세부 지향적인 사람이다. ★', 'oriented'
    ],
    [
        '38', "6) He didn't p___________ enough for the exam. .",
        '그는 시험에 충분한 대비를 하지 않았다.', 'prepare'
    ],
    [
        '38', '7) Do you know how to operate this heating a___________? ?',
        '이 난방장치를 작동시키는 법을 아십니까?', 'apparatus'
    ],
    [
        '38', "8) Carla said she'd r___________ the oven today.",
        'Carla는 오늘 오븐을 고칠 것이라고 말했다.', 'repair'
    ],
    [
        '38',
        '9) The new manager had to put signification time and effort into the r___________ and maintenance of the machines. .',
        '새 매니저는 그 기계를 유지 및 보수하는데 상당한 시간과 노력을 들여야했따.', 'repair'
    ],
    [
        '38',
        '10) Augustus was the first Roman e___________ to be called "Caesar." ‘’ .',
        '아우구스투스는 ‘시저’라고 불린 최초의 로마 황제였다.', 'emperor'
    ], ['38', '11) the i___________ family ', '황족', 'imperial'],
    [
        '38',
        '12) The workers installed panels of t___________ glass around the hocky rink. .',
        '인부들은 하키 링크 주변에 투명한 유리판을 설지했다.', 'transparent'
    ],
    [
        '38',
        '13) Teachers should always make their expectations t___________ to their students. ★ .',
        '교사들은 항상 그들의 기대 사항을 학생들에게 명쾌하게 해주어야 한다.', 'transparent'
    ],
    [
        '38', '14) The baby cried for no a___________ reason. .',
        '그 아기는 특별한 이유 없이 울었다.', 'apparent'
    ],
    [
        '38', '15) It a___________ that your computer has a virus. .',
        '너의 컴퓨터는 바이러스에 걸린 것 같다.', 'appears'
    ],
    [
        '38', '16) Everything a___________ to be normal. .', '모든 것이 정상으로 보였다.',
        'appears'
    ],
    [
        '38', '17) She is currently a___________ in a popular TV drama. .',
        '그녀는 현재 인기 드라마에 출연 중이다.', 'appearing'
    ],
    [
        '38',
        '18) The researchers c___________ the new data w___________ the findings of prior studies. .',
        '연구원들은 새로운 데이터를 이전 연구에서 발견된 것들과 비교했다.', 'compared with'
    ],
    [
        '38',
        '19) What she said is nothing c___________ t___________ what she did. .',
        '그녀가 한 말은 그녀가 한 행동에 비하면 아무것도 아니다.', 'compared to'
    ],
    [
        '38', '20) Life is often c___________ t___________ a voyage. .',
        '인생은 종종 항해에 비유된다.', 'compared to'
    ],
    [
        '38', '21) He has no p___________ when it comes to originality. .',
        '독창성에서라면 그에 필적하는 사람은 없다.', 'peers'
    ],
    [
        '38',
        '22) She p___________ through the window to get a look at him. .',
        '그녀는 그를 보기 위해 창문 너머로 자세히 들여다보았다.', 'peered'
    ],
    [
        '38', '23) The event was a p___________ success. .',
        '그 행사는 부분적으로 성공했다.', 'partial'
    ],
    [
        '38', '24) A judge should not be p___________. . ★',
        '심판은 편파적이어서는 안 된다. ★', 'partial'
    ],
    [
        '38', "25) There wasn't a p___________ of truth in what he said. . ★",
        '그가 한 말에는 진실이라고는 티끌만큼도 없었다. ★', 'particle'
    ],
    [
        '38', '26) I have no p___________ plan. .', '특별한 계획은 없습니다.',
        'particular'
    ],
    [
        '38', '27) Do you live a___________ from your parents? ?',
        '당신은 부모님과 떨어져 삽니까?', 'apart'
    ],
    [
        '38', '28) Their relationship fell a___________. .', '그들의 관계는 깨졌다.',
        'apart'
    ],
    [
        '38', '29) A p___________ of the money went to charity. .',
        '그 돈의 일부는 자선단체에 기부되었다.', 'portion'
    ],
    [
        '38', '30) The p___________ at this restaurant are small. . ★',
        '이 레스토랑은 음식량이 적다. ★', 'portions'
    ],
    [
        '38',
        '31) I___________ p___________ t___________ her salary, Lynn spends a lot on clothes. ',
        'Lynn은 자기 월급에 비해서 옷에 많은 돈을 쓴다.', 'In proportion to'
    ], ['38', '32) a sense of p___________ ', '균형 감각', 'proportion'],
    ['39', '1) a p___________ of the Bible ', '성경의 한 구절', 'passage'],
    [
        '39', '2) With the p___________ of years, she grew wiser. , .',
        '수년이 지나면서, 그녀는 더욱 지혜로워졌다.', 'passage'
    ],
    [
        '39', '3) The driver stopped to pick up more p___________. .',
        '기사는 더 많은 승객을 태우기 위해 멈추었다.', 'passengers'
    ],
    [
        '39', '4) Ask a p___________ where the nearest gas station is. .',
        '가까운 주유소가 어디인지 지나가는 사람에게 물어봐.', 'passerby'
    ],
    [
        '39', '5) Walking my dog is one of my favorite p___________. . ★',
        '개 산책은 내가 좋아하는 여가 활동 중 하나이다. ★', 'pastimes'
    ],
    [
        '39',
        '6) Nobody could s___________ her at swimming. She would always outdo others and win the race. .',
        '아무도 수영에서 그녀를 능가할 수가 없었다 그녀는 항상 남들보다 잘해 경기를 이기곤 했다.', 'surpass'
    ],
    [
        '39',
        "7) Your p___________ is so fast that I can't k___________ p___________ w___________ you. .",
        '네 걸음이 너무 빨라 너와 보조를 맞출 수 없다.', 'pace, keep pace with'
    ],
    [
        '39', "8) Don't make p___________ excuses. . ★", '한심한 변명 늘어놓지 말아라. ★',
        'pathetic'
    ],
    [
        '39', '9) The sick and hungry children were a p___________ sight. . ★',
        '아프고 굶주리는 아이들을 보는 것은 가슴이 아팠다. ★', 'pathetic'
    ],
    [
        '39', '10) There is a growing mutual a___________ between them. . ★',
        '그들 사이에는자 라나는 상호적 반감이 있다. ★', 'antipathy'
    ],
    [
        '39', '11) E___________ creates a closeness between people. . ★',
        '공감은 사람들 사이에서 친밀감을 형성한다. ★', 'Empathy'
    ],
    [
        '39', '12) I feel a deep s___________ for the abandoned animals. . ★',
        '나는 버려진 동물들에게 깊은 동정심을 느낀다. ★', 'sympathy'
    ],
    [
        '39',
        '13) The nurses moved the p___________ into the operating room. .',
        '간호사는그 환자를 수술실로 옮겼다.', 'patient'
    ],
    [
        '39', '14) A : How can you be so p___________ with her? ?',
        '너는 어떻게 그녀에 대해 그렇게 잘 참을 수 있니?', 'patient, patience'
    ],
    [
        '39',
        '15) The professor had a burning p___________ for his subject. () .',
        '그 교수는 자신의 (연구)주제에 대한 불타는 열정이 있었다.', 'passion'
    ],
    [
        '39', '16) He felt c___________ for those in poverty. . ★',
        '그는 가난한 사람들에게 연민의 정을 느꼈다. ★', 'compassion'
    ],
    [
        '39',
        '17) He is a p___________ who wants a better future for his country. . ★',
        '나라의 더 나은 미래를 바라는 애국자이다. ★', 'patriot'
    ],
    [
        '39',
        '18) Many artists were economically dependent on their p___________. .',
        '많은 예술가들이 그들의 후원자들에게 경제적으로 의존했다.', 'patrons'
    ],
    [
        '39',
        '19) The scientists conducted studies on p___________ of behavior in social media. .',
        '과학자들은 소셜 미디어에서의 행동 양식에 대한 연구를 실시했다.', 'patterns'
    ],
    [
        '39', '20) His closet was full of ties with different p___________. .',
        '그의 옷장은 다양한 무늬의 넥타이로 가득했다.', 'patterns'
    ],
    [
        '39', '21) Be sure to watch out for p___________ when you drive. . ★',
        '운전할 때 보행자들을 조심하는 것을 명심해라. ★', 'pedestrians'
    ],
    [
        '39', '22) a p___________ walkway[crossing] []', '인도[횡단보도]',
        'pedestrian'
    ],
    [
        '39',
        '23) Ben was anxious about his e___________ into the Amazon rainforest. Ben .',
        'Ben은 아마존 우림으로의 탐험을 열망했다.', 'expedition'
    ],
    [
        '39',
        '24) He was c___________ t___________ r___________ due to his legal problems. .',
        '그는 법적 문제로 사퇴해야만 했다.', 'compelled to resign'
    ],
    [
        '39',
        '25) The troublemaking student was e___________ from school. . ★',
        '그 문제 학생은 학교에서 퇴학당했다. ★', 'expelled'
    ],
    [
        '39', '26) We a___________ to him for help. .', '우리는 그에게 도움을 호소했다.',
        'appealed'
    ],
    [
        '39', '27) The movie a___________ t___________ all ages. .',
        '그 영화는 모든 연령의 흥미를 끌고 있다.', 'appeals to'
    ],
    [
        '39', '28) The lawyer will a___________ the case. .',
        '그 변호사는 그 사건을 항소할 것이다.', 'appeal'
    ],
    [
        '39',
        '29) You ought to p___________ your dress shoes before the interview. ',
        '면접 전에 정장에 신을 구두를 닦아야 해', 'polish'
    ],
    [
        '39',
        '30) The young musician has a lot of natural talent, but he still needs to p___________ his skills. ★ , .',
        '그 어린 음악가는 천성적인 재능을 많이 가졌지만, 여전히 기술을 연마할 필요가 있다.', 'polish'
    ], ['39', '31) nail p___________ ', '매니큐어', 'polish'],
    [
        '39',
        "31) Emmet is finished building the chair, but he hasn't put any p___________ on it yet.",
        'Emmet은 의자를 다 만들었지만 아직 위에 광택제를 바르지 않았다. ', 'polish'
    ],
    [
        '39', '32) She buy things o___________ i___________. . ★',
        '그녀는 충동적으로 물건을 산다. ★', 'on impulse'
    ],
    [
        '39',
        '33) the death p___________ , He paid a p___________ for not wearing a seatbelt. .',
        '사형, 그는 안전벨트 미착용으로 벌금을 냈다.', 'penalty'
    ],
    [
        '39', '34) He was p___________ for breaking the law. .',
        '그는 법을 위반하여 처벌받았다.', 'punished'
    ],
    [
        '40', '1) Your happiness d___________ o___________ how you think, .',
        '너의 행복은 네가 어떻게 생각하는가에 달려 있다.', 'depends on'
    ],
    [
        '40',
        '2) The following flights will be s___________ until further notice. .★',
        '다음 비행기들은 추후 공고가 있을 때까지 운항이 잠시 중단됩니다.★', 'suspended'
    ],
    [
        '40', '3) The employee was s___________ without pay. .',
        '그 종업원은 무임금 정직 처분을 받았다.', 'suspended'
    ],
    [
        '40',
        '4) Do not e___________ too much time and energy on a little thing. ',
        '작은 일에 너무 많은 시간과 에너지를 들이지마', 'expend'
    ],
    [
        '40',
        '5) Nothing can c___________ f___________ losing my husband. . ★',
        '어떤 것도 내 남편을 잃은 것을 보상할 수 없다. ★', 'compensate for'
    ],
    [
        '40', '6) She lives on a p___________ now, . ★',
        '그녀는 지금 연금으로 생활하고 있다. ★', 'pension'
    ],
    [
        '40', '7) Let me p___________ over it a little longer. .',
        '그것에 대해 조금만 더 생각하게 해주세요.', 'ponder'
    ],
    [
        '40', '8) She has e___________ in public relations. .',
        '그녀는 홍보 일에 경험이 있다.', 'experience'
    ],
    [
        '40', '9) Is it right to e___________ on animals? ?',
        '동물을 대상으로 실험하는 것은 옳은 일인가?', 'experiment'
    ],
    [
        '40', '10) Talk to an e___________ before making a decision. .',
        '결정을 내리기 전에 전문가와 이야기해라.', 'expert'
    ],
    [
        '40', '11) Enter that area a___________ y___________ p___________. .',
        '위험을 각오하고 그 지역에 들어가시오.', 'at your peril'
    ],
    [
        '40', '12) You will c___________ against the best players. .',
        '너는 최고의 선수들과 경쟁하게 될 것이다.', 'compete'
    ],
    [
        '40', '13) Her c___________ as a designer is not in question. .',
        '디자이너로서의 그녀의 능력은 의심의 여지가 없다.', 'competence'
    ],
    [
        '40',
        '14) The organization brought a p___________ against the restrictions to the city council. ★ .',
        '그 단체는 규제에 반대하는 탄원서를 시 의회에 가져갔다.', 'petition'
    ],
    [
        '40', "15) I've lost my a___________ lately. .", '나는 요즘 식욕을 잃었다.',
        'appetite'
    ],
    [
        '40', "16) I'm sorry, could you r___________ that? , ?",
        '미안하지만, 다시 한번 말씀해 주시겠습니까?', 'repeat'
    ],
    [
        '40', '17) His mother e___________ the importance of good manners. .',
        '그의 어머니는 올바른 예절의 중요성을 강조했다.', 'emphasized'
    ],
    [
        '40',
        '18) The first p___________ of the experiment has been completed. .',
        '실험의 첫 번째 단계가 완료되었다.', 'phase'
    ],
    [
        '40',
        '19) The new standard will be p___________ in over the next several years. .★',
        '새로운 기준이 향후 몇 년에 걸쳐 단계적으로 시행될 것이다.★', 'phased'
    ],
    [
        '40',
        '20) An aurora is a commonly photographed natural p___________. .',
        '오로라는 흔히 사진에 포착되는 자연 현상이다.', 'phenomenon'
    ],
    [
        '40',
        "21) A : Is this dress too f___________? ? B : No, it's perfect for a f___________ club , .",
        '이 드레스 너무 화려하니? 아니야, 고급 클럽에 딱 어울려.', 'fancy, fancy'
    ],
    [
        '40', '22) Do you f___________ a walk in the park? ?',
        '공원에서 산책하는 것을 좋아하니?', 'fancy'
    ],
    [
        '41', '1). A: Why do you keep a___________such a bad play? ?',
        '너는 이렇게 형편없는 연극에 왜 계속 박수를 치는 거야?', 'applauding'
    ],
    [
        '41', '2). The bomb e___________ with a terrible force. .',
        '그 폭탄은 엄청난 위력으로 폭발했다.', 'exploded'
    ],
    ['41', '3). a c___________ success[failure] []', '완전한 성공[실패]', 'complete'],
    [
        '41', '4). The reconstruction work will be c___________ next year. .',
        '복원공사는 내년에 완공될 예정이다.', 'completed'
    ],
    [
        '41',
        '5). A skilled chef knows how to choose ingredients that c___________ each other. .',
        '숙련된 요리사는 서로 보완하는 재료를 고르는 법은 안다.', 'complement'
    ], ['41', '6). farming i___________ ', '농기구', 'implements'],
    [
        '41', '7). The new rules will be i___________next month. . ★',
        '새 규칙은 다음 달에 시행될 것입니다. ★', 'implemented'
    ],
    [
        '41', '8). Thank you for your c___________. . ★', '칭찬의 말씀 감사합니다. ★',
        'compliment'
    ],
    [
        '41', '9). A lazy man can never a___________ anything. .',
        '게으른 사람은 결코 아무것도 성취할 수 없다.', 'accomplish'
    ], ['41', '10). s___________ and demand ', '공급과 수요', 'supply'],
    [
        '41',
        '11) They s___________ the victims w___________ food and clothing. .',
        '그들은 피해자들에게 음식과 옷을 공급했다.', 'supplied, with'
    ],
    [
        '41', '12) This job requires p___________ o___________ hard work. .',
        '이 일은 많은 노력을 필요로 한다.', 'plenty of'
    ],
    [
        '41',
        '13) People can gain satisfaction when they notice that their presence p___________ other people. .',
        '사람들은 자신의 존재가 다른 사람들을 기쁘게 한다는 것을 알게 되면 만족감을 얻을 수 있다.', 'pleases'
    ],
    [
        '41', '14). I p___________ w___________ her not to leave me. .',
        '나는 그녀에게 떠나지 말라고 애원했다.', 'pleaded with'
    ],
    [
        '41', '15). He p___________ innocent to the charges. . ★',
        '그는 그 혐의에 대해 무죄를 주장했다. ★', 'pleaded'
    ],
    [
        '41', '16) Your comments have only c___________ the situation. .',
        '너의 말은 상황을 복잡하게 만들 뿐이었다.', 'complicated'
    ],
    [
        '41', '17). The instructions were too c___________ for me. .',
        '그 지시문은 나에게 너무 복잡했다.', 'complicated'
    ],
    [
        '41', '18). His style is characterized by s___________. .',
        '그의 문체는 간결함으로 특징지어진다.', 'simplicity'
    ],
    [
        '41', '19). My feelings for him are c___________. .',
        '그에 대한 내 감정은 복잡하다.', 'complex'
    ],
    [
        '41', '20). We were p___________ by the complicated puzzle. .',
        '우리는 복잡한 퍼즐 때문에 당황했다.', 'perplexed'
    ],
    [
        '41',
        '21). Are you i___________ that he is not competent enough for the job? ?',
        '그가 그 일을 하기에 충분한 능력이 없다는 말씀이십니까?', 'implying'
    ],
    [
        '41', '22). His silence i___________ that he agrees. .',
        '그의 침묵은 그가 동의한다는 것을 암시한다.', 'implies'
    ],
    [
        '41',
        '23). If you want to a___________ f___________ the job, you must first get an application form from the company. , .',
        '네가 그 일자리에 지원하고자 한다면, 우선 그 회시로부터 지원서를 받아야 한다.', 'apply for'
    ],
    [
        '41',
        '24). The ban on smoking has a___________ t___________ restaurants and bars. () . ★',
        '금연(정책)은 식당과 술집에 적용되었다. ★', 'applied to'
    ],
    [
        '41',
        '25). The two countries established d___________ relations in 1962. ',
        '두 나라는 1962년 수교했다.', 'diplomatic'
    ],
    [
        '41',
        "26). Employers are reducing their staff, and they're not e___________ any new people. , .",
        '고용주들이 직원을 줄이면서, 새로운 사람들을 고용하지는 않고 있다.', 'employing'
    ],
    [
        '41', '27). The company was sued for e___________ its workers.. . ★',
        '그 회사는 근로자들을 착취한 것으로 고소당했다. ★', 'exploiting'
    ],
    [
        '41',
        '28). An expedition has been organized to e___________ the Antarctic. . ',
        '남극을 탐험하기 위해 탐험대가 조직되었다. ', 'explore'
    ],
    [
        '41',
        '29). Humans have yet to fully e___________ the depths of the ocean. . ',
        '인간은 아직 심해를 완전히 탐구하지 못했다. ', 'explore'
    ],
    [
        '42', '1). The nation is having p___________ difficulties. .',
        '그 나라는 정치적인 어려움을 겪고 있어.', 'political, politicians'
    ], ['42', '2). diplomatic[foreign] p___________ ', '외교 정책', 'policy'],
    [
        '42', '3). The department store has a strict return p___________. .',
        '그 백화점은 엄격한 환불 정책이 있다.', 'policy'
    ],
    [
        '42', '4). Seoul is a highly populated m___________. . ★',
        '서울은 인구밀도가 매우 높은 대도시이다. ★', 'metropolis'
    ], ['42', '5). a p___________ song ', '유행가', 'popular'],
    [
        '42',
        '6). This lecture focuses on arts, media and p___________ culture. , .',
        '이 강의는 예술과 매체, 대중문화를 중심으로 한다.', 'popular'
    ], ['42', '7). a densely p___________ area ', '인구 밀집 지역', 'populated'],
    ['42', '8). p___________ education ', '공교육', 'public'],
    [
        '42',
        "9). That's something you should say in private, not in p___________. ",
        '그것은 공적이 아니라 사적으로 말해야 하는 것이다.', 'public'
    ],
    [
        '42',
        "10). Richard Bolles' best selling job search book was first p___________ in 1970. Richcard Bolles 1970 .",
        'Richard의 가장 잘 팔리는 직업 찾기 책은 1970년에 처음 출판되었다.', 'published'
    ],
    [
        '42', '11). The election results will be p___________ soon. ',
        '선거 결과가 곧 발표될 것이다.', 'published'
    ],
    [
        '42', '12). Switzerland is one of the oldest surviving r___________. ',
        '스위스는 현존하는 가장 오래된 공화국 중의 하나이다.', 'republics'
    ],
    [
        '42',
        '13). The economic policy of the government encourages e___________ and discourages imports. ',
        '정부의 경제 정책은 수출을 장려하고 수입을 억제한다.', 'exports'
    ],
    [
        '42',
        '14). If we i___________ more than we can export, our economy will be in trouble. ',
        '수출보다 수입을 더 많이 한다면, 우리 경제는 곤경에 처할 것이다.', 'import'
    ],
    [
        '42', '15). i___________ restriction[control/regulation] ', '수입 규제',
        'import'
    ],
    [
        '42',
        '16). They were able to t___________ many heavy goods because of the new t___________ system. ',
        '새로운 운송 체계 덕분에 그들은 많은 무거운 상품들을 수송할 수 있었다.', 'transport, transportation'
    ],
    [
        '42',
        '17). I asked Jeff to bring his p___________ speaker, so we can play music at the party. Jeff ',
        '나는 파티에서 음악을 틀 수 있도록 에게 휴대용 스피커를 가져와 달라고 부탁했다.', 'portable'
    ], ['42', '18). equal education o___________ ', '균등한 교육기회', 'opportunity'],
    [
        '42', "19). You'll regret it if you don't take this o___________. ",
        '이 기회를 잡지 못한다면 너는 후회하게 될 것이다.', 'opportunity'
    ],
    [
        '42', '20). After the wedding, we all p___________ for a photograph. ',
        '결혼식 후에, 우리 모두는 사진을 찍기 위해 포즈를 취했다.', 'posed'
    ],
    [
        '42',
        '21) I was offered a p___________ at an engineering firm last week. ',
        '나는 지난주에 엔지니어링 회사에서 일자리를 제안받았다.', 'position'
    ],
    [
        '42', '22) Global P___________ System(GPS) ', '위성 위치 확인 시스템',
        'Positioning'
    ],
    [
        '42',
        '23). You always tend to be negative. Please try to be more p___________. . ',
        '너는 부정적인 경향이 있어. 좀 더 긍정적이 되도록 노력해 봐.', 'positive'
    ],
    [
        '42',
        "24) There's an advertisement for tutoring services p___________ on the bulletin board. .",
        '과외 교습에 대한 광고가 게시판에 붙어있다.', 'posted'
    ],
    [
        '42',
        '25) All winning entries will be p___________ on the official website. .',
        '수장작들은 모두 공식 웹사이트에 게시될 것입니다.', 'posted'
    ],
    [
        '42',
        '26). You have to pay a d___________ to use a locker for a day. ',
        '하루 동안 보관함을 사용하려면 보증금을 내야 합니다. ★', 'deposit'
    ], ['42', '27). a savings d___________ ', '저축 예금', 'deposit'],
    [
        '42',
        "28). Please d___________ your valuables in the hotel's safety d___________ box. ",
        '귀중품은 호텔의 귀중품 보관함에 넣어 두도록 하세요.★', 'deposit, deposit'
    ],
    [
        '42',
        '29). In order to protect domestic industry, very high tariffs are sometimes i___________ o___________ some imports. .',
        '국내 산업을 보호하기 위해 때때로 매우 높은 관세가 일부 수입품에 부과된다.', 'imposed on'
    ],
    [
        '42',
        '30). The main p___________ of the meeting was to gather useful information. .',
        '그 회의의 주요 목적은 유용한 정보를 수집하는 것이었다.', 'purpose'
    ],
    [
        '42', '31). Did he break it by accident? ', '그가 그것을 우연히 깬 거야?',
        'on purpose'
    ],
    [
        '42',
        '32). He w___________ o___________ t___________ the idea because it could have the opposite effects. .',
        '역효과가 있을 수 있기 때문에 그는 그 생각에 반대했다.', 'was opposed to,'
    ],
    [
        '42',
        "33). A: S___________ you were offered the job ― would you accept? . ? B: I don't think so. I'm s___________ t___________ t___________ another one. . .",
        '만약 네가 그 일을 제의받는다고 생각해 봐. 받아들일 거야? 그러지 않을 것 같아. 나는 다른 일을 맡기로 되어 있어.',
        'Suppose, supposed to'
    ],
    [
        '42', '34). Trust is a fundamental c___________ of a good marriage. .',
        '신뢰는 훌륭한 결혼 생활의 중요한 요소이다.', 'component'
    ],
    [
        '42', '35). She has a distinct advantage over her o___________. .',
        '그녀는 상대에 비해 뚜렷한 강점이 있다.', 'opponent'
    ],
    [
        '42',
        '36). It was a problem c___________ of lazinees and wasteful spending. .',
        '이는 게으름과 낭비벽이 혼합된 문제였다.', 'compounded'
    ],
    [
        '42',
        '37). Our economic difficulties have been c___________ by soaring oil prices. ',
        '우리의 경제적 어려움은 치솟는 유가로 더욱 악화되었다.★', 'compounded'
    ],
    [
        '43',
        '1). A: Do you think there is a p___________ of life on Mars? B: Yes, I think it is p___________. ',
        '화성에 생명체가 있을 가능성이 있다고 생각하니?', 'possibility, possible'
    ],
    [
        '43', '2). They p___________ a great fortune. .',
        '그들은 많은 재산을 소유하고 있다.', 'possess'
    ],
    [
        '43', '3). Be aware of p___________ problems. .',
        '잠재적인 문제점들을 인식하고 있어라.', 'potential'
    ],
    [
        '43', '4). Many people never achieve their full p___________. .',
        '많은 사람들은 자신의 잠재력을 최대한 발휘하지 못한다.', 'potential'
    ],
    [
        '43', '5). Nothing is so p___________ as time. .', '시간만큼 소중한 것은 없다.',
        'precious'
    ],
    [
        '43', '6). I a___________ your kindness. .', '당신의 친절에 감사드립니다.',
        'appreciate'
    ],
    [
        '43', '7). His works were not a___________ until after his death. ',
        '그의 작품들은 그가 죽은 후에야 비로소 그 진가를 인정받았다.★', 'appreciated'
    ],
    [
        '43',
        '8). Children respond best when p___________ rather than criticized. .',
        '아이들은 꾸중을 들을 때보다 칭찬받을 때 말을 가장 잘 듣는다.', 'praised'
    ],
    [
        '43', '9). Love is a p___________ thing. .', '사랑은 값을 매길 수 없는 귀중한 것이다.',
        'priceless'
    ],
    [
        '43',
        "10). Though he has a comprehensive grasp of English grammar, he can't c___________ this simple sentence. ★ , .",
        '그는 영문법을 포괄적으로 이해하고 있음에도, 이 간단한 문장의 뜻은 파악할 수 없다.', 'comprehend'
    ],
    [
        '43', '11). The bank robber was sent to p___________ for ten years. ',
        '그 은행 강도는 10년 동안 수감되었다.', 'prison'
    ],
    [
        '43', '12). He was sentenced to be i___________ for life. .',
        '그는 종신형을 선고받았다.', 'imprisoned'
    ],
    [
        '43',
        '13). Because its directors were e___________, the company became the largest e___________ of its kind. ',
        '.회사의 중역들이 진취적이었기 때문에, 그 회사는 동종업계에서 가장 큰 기업이 되었다.',
        'enterprising, enterprise'
    ],
    [
        '43', '14). He continuously s___________ me. .', '그는 끊임없이 나를 놀라게 한다.',
        'surprises'
    ],
    [
        '43',
        "15). I didn't anticipate the offer, but it was a welcome s___________. .",
        '나는 그 제안을 예상하진 못했지만 그것은 반가운 놀람이었다.', 'surprising'
    ],
    [
        '43',
        '16). Parents worry that their children will f___________ p___________ t___________ the influence of bad students. ',
        '부모들은 그들의 자녀가 불량 학생들의 영향의 희생양이 될까 봐 걱정한다.', 'fall prey to'
    ],
    [
        '43',
        '17). The strong p___________ of competition forced companies to innovate. . ',
        '경쟁에 대한 강한 압박으로 회사들은 변화해야만 했다. ', 'pressure'
    ], ['43', '18). high blood p___________', '고혈압', 'pressure'],
    [
        '43', "19). Words cannot always e___________ one's emotions. .",
        '말로써 항상 사람의 감정을 표현할 수 있는 것은 아니다.', 'express'
    ],
    [
        '43', '20). We took an e___________ train[bus] to Busan, ',
        '우리는 부산행 급행열차[고속버스]를 탔다.', 'express'
    ],
    [
        '43',
        '21). He was trying to i___________ his girlfriend with funny jokes. .',
        '그는 웃긴 농담으로 여자친구를 감동시키려고 애쓰고 있었다.', 'impress'
    ],
    [
        '43',
        '22). The more we are o___________, the more we will resist that o___________. , .',
        '우리가 억압받으면 받을수록, 그 억압에 더욱더 저항할 것이다.', 'oppressed, oppression'
    ],
    [
        '43', '23). The p___________ cause of lung cancer is smoking. .',
        '폐암의 주된 원인은 흡연이다.', 'prime'
    ],
    [
        '43', '24). Who will be the next p___________ minister?',
        '다음 수상은 누가 될까?', 'prime'
    ],
    [
        '43', '25). Our p___________ concern is the safety of the students. .',
        '우리의 주된 관심사는 학생들의 안전이다.', 'primary'
    ], ['43', '26). a p___________ infection 1 ,', '1차 감염', 'primary'],
    [
        '43',
        '27). The Brazilian rain forest is home to many p___________ tribes. .',
        '브라질의 열대 우림은 많은 원시 부족들의 보금자리다.', 'primitive'
    ],
    [
        '43',
        '28). The p___________ reason for the dismissal is that the employee was irresponsible. .',
        '해고의 주요 원인은 그 종업원이 무책임했기 때문이다.', 'principal'
    ],
    [
        '43', '29). Who is the p___________ of your high school? ',
        '너희 고등학교 교장 선생님은 누구시니? ★', 'principal'
    ], ['43', '30). free market p___________ ', '자유 시장의 원리', 'principles'],
    [
        '43', '31). I support the idea i___________ p___________. ',
        '나는 원칙적으로는 그 생각에 동의한다. ★', 'in principle'
    ],
    [
        '43',
        "32). I'd like to meet you today, but I have a p___________ commitment. , . ",
        '나는 오늘 너를 만나고 싶지만, 선약이 있어. ', 'prior'
    ],
    [
        '44', '1). A: Why did you ask to see me in p___________? ',
        '왜 저를 개인적으로 보자고 하셨죠?', 'private'
    ],
    [
        '44',
        '2). The law d___________ us o___________ our basic rights as citizens. ',
        '그 법은 우리의 시민으로서의 기본 권리들을 박탈했다. ★', 'deprived of'
    ],
    [
        '44',
        "3). Though it's possible Tom and Jerry will make up, it's not very p___________. , .",
        '톰과 제리가 화해할 수도 있지만, 가능성이 매우 낮다.', 'probable'
    ],
    [
        '44', '4). The police are p___________ into the details of the case. ',
        '경찰은 그 사건의 세부사항을 정밀 조사 중이다. ★', 'probing'
    ],
    [
        '44',
        "5). How can I p___________ my innocence when you won't let me search for evidence? ",
        '증거를 찾도록 허락해주시지 않는데 제가 어떻게 저의 결백을 입증할 수 있겠습니까?', 'prove'
    ],
    [
        '44', '6). The board is sure to a___________ the new budget. .',
        '이사회는 새 예산안을 승인할 것이 확실하다.', 'approve'
    ],
    [
        '44', "7). It's p___________ to dress formally for a funeral. .",
        '장례식에는 정장을 차려입는 것이 올바르다.', 'proper'
    ],
    [
        '44', "8). You're trespassing on private p___________. ",
        '당신은 사유지에 무단 침입 중이에요', 'property'
    ],
    [
        '44',
        '9). This seems like an a___________ time to announce my retirement. .',
        '지금이 내 은퇴를 알릴 적절한 시기인 것 같다.', 'appropriate'
    ],
    [
        '44', '10). He is always p___________ for appointments.',
        '그는 항상 약속 시간을 지킨다.', 'punctual'
    ],
    [
        '44', '11). All sentences need a p___________ mark at the end. ',
        '모든 문장 끝에는 구두점을 찍어야 한다. ★', 'punctuation'
    ],
    [
        '44', "12). I didn't mean to d___________ her. .",
        '나는 그녀를 실망시킬 의도는 아니었다.', 'disappoint'
    ],
    [
        '44',
        "13). The two people d___________ each other's claims in court. .",
        '두 사람은 법정에서 서로의 주장에 반론을 제기했다.', 'disputed'
    ],
    [
        '44',
        '14). The voting has ended, but the results are in d___________. , .',
        '투표는 끝났지만, 그 결과는 논란 속에 있다.', 'dispute'
    ],
    [
        '44',
        '15). Korean soccer fans have a r___________ for cheering enthusiastically. .',
        '한국 축구팬들은 열정적으로 응원하는 것으로 명성이 높다.', 'reputation'
    ],
    [
        '44',
        '16). They will a___________ new skills through this experience. .',
        '그들은 이번 경험을 통하여 새로운 기술을 얻게 될 것이다.', 'acquire'
    ],
    [
        '44', '17). To be a top athlete r___________ self-discipline.',
        '최고의 선수가 되려면 자기 수양이 필요하다. ', 'requires'
    ],
    [
        '44', "18). I'm calling you to i___________ about the latest model. .",
        '최신 모델에 관해 문의하려고 전화 드렸습니다.', 'inquire'
    ],
    [
        '44',
        "19). The detective i___________ i___________ the suspect's alibi. .",
        '그 탐정은 용의자의 알리바이를 조사했다.', 'inquired into'
    ],
    [
        '44', '20). He helped children c___________ their fears. ',
        '그는 아이들이 공포심을 극복하도록 도와주었다. ★', 'conquer'
    ],
    [
        '44', '21). He refused my r___________ to come an hour earlier. . ',
        '그는 한 시간 일찍 와달라는 내 요청을 거절했다. ', 'request'
    ],
    [
        '44', '22). The detail on this watch face is e___________. ',
        '시계 앞면(다이얼)의 세부 장식은 아주 정교하다. ★ ', 'exquisite'
    ],
    [
        '45',
        '1). A: How high are the mountains in this r___________? B: The peaks r___________ in height from 1,000 to 3,000 meters. ',
        '이 산맥의 산들은 얼마나 높습니까? 높이가 1,000에서 3,000미터에 이르지요.', 'range, range'
    ],
    [
        '45', '2). The meeting you a___________ has been postponed. .',
        '당신이 계획한 회의는 연기되었습니다.', 'arranged'
    ],
    [
        '45', '3). Everything has been well a___________. .', '모든 것이 잘 정리되었다.',
        'arranged'
    ],
    [
        '45',
        '4). Korea is r___________ number one in the world for archery. .',
        '한국은 양궁 분야에서 세계 위이다.', 'ranked'
    ],
    [
        '45', '5). The birth r___________ is going down. .', '출산율이 감소하고 있다.',
        'rate'
    ],
    [
        '45', '6). How would you r___________ this movie? ',
        '이 영화를 어떻게 평가하세요?', 'rate'
    ],
    [
        '45',
        '7) The r___________ o___________ nurses t___________ doctors is five to one at this hostpital. ',
        '이 병원의 간호사와 의사의 비율은 5대 1이다. ★', 'ratio of, to'
    ],
    [
        '45', '8). Humans are r___________ beings. .', '인간은 이성적인 존재이다.',
        'rational'
    ],
    [
        '45', '9). His excuse seems r___________. .', '그의 변명은 합리적으로 보인다.',
        'rational'
    ],
    [
        '45', "10). What's the r___________ you are asking so much?",
        '당신이 그렇게 많이 요구하는 이유는 무엇입니까? ', 'reason'
    ],
    [
        '45', '11). First impressions are not always c___________. .',
        '첫인상이 항상 옳은 것은 아니다.', 'correct'
    ],
    [
        '45', '12). Is there a d___________ flight to Chicago? ',
        '시카고로 가는 직항 노선이 있습니까?', 'direct'
    ],
    [
        '45',
        '13). I want you to d___________ all of your effort to this project. .',
        '나는 당신이 모든 노력을 이 일에 쏟기를 원합니다.', 'direct'
    ],
    [
        '45', '14). They e___________ a monument in the middle of the park. .',
        '그들은 그 공원의 중앙에 기념비를 세웠다.', 'erected'
    ],
    [
        '45', '15). The southern r___________ suffers from heavy rains. .',
        '남부 지역은 폭우로 고통받는다.', 'region'
    ],
    [
        '45',
        '16). R___________ exercise and healthy diet help you lose weight. .',
        '규칙적인 운동과 건강식은 체중 감량에 도움을 준다.', 'Regular'
    ],
    [
        '45',
        '17). The volume of economic activity is r___________ by the supply of money. .',
        '경제 활동 규모는 통화 공급량에 의해 조정된다.', 'regulated'
    ],
    [
        '45',
        '18) All citizens are expected to live by the r___________ of law. .',
        '모든 시민이 법이 정한 원칙에 따라 살기로 기대된다.', 'rule'
    ],
    [
        '45', '19) Many great pharaohs r___________ over Egypt in the past. ',
        '많은 위대한 파라오가 과거에 이집트를 지배했다. ★', 'ruled'
    ],
    [
        '45', '20). Catherine the Great r___________ for 34 years in Russia. ',
        '캐서린 여제는 러시아를 34년간 통치했다. ★ ', 'reigned'
    ], ['45', '21). the r___________ family [],', '왕족[왕실]', 'royal'],
    [
        '45', "22). Let's r___________ the table this way. .",
        '테이블을 이쪽으로 회전시키자.', 'rotate'
    ],
    [
        '45', '23). The guards r___________ every two hours. .',
        '경비원들은 두 시간마다 교대 근무한다.', 'rotate'
    ],
    [
        '45',
        '24). They tried to find new measures to c___________ inflation. .',
        '그들은 인플레이션을 통제하기 위한 새로운 방책을 찾으려 노력했다.', 'control'
    ],
    [
        '45',
        '25). I can c___________ my window shades by remote c___________. .',
        '나는 리모콘으로 내 블라인드를 조종할 수 있다.', 'control'
    ],
    [
        '45',
        '26). The situation is o___________ o___________ c___________. (=b___________ m___________ c___________) .',
        '그 상황은 통제할 수 없다.', 'out of control, beyond my control'
    ],
    [
        '45',
        "27). Don't e___________ in this course just to receive a certificate. ",
        '단지 수료증을 받기 위해서 이 과정에 등록하지는 마세요. ★', 'enroll'
    ],
    [
        '45',
        '28). Many businesses w___________ b___________ during the recession. .',
        '불경기 동안 많은 기업들이 파산했다.', 'went bankrupt'
    ],
    [
        '45', '29). The c___________ politician was arrested. ',
        '그 부패한 정치가는 체포되었다. ★', 'corrupt'
    ],
    [
        '45', "30) Drinking coffee too late can d___________ one's sleep. .",
        '너무 늦게 커피를 마시면 수면을 방해할 수 있다.', 'disrupt'
    ],
    [
        '45', '31). Violence e___________ during the protest. .',
        '항의 시위 도중에 폭력사태가 일어났다.', 'erupted'
    ],
    [
        '45', "32). Stop i___________ me while I'm talking. .",
        '내가 말하는 도중에 끼어들지 마세요.', 'interrupting'
    ],
    [
        '45', '33). The show was i___________ by a news report. .',
        '그 텔레비전[라디오] 프로는 뉴스 보도로 잠시 중단되었다.', 'interrupted'
    ],
    [
        '45', '34). Which r___________ did you take? ', '너는 어떤 길[노선]을 택했니?',
        'route'
    ],
    [
        '45', '35). My r___________ changed when I broke my leg. ',
        '다리를 다쳤을 때 나의 일상(생활)은 달라졌다. ', 'routine'
    ],
    [
        '46',
        '1). This temple was the most s___________ place of our ancestors. ',
        '이 사원은 우리 선조들에게 가장 신성한 장소였다. ★ ', 'sacred'
    ],
    [
        '46', '2). Animal s___________ was often considered a sacred act. . ',
        '짐승을 제물로 바치는 것은 흔히 신성한 행위로 간주되었다. ', 'sacrifice'
    ],
    [
        '46', '3). Parents s___________ a lot for their children. .',
        '부모님들은 자녀를 위해 많은 것을 희생한다.', 'sacrifice'
    ],
    [
        '46', '4). He is peace-loving and as patient as a s___________. .',
        '그는 온화하며 성인군자만큼 인내심이 많다.', 'saint'
    ],
    [
        '46', '5). The plane will begin to d___________ soon. ',
        '비행기가 곧 하강하기 시작할 것입니다. ★', 'descend'
    ],
    [
        '46', "6). We weren't aware of the s___________ of the problem. .",
        '우리는 그 문제의 심각한 정도를 깨닫지 못했다.', 'scale'
    ],
    [
        '46', '7). She moved steadily up the social s___________. ',
        '그녀는 착실하게 사회적 지위를 쌓아 올렸다. ★', 'scale'
    ],
    [
        '46', '8). I weighed myself on the s___________. ',
        '나는 체중계에 올라 몸무게를 쟀다. ★', 'scale'
    ],
    [
        '46', '9). Violence has e___________ to a worrying level. ',
        '폭력 사태가 우려할 수준으로 악화됐다. ★', 'escalated'
    ],
    [
        '46',
        '10). She w___________ c___________ o___________ a strange sound in the distance. .',
        '그녀는 멀리서 나는 이상한 소리를 의식하고 있었다.', 'was conscious of'
    ],
    [
        '46', '11) She has a s___________ fear of water. ',
        '그녀는 물에 대한 잠재의식적 공포가 있다. ★', 'subconscious'
    ], ['46', '12). a guilty c___________ ', '죄의식', 'conscience'],
    [
        '46', '13). Can you d___________ what the man looked like? ',
        '그 남자가 어떻게 생겼었는지 묘사할 수 있겠니?', 'describe'
    ],
    [
        '46', '14). The doctor p___________ antibiotics. ', '의사는 항생제를 처방했다. ★',
        'prescribed'
    ],
    [
        '46', '15). The law p___________ serious penalties for this crime. .',
        '법은 이 범죄에 대해 엄벌을 규정하고 있다.', 'prescribes'
    ],
    [
        '46', '16). Do you s___________ to any magazines[newspapers]?',
        '(정기) 구독하는 잡지[신문]가 있으세요?', 'subscribe'
    ],
    [
        '46', '17). The key s___________ are highlighted in blue. .',
        '중요한 부분은 파란색으로 표시되어 있습니다.', 'sections'
    ],
    [
        '46', '18). The orange was peeled and s___________. ',
        '그 오렌지는 껍질이 벗겨지고 분할되었다. ★', 'sectioned'
    ],
    [
        '46',
        '19) As the clean energy s___________ gains popularity, oil companies will start shrinking. ',
        '청정에너지 분야가 인기를 얻음에 따라 석유 회사는 위축되기 시작할 것이다.', 'sector'
    ],
    [
        '46',
        '20) Only a small s___________ of the population supported the new policies. ',
        '인구의 적은 일부만이 그 새로운 정책을 지지했다.', 'segment'
    ],
    [
        '46', '21) a s___________ of humor[direction/justice]',
        '유머감각[방향감각/정의감]', 'sense'
    ],
    [
        '46', '22) I felt a great s___________ of loss that day. .',
        '나는 그 날 엄청난 상실감을 느꼈다.', 'sense'
    ],
    [
        '46',
        '23) When the body s___________ a dangerous parasite, it is mobilized to produce special cells. ',
        '신체가 위험한 기생충을 감지하면 그것은 특별한 세포를 만드는데 동원된다.', 'senses'
    ],
    [
        '46', '24). The news created a great s___________. ',
        '그 소식은 세상을 떠들썩하게 했다.', 'sensation'
    ],
    [
        '46', '25). You are talking complete n___________. ',
        '너는 완전히 말도 안 되는 소리를 하고 있다.', 'nonsense'
    ],
    [
        '46', '26). antiwar s___________ of the public (反戰) ', '대중의 반전(反戰) 정서',
        'sentiments'
    ],
    [
        '46',
        "27). I didn't c___________ t___________ s___________ my information. .",
        '나는 나의 정보 공유에 동의하지 않았다.', 'consent to share'
    ],
    [
        '46', '28). The workers r___________ the way they were treated. ',
        '근로자[직원]들은 그들이 대우 받은 방식에 분개했다.', 'resented'
    ],
    [
        '46', '29). The s___________ of this perfume is nice. . ',
        '이 향수의 향은 좋다. ', 'scent'
    ],
    [
        '47', '1). Keep the numbered cards i___________ s___________. .',
        '번호가 매겨진 카드들을 순서대로 두세요.', 'in sequence'
    ],
    [
        '47', '2). Global warming has serious c___________. ',
        '지구 온난화는 심각한 결과를 초래한다. ★', 'consequences'
    ],
    [
        '47',
        '3). The charity event was a huge success, so they will be able to plan s___________ events. .',
        '자선행사가 큰 성공을 거두어서 그들은 다음 행사들을 기획할 수 있을 것이다.', 'subsequent'
    ],
    [
        '47',
        "4). I've encouraged students to p___________ their own interests. . ",
        '나는 학생들이 자신만의 관심사를 추구하도록 격려해왔다. ', 'pursue'
    ],
    [
        '47',
        "5). It's hard to find something that s___________ everyone's needs. . ",
        '모든 사람들의 필요에 부합하는 것을 찾기는 어렵다. ', 'suits'
    ],
    [
        '47', "6). Purple doesn't s___________ her. .", '보라색은 그녀에게 어울리지 않는다.',
        'suit'
    ],
    [
        '47',
        '7). During the French Revolution, thousands of people were e___________. .',
        '프랑스 혁명 때 수천 명이 처형당했다.', 'executed'
    ],
    [
        '47',
        "8). They couldn't e___________ the directions issued by the executive board. ",
        '그들은 이사회가 내린 지시사항들을 이행할 수 없었다.★', 'executed, executive'
    ],
    [
        '47',
        '9). While we were in the d___________, we could never enjoy any fresh desserts with our meals. .',
        '우리는 사막에 있는 동안 식사 때 신선한 후식을 전혀 즐길 수 없었다.', 'desert'
    ],
    [
        '47', '10). The house has been d___________ for a decade. ',
        '그 집은 10년간 버려진 채 있다. ★', 'deserted'
    ],
    [
        '47', '11). I i___________ my key in the door. .', '나는 문에 열쇠를 넣었다.',
        'inserted'
    ],
    [
        '47', '12). The editor i___________ a few words into the sentence. .',
        '편집자는 그 문장에 몇 마디를 덧붙였다.', 'inserted'
    ],
    [
        '47', '13). Advertising e___________ a great influence on us. ',
        '광고는 우리에게 큰 영향력을 발휘한다. ★', 'exerts'
    ],
    [
        '47', '14). He never e___________ h___________ to help anyone. ',
        '그는 결코 누군가를 도우려 노력하지 않는다. ★', 'exerts himself'
    ],
    [
        '47',
        "15). There's been a s___________ o___________ robberies downtown. .",
        '시내에서 연쇄 강도가 발생하고 있다.', 'series'
    ],
    [
        '47', '16). The popular actor appeared on the TV s___________. TV .',
        '그 인기 있는 배우는 시리즈에 출연했다.', 'series'
    ],
    [
        '47',
        '17). We must c___________ energy and use it more efficiently. .',
        '우리는 에너지를 보존하고 보다 더 효율적으로 사용해야 한다.', 'conserve'
    ],
    [
        '47', '18). His brave act d___________ admiration. ',
        '그의 용감한 행동은 존경받을만하다. ★', 'deserves'
    ],
    [
        '47',
        '19). The purpose of this fundraising event is to p___________ endangered animals. . ',
        '이 모금 행사의 목적은 멸종 위기의 동물들을 보호하기 위함이다. ', 'preserve'
    ],
    [
        '47', '20). We r___________ a table by the window. ',
        '우리는 창가 쪽 테이블을 예약했다.', 'reserved'
    ], ['47', '21). foreign exchange r___________ ', '외환 보유고', 'reserves'],
    [
        '47',
        '22). After o___________ the behavior of the ants carefully, he noticed that they o___________ strict social rules. , .',
        '개미의 행동을 주의 깊게 관찰한 뒤에, 그는 개미들이 엄격한 사회 규칙을 지킨다는 것을 알아냈다.',
        'observing, observed'
    ],
    [
        '47', '23). Where are you currently r___________? ',
        '현재 살고 있는 곳이 어디입니까?', 'residing'
    ], ['47', '24). the P___________ of Korea ', '한국의 대통령', 'President'],
    [
        '47',
        '25). She started at the bottom and worked her way up to become p___________ of the company. .',
        '그녀는 말단에서 시작하여 올라가 그 기업의 회장이 되었다.', 'president'
    ],
    [
        '47',
        '26). There will be a short break in the middle of the s___________. .',
        '회의 중간에 잠깐의 휴식 시간이 있겠습니다.', 'session'
    ],
    [
        '47',
        '27) Our engineer will a___________ the building site later today. .',
        '우리 엔지니어가 오늘 늦게 건축 부지를 평가할 것입니다.', 'assess'
    ],
    [
        '47',
        '28) My younger sister is o___________ w___________ playing games on her smartphone. .',
        '내 여동생은 스마트폰 게임에 집착한다. ★', 'is obsessed with'
    ],
    [
        '47',
        "29) You don't need to o___________ o___________ these details, so just relax! ",
        '이런 세부사항에 강박감을 가질 필요 없어, 그러니까 진정해!!', 'obsess over'
    ],
    [
        '47', '30). She s___________ the case quickly. .',
        '그녀는 그 사건을 재빨리 해결했다.', 'settled'
    ],
    [
        '47', '31). They got married and s___________ in Canada. .',
        '그들은 결혼해서 캐나다에 정착했다.', 'settled'
    ],
    [
        '47', '32). Stop chatting and s___________ down. . ', '그만 떠들고 진정해라. ',
        'settle'
    ],
    [
        '48',
        "1). Once you've completed the form, please s___________ your name at the bottom. , .",
        '양식 작성을 완료하시면, 아래에 서명해 주십시오.', 'sign'
    ],
    [
        '48', '2). She played a s___________ role in carrying out the plan. .',
        '그녀는 그 계획을 수행하는데 있어 중요한 역할을 했다.', 'significant'
    ],
    [
        '48', '3). I was a___________ the task of ordering samples. .',
        '나는 견본을 주문하는 업무를 부여받았다.', 'assigned'
    ],
    [
        '48',
        '4) It is important to d___________ spaces where unwanted noise can be eliminated. ',
        '원치 않는 소음이 제거될 수 있는 공간을 설계하는 것이 중요하다', 'design'
    ],
    [
        '48',
        '5) Designers draw on their d___________ experience when approaching a new project. .',
        '디자이너들은 새 프로젝트 착수할 때 그들의 디자인 경험을 기반으로 했다.', 'design'
    ],
    [
        '48',
        '6) There are two locations d___________ for donations: the Library and the Community Center. ',
        '기부를 위해 지정된 두 장소가 있는데, 도서관과 시민회관이다.', 'designated'
    ],
    [
        '48', '7). She r___________ from her post yesterday. ',
        '그녀는 어제 자신의 직[직위]에서 사임했다.', 'resigned'
    ],
    [
        '48',
        '8) At an agreed s___________ , everyone in the auditorium started clapping their hands. .',
        '합의된 신호에 따라 강당에 있던 모든 사람이 박수를 치기 시작했다.', 'signal'
    ],
    [
        '48',
        '9) When the director was ready, he s___________ for the actors to begin. , .',
        '감독은 준비되자, 배우들에게 시작하라고 신호를 보냈다.', 'signaled'
    ],
    [
        '48',
        '10). Emma folded the letter twice and s___________ it within an envelope. Emma . ',
        'Emma는 편지를 두 번 접어 그것을 봉투 안에 봉했다. ', 'sealed'
    ],
    [
        '48',
        "11). The similarity doesn't end there. The twins are s___________ in every respect. . .",
        '비슷한 점은 그뿐만이 아니다. 그 쌍둥이는 모든 면에서 닮았다.', 'similar'
    ],
    [
        '48',
        '12). The smell closely r___________ the scent of fresh roses.. . ',
        '그 냄새를 신선한 장미의 향기와 아주 유사하다. ★', 'resembles'
    ],
    [
        '48', '13). Wait until all the guests are a___________. .',
        '손님들이 모두 모일 때까지 기다려라.', 'assembled'
    ],
    [
        '48', "14). The couple s___________ don't have any problems. . ",
        '그들은 겉보기에는 아무 문제가 없다. ★', 'seemingly'
    ],
    [
        '48', '15). They carried out a s___________ of a tsunami disaster. . ',
        '그들은 쓰나미 재난에 대한 가상 실험을 실시했다. ★', 'simulation'
    ],
    [
        '48', '16). They shouted the answer s___________. . ',
        '그들은 동시에 답을 외쳤다. ★', 'simultaneously'
    ],
    [
        '48', '17). You must be sociable to be a s___________ success. .',
        '사회적으로 성공하려면 사교적이어야 한다.', 'social'
    ],
    [
        '48', '18). Alcohol is a___________ with some cancers. .',
        '알코올은 몇 가지 암과 연관이 있다.', 'associated'
    ],
    [
        '48',
        "19). I don't want my sone to a___________ w___________ bullies. . ",
        '저는 제 아들이 불량 학생들과 어울리지 않았으면 해요. ★', 'associate with'
    ],
    [
        '48',
        '20). The s___________ survivor of the plane crash was a little baby. .',
        '그 비행기 추락사고의 유일한 생존자는 어린 아기였다.', 'sole'
    ],
    [
        '48', '21). I used to be a s___________ traveler. .',
        '나는 (예전에) 혼자 여행하곤 했다.', 'solitary'
    ],
    [
        '48', '22). I sometimes enjoy quiet s___________ at home. .',
        '나는 때때로 집에서 조용히 혼자 있는 것을 즐긴다.', 'solitude'
    ],
    [
        '48', '23). How can we s___________ this problem? ',
        '우리는 이 문제를 어떻게 해결할 수 있을까?', 'solve'
    ],
    [
        '48', "24). The issue hasn't been r___________ yet. .",
        '그 문제는 아직 해결되지 않았다.', 'resolved'
    ],
    [
        '48', '25). I d___________two spoonfuls of sugar in my coffee. ',
        '나는 커피에 설탕 두 스푼을 넣고 녹였다. ★', 'dissolved'
    ],
    [
        '49', '1). She studied the p___________ of the ancient Greeks. . ',
        '그녀는 고대 그리스인들의 철학을 공부했다. ★', 'philosophy'
    ],
    [
        '49', '2). Airport security is getting more s___________. .',
        '공항 보안이 점점 더 정교해지고 있다.', 'sophisticated'
    ],
    [
        '49',
        '3). Freshmen, s___________, juniors and seniors are all considered undergraduated. ',
        '1학년, 2학년, 3학년, 4학년은 모두 학부생으로 간주된다.', 'sophomores'
    ],
    [
        '49',
        '4). Jake put on his s___________ to view the strange s___________ properly. .',
        '존은 그 기묘한 구경거리를 제대로 보려고 안경을 썼다.', 'spectacles'
    ],
    [
        '49', '5). Try to find the positive a___________ of any situation. .',
        '어떤 상황에서든 긍정적인 면을 찾도록 노력해라.', 'aspects'
    ],
    [
        '49',
        "6). We didn't e___________ him t___________ c___________ in time. .",
        '우리는 그가 제시간에 오리라고는 기대하지 않았다.', 'expect, to come'
    ],
    [
        '49', '7). Police i___________ the crime scene.', '경찰은 범죄 현장을 조사했다.',
        'inspected'
    ],
    [
        '49', '8). Our main virtue is r___________ for elders. .',
        '우리의 중요한 미덕은 웃어른을 공경하는 것이다.', 'respect'
    ],
    [
        '49', "9). The p___________ for continued growth aren't favorable. .",
        '지속적인 성장에 대한 전망은 밝지 않다.', 'prospects'
    ],
    [
        '49',
        "10). A: Who do the police s___________ in the robbery? B: The s___________ is a tall, thin man called 'Mike.' ",
        '경찰이 그 강도 사건에서 의심하고 있는 것은 누구지?', 'suspect, suspect'
    ],
    [
        '49',
        '11). The government passed a new law to protect endangered s___________ . .',
        '정부는 멸종 위기에 처한 종을 보호하기 위해 새로운 법을 통과시켰다.', 'species'
    ],
    [
        '49', '12). There was no s___________ reason for the quarrel. .',
        '그 말다툼에는 특별한 이유가 없었다.', 'specific'
    ],
    [
        '49', '13). Can you be more s___________? ?', '좀 더 자세히 말해줄래?',
        'specific'
    ],
    [
        '49', '14). S___________ care is required when shopping online. .',
        '온라인으로 구매 시에는 각별한 주의가 요구된다.', 'Special'
    ],
    [
        '49', '15). He came d___________ the bad weather. .',
        '그는 좋지 않은 날씨에도 불구하고 왔다.', 'despite'
    ],
    [
        '49', '16). His business p___________ as expected. .',
        '그의 사업은 예상대로 번창했다. ★', 'prospered'
    ],
    [
        '49',
        '17). Sam felt d___________ over his desperate financial situation. .',
        '샘은 그의 절망적인 재정 상태에 절망감을 느꼈다.', 'despair'
    ],
    [
        '49', '18). The Earth is not a perfect s___________. .',
        '지구는 완전한 구형이 아니다.', 'sphere'
    ],
    [
        '49',
        "19). Most meteors burn up when they enter Earth's a___________. . ",
        '대부분의 유성은 지구 대기에 집입할 때 불탄다. ★', 'atmosphere'
    ],
    [
        '49', '20). The office party had a friendly a___________. .',
        '사내 파티는 화기애애한 분위기였다.', 'atmosphere'
    ],
    [
        '49',
        "21). Most of the world's population lives in the Northern H___________. . ",
        '세계 인구의 대부분은 북반구에 산다. ★', 'Hemisphere'
    ],
    [
        '49',
        '22). Many people believe that creativity comes from the right h___________ of the brain. .',
        '많은 사람이 창의력은 우뇌에서 온다고 생각한다.', 'hemisphere'
    ],
    [
        '50', '1). My grandmother is with me in s___________. .',
        '내 할머니는 마음속에서 나와 함께 계신다.', 'spirit'
    ], ['50', '2). raise[drop] s___________ []', '사기를 높이다[떨어뜨리다]', 'spirits'],
    [
        '50', '3). I a___________ t___________ b___________ a doctor. .',
        '저는 의사가 되기를 간절히 바랍니다.', 'aspiration, aspire to become'
    ],
    [
        '50',
        '4). The saying "Genius is 1% i___________ and 99% perspiration" is very i___________. ‘ ',
        '‘천재는 1%의 영감과 99%의 노력에 의해 이루어진다.’는 격언은 매우 고무적이다.',
        'inspiration, inspiring'
    ],
    [
        '50', '5). My credit card e___________ in July. ',
        '내 신용카드는 7월에 만료된다. ★', 'expires'
    ],
    [
        '50',
        '6). Although technology is responsive to the will of the people, it can seldom r___________ immediately and is never free. .',
        '비록 기술이 사람들의 의지에 호응할지라도 그것이 즉시 반응하는 경우는 거의 없고 절대 공짜가 아니다.', 'respond'
    ],
    [
        '50', '7). He was r___________ for the accident. .',
        '그는 그 사고에 대한 책임이 있었어.', 'responsible, responsibility'
    ],
    [
        '50', '8). The company s___________ a baseball team. .',
        '그 회사는 야구팀을 후원한다.', 'sponsors'
    ],
    [
        '50', '9). I know where you s___________. .',
        '나는 네가 어떤 입장에 있는지 알고 있다.', 'stand'
    ],
    [
        '50', '10) I can’t s___________ this pain. .', '나는 이 고통을 참을 수가 없다.',
        'stand'
    ],
    [
        '50',
        '11). Most phone companies charge a s___________ rate for local phone calls. .',
        '대부분의 이동통신 업체들은 지역 통화에 대해 표준 요금을 부과한다.', 'standard'
    ],
    [
        '50', '12). Jack always sets his s___________ too high. Jack .',
        '은 항상 자신의 기준을 너무 높게 설정한다.', 'standard'
    ],
    [
        '50',
        "13). He s___________ firmly that the freedom of the press shouldn't be limited by the s___________. .",
        '그는 언론의 자유가 국가에 의해 제한되어서는 안 된다고 단언했다.', 'stated, state'
    ],
    [
        '50',
        "14). Teams compile s___________ to evaluate their players' game performance.",
        '팀들은 선수들의 경기 성적을 평가하기 위해 통계를 모은다.', 'statistics'
    ],
    [
        '50',
        "15). Some of the world's most famous s___________ can be seen in the Louvre in Paris. .",
        '세계의 가장 유명한 조각상 중 몇몇은 파리의 루브르 박물관에서 볼 수 있다.', 'statues'
    ], ['50', '16). legal immigrant s___________ ', '합법적 이민자 신분', 'status'],
    [
        '50', '17). She inquired about the s___________ of her application. .',
        '그녀는 지원의 진행 상황에 대해 문의했다.', 'status'
    ],
    [
        '50',
        '18). In spite of some instability in the labor market, Korea will soon regain economic s___________. ',
        '노동과 관련된 어느 정도의 불안정에도 불구하고, 한국은 곧 경제적 안정을 되찾을 것이다.', 'stability'
    ],
    [
        '50', '19). Our company was e___________ in 1972. ',
        '우리 회사는 1972년에 설립되었다.', 'established'
    ],
    [
        '50', '20). We had c___________ rain in July. 7 .',
        '7월에는 끊임없이 비가 내렸다.', 'constant'
    ],
    [
        '50', '21). His e___________ is twice the size of mine. .',
        '그의 재산은 나의 두 배이다.', 'estate'
    ],
    [
        '50', '22). There are countless i___________ like that. . ',
        '그와 같은 예들은 셀 수 없이 많다. ', 'instances'
    ],
    [
        '50', '23). The movie was an i___________ success. . ',
        '그 영화는 즉각적인 성공을 거두었다. ', 'instant'
    ],
    [
        '50', '24). She was confused for an i___________. .', '그녀는 순간 혼란스러웠다.',
        'instant'
    ],
    [
        '50',
        '25). He overcame the o___________ of blindness and became a great musician. ',
        '그는 시각 장애를 극복하고 훌륭한 음악가가 되었다.★', 'obstacle'
    ],
    [
        '50', '26). Keep dangerous s___________ away from children. .',
        '위험한 물질은 아이들로부터 멀리 두어라.', 'substances'
    ],
    [
        '51', '1) The dog a___________ the blind. .', '그 개는 시각장애인을 도왔다.',
        'assisted'
    ],
    [
        '51',
        '2) Happiness c___________ i___________ being with people you love. ',
        '행복은 사랑하는 사람들과 함께 있는 데 있다. ★', 'consists in'
    ],
    [
        '51', '3) What does this drink c___________ o___________ ? ',
        '이 음료는 무엇으로 만들어졌나요? ★', 'consist of'
    ],
    [
        '51',
        '4) If we e___________ without love, our existence is meaningless. , .',
        '만약에 우리가 사랑 없이 살아간다면, 우리의 존재는 무의미하다.', 'exist'
    ],
    [
        '51', '5) They i___________ o___________ c___________ with us. .',
        '그들은 우리와 함게 갈 것을 고집했다.', 'insisted on coming'
    ],
    [
        '51', '6) She i___________ that he wear his new suit for the party. .',
        '그녀는 그에게 파티를 위해 새 양복을 입을 것을 요구했다.', 'insisted'
    ],
    [
        '51', "7) She r___________ her mother's pressure. .",
        '그녀는 어머니의 압박에 반항했다.', 'resisted'
    ],
    [
        '51',
        '8) Paying promptly will r___________ your membership to good standing. .',
        '곧바로 지불하면 귀하의 멤버십이 정상 회원으로 회복될 것입니다.', 'restore'
    ],
    [
        '51', '9) The police a___________ him for selling drugs. .',
        '경찰은 그를 마약 판매 혐의로 체포했다.', 'arrested'
    ],
    [
        '51',
        '10) Lewis made a costly mistake, which c___________ him his job.',
        'Lewis 은 손실이 큰 실수를 해서, 그것 때문에 일자리를 잃었다. ★', 'costly, cost'
    ],
    [
        '51',
        '11) He has a s___________ job and his wages are s___________ rising. , .',
        '그는 안정된 일자리를 갖고 있고, 그의 봉급은 꾸준히 오르고 있다.', 'steady, steadily'
    ],
    ['51', '12) a political[educational] s___________', '정치[교육] 제도', 'system'],
    [
        '51',
        "13) Forty pages c___________ the book's section on World War Ⅱ. ",
        '이 책의 2차 세계대전에 대한 장은 40페이지로 구성되어 있다. ★', 'constitute'
    ],
    [
        '51', '14) Their actions c___________ a clear threat. ',
        '그들의 행동은 명백한 위협으로 간주된다. ★', 'constitute'
    ],
    [
        '51',
        '15) The university established an i___________ for Korean studies. .',
        '그 대학은 한국학 연구소를 설립했다.', 'institute'
    ],
    [
        '51',
        '16) We must s___________ a new chair f___________ the broken one. ',
        '우리는 부러진 의자를 새 의자로 바꾸어야 한다. ★', 'substitute, for'
    ],
    [
        '51',
        '17) Jake s___________ f___________ Lucy, who was on a business trip. .',
        '제이크는 출장 중인 루시의 업무를 대신했다.', 'substituted for'
    ],
    [
        '51',
        '18) The transportation industry does more than just carry travelers from one d___________ to another. .',
        '운송업은 단지 한 목적지에서 다른 목적지로 여행객을 옮기는 것 이상의 것을 한다.', 'destination'
    ],
    [
        '51', '19) According to s___________, Friday the 13th is unlucky.',
        '미신에 따르면, 13일의 금요일은 불길하다.', 'superstition'
    ],
    [
        '51',
        '20) Sometimes, it is difficult to d___________ fantasy f___________ reality. .',
        '때때로 환상화 현실을 구별하기가 어렵다.', 'distinguish, from'
    ],
    [
        '51', '21) The firefighters could barely e___________ the fire. ',
        '소방관들이 간신히 불길을 잡았다. ★', 'extinguish'
    ],
    [
        '51',
        '22) The number of e___________ species outnumbers that of living species. .',
        '멸종된 종들의 수가 살아있는 종들의 수보다 더 많다.', 'extinct'
    ],
    [
        '51', '23) That idea is quite d___________ f___________ my idea. ',
        '그 생각은 나의 생각과 상당히 다르다.', 'distinct from'
    ],
    [
        '51', '24) Animals hunt by i___________ . .', '동물들은 본능적으로 사냥을 한다.',
        'instinct'
    ],
    [
        '51', "25) Some colors s___________ people's appetites. ",
        '어떤 색은 식욕을 자극한다. ★ ', 'stimulate'
    ],
    [
        '52', '1) Mary is quite s___________ with her children. ',
        '메리는 아이들에게 꽤나 엄격하다.', 'strict'
    ],
    [
        '52',
        '2) The movie was not successful in the s___________ sense of the word. ',
        '엄밀한 의미로 그 영화는 성공적이지 못했다.', 'strict'
    ], ['52', '3) a r___________ area ', '제한 구역', 'restricted'],
    ['52', '4) an election d___________ ,', '선거구,', 'district'],
    [
        '52',
        '5) I enjoyed walking around the theater d___________ in New York. ',
        '나는 뉴욕의 극장가를 돌아다니는 것을 즐겼다.', 'district'
    ],
    [
        '52',
        '6) Their relationship has been under a lot of s___________ lately. ',
        '그들의 관계는 최근에 많은 긴장감 속에 있다. ★', 'strain'
    ],
    [
        '52',
        "7) It's hard for children to r___________ themselves from making noise. ",
        '아이들이 스스로 떠들지 않도록 억제하는 것은 힘들다.', 'restrain'
    ],
    [
        '52', "8) Being so upset, I couldn't r___________ my anger. ",
        '너무 화가 나서, 나는 화를 참을 수 없었다.', 'restrain'
    ],
    [
        '52', '9) The ship is rounding the S___________ of Gibraltar. ',
        '그 배는 지브롤터 해협을 돌고 있다. ★', 'straits'
    ],
    [
        '52', '10) Stressful events can cause a lot of d___________ . ',
        '스트레스를 주는 사건은 많은 고통을 야기할 수 있다.', 'distress'
    ],
    [
        '52', '11) Too much s___________ can ruin your health. ',
        '과도한 스트레스는 건강을 해칠 수 있다.', 'stress'
    ],
    [
        '52',
        '12) The speaker s___________ the importance of eating a good breakfast. ',
        '강연자는 균형 잡힌 아침 식사의 중요성을 강조했다.', 'stressed'
    ],
    [
        '52',
        '13) Our school baseball team enhanced our school p___________ by winning the national championship. ',
        '우리 학교 야구부는 전국 선수권 대회에서 승리하여 학교의 위상을 높였다.', 'prestige'
    ],
    [
        '52', '14) the social/political/economic s___________ ', '사회/정치/경제 구조',
        'structure'
    ],
    [
        '52', '15) The human body is an incredibly complex s___________. ',
        '인체는 믿을 수 없을 정도로 복잡한 조직체이다.', 'structure'
    ],
    [
        '52', '16) When are they going to c___________ a new bridge? ',
        '그들은 언제 새로운 다리를 건설할 예정입니까?', 'construct'
    ],
    [
        '52',
        "17) I've i___________ everyone to wait here until the instructor arrives. ",
        '나는 선생님이 도착할 때까지 여기에서 기다리라고 모두에게 지시했다.', 'instructed'
    ], ['52', '18) a medical i___________ ', '의료기구', 'instrument'],
    [
        '52',
        '19) She plays several musical i___________, including the piano and flute. ',
        '그녀는 피아노와 플롯을 포함한 몇 가지 악기를 연주할 수 있다.', 'instruments'
    ], ['52', '20) car/tourist i___________ / ', '자동차/관광 산업', 'industry'],
    [
        '52',
        '21) One destructive action can d___________ the results of years of constructive activity. ',
        '하나의 파괴적인 행동이 수년 간 건설적인 활동의 결과를 망칠 수 있다.', 'destroy'
    ],
    [
        '52',
        '22) A: I did not mean to ___ Ryan. B: But that joke you told was quite an ___ . ',
        '나는 라이언을 모욕할 의도는 아니었어. 하지만 네 농담은 꽤나 모욕적이었어.', 'insult, insult'
    ],
    [
        '52', '23) According to the test r___________ , your health is fine. ',
        '검사 결과에 따르면, 당신의 건강은 좋습니다.', 'results'
    ],
    [
        '52',
        '24) Tooth decay can r___________ f___________ eating too many sweets. ',
        '충치는 단 것을 너무 많이 먹게 되면 생길 수 있다. ★', 'result from'
    ],
    [
        '52',
        '25) The accident r___________ i___________ the death of two passengers. ',
        '그 사고로 승객 두 명이 죽었다. ★', 'resulted in'
    ],
    [
        '52',
        '26) I a___________that you were leaving early, since you said you needed to pick up your son. ',
        '네가 네 아들을 데리러 가야한다고 말해서 나는 네가 일찍 떠날 것이라고 생각했다.', 'assumed'
    ],
    [
        '52', '27) He a___________ the office of the presidency in May. ',
        '그는 대통령직을 5월에 맡았다. ★', 'assumed'
    ],
    [
        '52', '28) This car c___________ less gas than others. ',
        '이 차는 다른 차들보다 연료를 덜 소비한다.', 'consumes'
    ],
    [
        '52', '29) The ten missing passengers are p___________ dead. ',
        '실종된 10명의 승객들은 사망한 것으로 추정된다.', 'presemed'
    ],
    [
        '52',
        "30) They're going to r___________ the match after the rain stops. ",
        '그들은 비가 그친 뒤 경기를 재개할 것이다. ★', 'resume'
    ],
    [
        '53',
        '1) We a___________ customers that our goods are 100% authentic. ',
        '저희는 고객들에게 저희 제품이 100% 진품이라는 것을 보장합니다.', 'assure'
    ],
    [
        '53', '2) The nurse knows how to r___________ anxious patients. ',
        '그 간호사는 걱정하는 환자들을 안심시키는 방법을 안다.', 'reassure'
    ],
    [
        '53', '3) This building is i___________ against fire. ',
        '이 건물은 화재에 대비하여 보험에 들어있다.', 'insured'
    ],
    [
        '53', '4) A crowd of fans s___________ toward the stage. ',
        '수많은 팬들이 무대 앞으로 몰려들었다. ★', 'surged'
    ],
    [
        '53', '5) Her main s___________ of income is her pension. ',
        '그녀의 주요 수입원은 연금이다.', 'source'
    ],
    [
        '53', '6) Have you found the s___________ of the problem? ',
        '그 문제의 원인을 찾았습니까?', 'source'
    ],
    [
        '53',
        '7) Countries need to carefully manage their natural r___________ ',
        '국가들은 그들의 천영 자원을 주의하여 관리해야한다.', 'resources'
    ],
    [
        '53',
        '8) She used a variety of r___________ to gather information for her report. ',
        '그녀는 보고서를 위한 정보를 모으기 위해 다양한 자료를 사용했다.', 'resources'
    ],
    [
        '53',
        '9) The secretary a___________ a note t___________ the front of the file. ',
        '비서는 서류 앞에 메모를 붙였다.', 'attached'
    ],
    [
        '53',
        '10) A___________ is often the best form of defense. ; the heart a___________ ',
        '공격이 종종 최선의 방어책이다. , 심장 마비', 'Attack'
    ],
    [
        '53', '11) His life was a___________ s___________ .',
        '그의 목숨이 위태로웠다. ★', 'at stake'
    ],
    [
        '53',
        '12) My car remains i___________, even though I bought it many years ago. ',
        '수년 전에 구매했음에도 불구하고 내 차는 아직 멀쩡하다.★', 'intact'
    ],
    [
        '53', '13) He has a lot of c___________ in business and politics. ',
        '그는 재계와 정계에 인맥이 많다. ★', 'contacts'
    ],
    [
        '53', "14) I'll c___________ you as soon as I arrive. .",
        '도착하는 대로 당신에게 전화할게요.', 'contact'
    ],
    [
        '53',
        '15) The committee will try to i___________ the different ideas into one uniform plan. ',
        '그 위원회는 서로 다른 의견들을 모아 하나의 통일된 계획으로 만들려고 노력할 것이다.', 'integrate'
    ],
    [
        '53', '16) To a___________ your goal, you must never give up. ',
        '목적을 이루기 위해서는 절대 포기해서는 안 된다.', 'attain'
    ],
    [
        '53', '17) At last, she a___________ her dream of owning a home. ',
        '마침내, 그녀는 자신 소유의 집을 갖겠다는 꿈을 이뤘다.', 'attained'
    ],
    [
        '53', '18) The e___________audience was moved by his speech. ',
        '모든 청중이 그의 연설에 감동했다.', 'entire'
    ],
    [
        '53', '19) The suit was well t___________. .', '그 양복은 잘 만들어졌다.',
        'tailored'
    ],
    [
        '53', '20) A: Did you buy those clothes r___________ ? ',
        '저 옷들을 소매로 샀니?', 'retail'
    ],
    [
        '53',
        '21) Would you tell us about it i___________ more d___________ ? ',
        '그것에 대해 좀 더 자세히 말씀해 주시겠어요?', 'in, detail'
    ],
    [
        '53', '22) Can you guess what this package c___________ ? ',
        '이 소포 안에 무엇이 들었는지 알 수 있겠니?', 'contains'
    ],
    [
        '53',
        '23) The information c___________ in the letter really upset me. ',
        '편지에 담긴 내용은 나를 정말로 화나게 했다.', 'contained'
    ],
    [
        '53', '24) The children e___________ us with their singing. ',
        '아이들이 노래로 우리를 즐겁게 해주었다.', 'entertained'
    ],
    [
        '53', "25) When did you o___________ your driver's license? ",
        '당신은 언제 운전 면허증을 땄나요?', 'obtain'
    ],
    [
        '53',
        "26) He couldn't r___________ his prestige because of the scandal. ",
        '그는 그 스캔들 때문에 명성을 유지할 수 없었다.', 'retain'
    ],
    [
        '53', "27) I want to know how to s___________ my students' interest. ",
        '나는 나의 학생들의 관심을 지속시키는 방법을 알고 싶다.', 'sustain'
    ],
    [
        '53',
        "28) Do you think she'll be c___________ with your gift? Yes. She'll be satisfied with the c_______________ of the box ",
        '그녀가 네 선물에 만족할 거라고 생각하니? 응, 그녀는 상자 속의 내용물에 매우 만족할 거야. ',
        'content, contents'
    ],
    [
        '53', '29) Asia is larger than any other c___________ in the world. ',
        '아시아는 세계에서 가장 큰 대륙이다.', 'continent'
    ],
    [
        '53', '30) The rain c___________ all through the night. ',
        '비가 밤새도록 내렸다.', 'continued'
    ],
    [
        '54',
        '1) Each technician had a different t___________ for assembling the engines. ',
        '각 기술자들은 엔진들을 조립하는 데 필요한 서로 다른 기술을 가지고 있었다.', 'technique'
    ],
    [
        '54', '2) This product is made by using the latest t___________ . ',
        '이 제품은 최신 기술을 사용하여 만들어진다.', 'technology'
    ], ['54', '3) a t___________ climate ', '온화한 기후', 'temperate'],
    [
        '54', '4) Being t___________ at all things requires self-discipline. ',
        '매사에 절제하기 위해서는 자기 수양이 필요하다. ★', 'temperate'
    ],
    [
        '54', '5) T___________will drop below zero tonight. ',
        '오늘 밤 기온이 영하 이하로 떨어질 것입니다.', 'Temperatures'
    ],
    [
        '54', '6) My mom sent me to bed because I had a high t___________. ',
        '내 체온이 높아서 어머니께서 나를 잠자리에 들게 하셨다.', 'temperature'
    ],
    [
        '54',
        '7) Please calm down and c___________ y___________ t___________. ',
        '진정하고 화를 참도록 해봐. ★', 'control your temper'
    ],
    [
        '54',
        "8) The limit must be reasonable in terms of the child's age, t___________ , and developmental level. ",
        '제한은 아이의 나이와 기질, 발달 단계의 측면에서 합리적이어야한다.', 'temperament'
    ],
    [
        '54', '9) The effect of this medicine is t___________. ',
        '이 약의 효과는 일시적이다.', 'temporary'
    ],
    [
        '54', '10) I want a permanent job rather than a t___________ one. ',
        '나는 임시직보다는 정규직을 원한다.', 'temporary'
    ],
    [
        '54', '11) c___________ music/art/dance/literature ', '현대 음악/미술/무용/문학',
        'contemporary'
    ],
    [
        '54', '12) Bach was c___________ with Handel. ',
        '바흐는 헨델과 동시대 사람이었다. ★', 'contemporary'
    ],
    [
        '54',
        '13) A: On sunny days, I am t___________ to skip class and go to the beach. .',
        '나는 화창한 날에는 수업을 빼먹고 해변으로 가고 싶어.', 'tempted'
    ],
    [
        '54', '14) The prisoner a___________ to escape, but failed. ',
        '그 죄수는 탈출을 시도했으나, 실패했다.', 'attempted'
    ],
    [
        '54', '15) If your first a___________ is not successful, try again! ',
        '첫 번째 시도에서 성공하지 못하면, 다시 시도해 봐!', 'attempt'
    ],
    [
        '54', '16) Sue always a___________ this class. Sue .',
        'Sue는 항상 이 수업에 출석한다.', 'attends'
    ],
    [
        '54', '17) The Minister is a___________ by a staff of secretaries. ',
        '그 장관은 비서들의 시중을 받는다. ★', 'attended'
    ],
    [
        '54', '18) I have some matters I need to a___________ t___________ . ',
        '나는 처리해야 할 문제가 좀 있어. ★', 'attend to'
    ],
    [
        '54', '19) When she came in, he p___________ to be surprised. ',
        '그녀가 들어왔을 때, 그는 놀라는 척 했다.', 'pretended'
    ],
    [
        '54', '20) We e___________ our rental agreement for another year. ',
        '우리는 임대계약을 1년 더 연장했다.', 'extended'
    ],
    [
        '54', '21) This road e___________ to the port. .',
        '이 길은 항구까지 뻗어 있습니다.', 'extends'
    ],
    [
        '54', '22) He i___________ to study abroad next year. .',
        '그는 내년에 유학을 갈 작정이다.', 'intends'
    ],
    [
        '54',
        '23) He t___________ t___________ g___________ angry when people oppose his plans. .',
        '그는 사람들이 자기 계획에 반대하면 화를 내는 경향이 있다.', 'tends to get'
    ],
    [
        '54', '24) She t___________ her garden lovingly through the summer. ',
        '그녀는 여름 동안 사랑으로 정원을 돌보았다. ★', 'tended'
    ],
    [
        '54', '25) My steak is t___________ . How’s yours? ',
        '내 스테이크는 부드러워. 네 것은 어때?', 'tender'
    ],
    [
        '54',
        '26) The chief officer t___________ his resignation immediately. ',
        '그 최고 책임자는 즉시 사직서를 제출했다. ★', 'tendered'
    ],
    [
        '54', "27) I'm always so t___________ the night before an exam. .",
        '나는 시험 전날 항상 긴장을 한다.', 'tense'
    ],
    ['54', '28) the present/past/future t__________', '현재/과거/미래 시제', 'tense'],
    [
        '54', '29) Competition in the mobile phone industry is i___________',
        '휴대폰 업계의 경쟁이 심하다.', 'intense'
    ], ['54', '30) t___________ cancer ', '말기 암', 'terminal'],
    [
        '54', '31) He works in logistics at the end of the t___________ .',
        '그는 터미널 끝에더 물류 업무를 한다.', 'terminal'
    ],
    [
        '54', '32) Your contract t___________ in three months. ',
        '당신의 계약은 3개월 후에 종료됩니다.', 'terminates'
    ],
    [
        '54', '33) Quality d___________ the value of a product. .',
        '품질이 상품의 가치를 결정한다.', 'determines'
    ],
    [
        '54', '34) She was d___________ to succeed. .', '그녀는 성공하기로 결심했다.',
        'determined'
    ], ['54', '35) a medical/legal t___________', '의학[법률] 용어', 'term, terms'],
    [
        '54', "36) We're unbeatable in t___________ of price and service. ",
        '가격과 서비스 측면에서 우리는 어느 누구와도 상대가 되지 않는다. ★', 'terms'
    ],
    [
        '54', '37) We are on good[bad] t___________ with each other. ',
        '우리는 서로 사이가 좋다[나쁘다]. ★ ', 'terms'
    ],
    ['55', '1) a t___________ story[accident]', '무서운 이야기[끔찍한 사고]', 'terrible'],
    [
        '55',
        '2) Security has tightened up around the city due to the recent threat of t___________ . .',
        '최근 테러 위협으로 인해 도시의 경비가 강화되었다.', 'terror'
    ],
    [
        '55', '3) She was t___________ by the terrible monster. .',
        '그녀는 무시무시한 괴물 때문에 무서워했다.', 'terrified'
    ],
    [
        '55', '4) T___________ plants grow on land but not in water. ',
        '육상 식물은 육지에서는 자라지만, 수중에서는 그렇지 않다. ★', 'terrestrial'
    ],
    [
        '55',
        '5) The acquisition of new t___________ was a major preoccupation of the US government during the 19th century.',
        '새로운 영토의 획득은 19세기 동안 미 정부의 주된 관심사였다.', 'territory'
    ],
    [
        '55', '6) The man agreed to t___________ to help his friend. .',
        '그 남자는 친구를 도와주기 위해 증언하는 것에 동의했다.', 'testify'
    ],
    [
        '55', "7) I've never seen such a c___________ c___________. .",
        '난 그렇게 우열을 가리기 힘든 경기는 본 적이 없다.', 'close contest'
    ],
    [
        '55',
        '8) Students p___________ against the decision, but the p___________ was ignored.',
        '학생들은 그 결정에 항의했지만, 그 항의는 묵살되었다.', 'protested, protest'
    ],
    [
        '55', '9) This history book contains 300 pages of t___________ . ',
        '이 역사책은 300페이지의 본문으로 되어 있다.', 'text'
    ],
    [
        '55', "10) I'll t___________ you his cell phone number. .",
        '그의 핸드폰 번호로 문자를 보내줄게.', 'text'
    ],
    [
        '55',
        '11) The report should be considered within its social c___________ ',
        '그 보고서는 사회적 맥락 내에서 고찰되어야 한다. ★', 'context'
    ],
    [
        '55', '12) What does it mean in this c___________ ? ',
        '그것은 이 문맥에서 어떤 의미인가요?', 'context'
    ],
    [
        '55',
        '13) That t___________ factory produces the finest cotton fabric. .',
        '그 직물 공장은 최고급의 면직물을 생산한다.', 'textile'
    ],
    [
        '55',
        '14) If frozen quickly, freshly caught fish will keep their taste and t___________. .',
        '갓 잡힌 물고기가 빨리 냉동되면 그 맛과 질감이 보존될 것이다.', 'texture'
    ],
    [
        '55', '15) My uncle is a t___________ scholar. .', '우리 삼촌은 신학자이다.',
        'theological'
    ],
    [
        '55', '16) Their e___________ helped the team win. .',
        '그들의 열광은 그 팀이 승리하는 것을 도왔다.', 'enthusiasm'
    ],
    [
        '55',
        '17) Make sure to include your t___________ statement in your introduction. ',
        '도입부에 당신의 논지를 꼭 포함하세요', 'thesis'
    ],
    [
        '55',
        '18) Every good experiment needs a well-developed h___________. ',
        '모든좋은 실험은 잘 다듬어진 가설을 필요로한다. ★', 'hypothesis'
    ],
    [
        '55', '19) My niece is having a Baby Shark t___________ party. .',
        '우리 조카는 <아기상어>를 주제로 하는 파티를 가질 예정이다.', 'theme'
    ],
    [
        '55', '20) She said it in an angry t___________. .', '그녀는 성난 어조로 말했다.',
        'tone'
    ],
    [
        '55',
        '21) The i___________ of a sentence can have a big impact on its interpretation. .',
        '문장의 억양은 해석에 지대한 영향을 미칠 수 있다.', 'intonation'
    ],
    [
        '55',
        "22) The teacher's m___________ tone of voice was a terrific sleeping pill. ",
        '선생님의 단조로운 억양의 목소리는 엄청난 수면제였다.★', 'monotonous'
    ],
    [
        '55', '23) The piano is in t___________ [out of t___________]. ',
        '그 피아노는 음이 맞는다[맞지 않는다].', 'tune'
    ],
    [
        '55',
        "24) We'll come back with more new movies. So stay t___________. ",
        '더 많은 새로운 영화들과 함께 돌아오겠습니다. 채널 고정하세요.', 'tuned'
    ],
    [
        '55', '25) T___________cannot be justified under any circumstances. .',
        '고문은 어떤 상황에서도 정당화 될 수 없다.', 'Torture'
    ],
    [
        '55', '26) The reporter d___________ the truth. ', '그 기자는 사실을 왜곡했다. ★',
        'distorted'
    ],
    [
        '55', '27) He was t___________ by feelings of guilt. . ',
        '그는 죄책감으로 괴로워했다. ', 'tormented'
    ],
    [
        '56', '1) Beauty and truth are a___________ ideas. .',
        '미와 진실은 추상적인 개념이다.', 'abstract'
    ],
    [
        '56', "2) We've a___________ the data from the experiment. ",
        '우리는 그 실험에서 데이터를 추출했다. ★', 'abstracted'
    ],
    [
        '56',
        '3) What a___________ me most to Seoul is the variety of shopping malls. .',
        '내가 서울에 가장 끌리는 점은 다양한 쇼핑몰들이다.', 'attracts'
    ],
    [
        '56', '4) Wood expands when wet and c___________ when dry. ',
        '목재는 젖으면 팽창하고, 마르면 수축한다. ★', 'contracts'
    ], ['56', '5) a(n) employment[hiring] c___________', '고용계약', 'contract'],
    [
        '56', "6) Don't d___________ me ― I'm trying to study. . ",
        '나를 산만하게 하지 마. 나 공부하려고 하니까', 'distract'
    ],
    [
        '56',
        '7) The dentist was distracted by the noise and e___________ the wrong tooth. ',
        '치과 의사는 소음으로 주의가 산만해져 엉뚱한 이를 뽑았다.', 'extracted'
    ],
    [
        '56', '8) T___________ others the way you want to be t___________. .',
        '대우받고 싶은 대로 남을 대하여라.', 'Treat, treated'
    ],
    [
        '56', "9) I'll t___________ you this time. ", '이번에는 제가 대접할게요(한턱낼게요) ★',
        'treat'
    ],
    [
        '56', '10) That trade t___________ was signed by five countries. ',
        '그 무역 협정은 5개국에 의해서 체결되었다.', 'treaty'
    ],
    [
        '56', '11) The troops could neither advance nor r___________ . ',
        '그 군대는 전진하지도 후퇴하지도 못했다. ★', 'retreat'
    ],
    ['56', '12) She t___________ the suspect. .', '그녀는 용의자를 추적했다.', 'traced'],
    [
        '56', '13) The island vanished without a t___________. .',
        '그 섬은 흔적도 없이 사라졌다.', 'trace'
    ],
    [
        '56',
        "A: I'll t_____________ the rabbit through the woods. B: Don't lose t__________ of it. It ate all the carrots in the barn. ",
        '나는 숲 속으로 그 토끼를 추적하러 갈 거야. 놓치지마. 그 녀석이 헛간의 당근을 모두 먹었어.',
        'track, lose track of'
    ],
    [
        '56', '15) Her long dress was t___________ on the floor. .',
        '그녀의 긴 원피스가 바닥에 질질 끌렸다. ', 'trailing'
    ],
    [
        '56', "16) Keep to the t___________ and you won't get lost. ",
        '그냥 이 길만 따라 가요. 그러면 길을 잃지 않을 거예요.', 'trail'
    ],
    [
        '56',
        '17) There are personality t___________ and characteristics commonly associated with entrepreneurs. .',
        '기업가들과 흔히 연관되는 성격 특성과 특징들이 있다.', 'traits'
    ],
    [
        '56', '18) The portrait p___________ him as strong and noble. .',
        '그 초상화는 그를 강인하고 기품있게 묘사하고 있다.', 'portrays'
    ],
    [
        '56', '19) Buddhism has a long t___________ in Korea. .',
        '불교는 한국에서 오랜 전통을 지니고 있다.', 'tradition'
    ],
    [
        '56', '20) He b___________ his country to save his own life. .',
        '그는 살아남기 위해 조국을 배반했다.', 'betrayed'
    ],
    [
        '56',
        '21) I could not tell if he was t___________ with fear or shivering from the cold. .',
        '나는 그가 공포로 떨고 있는지 아니면 추워서 떨고 있는지 분간할 수 없었다.', 'trembling'
    ],
    [
        '56', '22) She has a t___________ amount of property. .',
        '그녀는 막대한 재산이 있다.', 'tremendous'
    ],
    [
        '56',
        '23) Korean singers are enjoying t___________ popularity all over Asia. .',
        '한국 가수들은 아시아 전역에서 엄청난 인기를 누리고 있다.', 'tremendous'
    ],
    [
        '56',
        "24) He a___________ his success t___________ other people's help. ",
        '그는 자신의 성공을 다른 사람들의 도움 덕택으로 돌렸다. ★', 'attributed, to'
    ],
    [
        '56', '25) He c___________ a lot of money to the charity. .',
        '그는 자선 단체에 많은 돈을 기부했다.', 'contributed'
    ],
    [
        '56',
        '26) A proper amount of exercise c___________ t___________ good health. .',
        '적당량의 운동은 건강에 도움이 된다.', 'contributes to'
    ],
    [
        '56', '27) The government d___________ free food to flood victims. .',
        '정부는 수재민들에게 무상으로 음식을 배급했다.', 'distributed'
    ],
    [
        '56', '28) I find it difficult to t___________ him. ',
        '나는 그를 신뢰하기는 힘들다고 생각한다.(그는 믿음직하지 않다.)', 'trust'
    ],
    [
        '56',
        '29) I e___________ my estate to him. (= I e___________ him with my estate.) .',
        '나는 내 재산을 그에게 위탁했다.', 'entrusted'
    ],
    [
        '56', '30) Please give me a t___________ account of what happened. . ',
        '무슨 일이 일어났는지 제게 솔직하게 설명해주세요. ', 'truthful'
    ],
    [
        '57',
        "1) I don't want to i___________ o___________ you if you're busy. .",
        '만약 당신이 바쁘다면 방해하고 싶지 않아요.', 'intrude on'
    ],
    [
        '57',
        '2) He t___________ his hand into the hole to find out what was there. .',
        '그는 구멍 안에 무엇이 있는지 알아내려고 손을 찔러 넣었다.', 'thrust'
    ],
    [
        '57', "3) the main t___________ of government's economic policy ",
        '정부 경제 정책의 주요 요점 ★', 'thrust'
    ],
    [
        '57', '4) The t___________ of terrorism is still present. .',
        '테러의 위협은 여전히 존재한다.', 'threat'
    ],
    [
        '57', '5) The sign said, “Please do not d___________ .”',
        "표지판에는 '방해하지 마세요'라고 쓰여 있었다.", 'disturb'
    ],
    [
        '57',
        '6) Did you have much t___________ getting tickets to the musical? ',
        '그 뮤지컬 티켓을 구하는 데 어려움이 많았나요?', 'trouble getting'
    ],
    [
        '57',
        '7) Some countries have a___________ natural resources, like coal or oil. ',
        '몇몇 나라들은 석탄이나 석유같은 천연자원이 풍부하다', 'abundant'
    ],
    [
        '57', '8) He was s___________ by the crowed. .',
        '그는 많은 사람들에 둘러싸여 있었다.', 'surrounded'
    ],
    [
        '57',
        '9) The u___________ pollution of Seoul is spreading to the nearby suburbs. ',
        '서울 도심의 오염이 주변 교외지역으로 퍼지고 있다.', 'urban'
    ],
    [
        '57',
        '10) Many people who work in the city live in the s___________ . ',
        '도시에서 일하는 많은 사람들이 교외에 산다.', 'suburbs'
    ],
    [
        '57', '11) It is no u___________ trying to make him hurry. ',
        '그를 서두르게 하려고 해봐야 소용없어.', 'use'
    ],
    [
        '57', '12) No one should a___________ animals. ',
        '누구도 동물을 학대해서는 안 된다. ★', 'abused'
    ],
    [
        '57',
        '13) Politicians who a___________ their privileges will be investigated. .',
        '특권을 남용하는 정치인들은 조사를 받을 것이다.', 'abuse'
    ], ['57', '14) drug a___________ ', '약물 남용', 'abuse'],
    [
        '57',
        '15) The cooking u___________ are in that drawer next to the stove. .',
        '주방(조리) 기구는 레인지 옆 서랍 안에 있어.', 'utensils'
    ],
    [
        '57',
        '16) Major public u___________ include gas, electricity, and water. ',
        '주요 공공 사업은 가스와 전기, 수도를 포함한다.', 'utilities'
    ],
    [
        '57',
        '17) William the Conqueror i___________ England in the 11th century.',
        '정복왕 윌리엄은 11세기 영국을 침략했다', 'invaded'
    ],
    [
        '57', '18) Give me a direct answer, and stop e___________ the issue. ',
        '문제를 회피하지 말고 단도직입적으로 대답해라. ★', 'evading'
    ],
    [
        '57', '19) I have only a v___________ idea of the plan. .',
        '나는 그 계획에 대한 막연한 생각만 있다.', 'vague'
    ],
    [
        '57', '20) A v___________ shape appeared through the fog. .',
        '어렴풋한 형체가 연기 속에서 나타났다.', 'vague'
    ],
    [
        '57', '21) The woman has very e___________ taste in furniture. ',
        '그 여자는 가구에 매우 사치스러운 취향이 있다. ★', 'extravagant'
    ], ['57', '22) e___________ demand ', '지나친 요구', 'extravagant'],
    [
        '57',
        '23) The v___________ of a diamond is based on several factors. .',
        '다이아몬드의 가치는 여러 가지 요소에 기초한다.', 'value'
    ],
    [
        '57', '24) Korean parents v___________ education highly. ',
        '한국의 부모들은 교육을 아주 중요시한다. ★', 'value'
    ],
    [
        '57', '25) This pottery is v___________ at 50 dollars.',
        '이 도자기는 50달러로 평가된다.', 'valued'
    ],
    [
        '57',
        "26) The shop has only been open for six months, so it's too early to e___________ its success.",
        '그 가게는 개업한 지 겨우 6개월밖에 되지 않았기 때문에 그 성공 여부를 평가하기에는 너무 이르다.', 'evaluate'
    ],
    [
        '57', '27) Your passport is no longer v___________ . ',
        '당신의 여권은 유효하지 않습니다. ★', 'valid'
    ],
    [
        '57', '28) Is a bigger size a___________ ? ', '더 큰 사이즈를 이용할 수 있습니까?',
        'available'
    ],
    [
        '57', '29) Are you a___________ this Sunday? ', '이번 주 일요일에 시간 있니? ★',
        'available'
    ],
    [
        '57', '30) the p___________ public opinion on the issue ',
        '그 안건에 대한 지배적인 여론', 'prevailing'
    ], ['57', '31) Justice will p___________. ', '정의는 승리할 것이다. ★', 'prevail'],
    [
        '57', '32) The cat v___________ into the darkness. ',
        '그 고양이는 어둠 속으로 사라져버렸다. ★', 'vanished'
    ],
    [
        '57', '33) He tried in v___________ to finish the project on time. ',
        '그는 프로젝트를 제때 마치려고 했지만 허사였다. ★', 'vain'
    ],
    [
        '57', '34) There are some doctors who a___________ paying taxes. .',
        '탈세를 하는 몇몇 의사들이 있다.', 'avoid'
    ],
    [
        '57', '35) A: Do you have any v___________ rooms? ?', '빈 방 있습니까?',
        'vacant,'
    ],
    [
        '57',
        '36) As we all know, the term "v___________" is an inappropriate name because there exists no v___________ in a v___________ cleaner.',
        '우리 모두가 알듯이, ‘진공’이라는 용어는 부적절한 이름인데, 진공 청소기에는 진공이 존재하지 않기 때문이다. ',
        'vacuum'
    ],
    [
        '58',
        "1) I've visited v___________ theme parks, but this one is the best. .",
        '나는 다양한 놀이공원에 가보았지만 이번이 최고다.', 'various'
    ],
    [
        '58',
        '2) Rates for housing loans are usually fixed or v___________ . .',
        '주택 이자율은 보통 고정이거나 변동이다.', 'variable'
    ],
    [
        '58',
        "3) It's difficult to control so many v___________ in an experiment. ",
        '그렇게 많은 변수를 한 실험에서 통제하기는 어렵다. ★', 'variables'
    ],
    [
        '58',
        "4) It's important to use some color v___________ when making an image look realistic. ",
        '이미지를 현실적으로 보이게 할 때 색 차이를 사용하는 것이 중요하다', 'variation'
    ],
    [
        '58', "5) He swore he would a___________ his brother's death. .",
        '그는 형의 죽음을 복수하겠다고 맹세했다.', 'avenge'
    ],
    [
        '58',
        '6) My cousin stole my piece of pie, so I took r___________ by putting a cricket in his bed. .',
        '내 사촌이 파이를 훔쳐서 나는 그의 침대에 귀뚜라미를 넣는 것으로 복수했다.', 'revenge'
    ],
    [
        '58', '7) He got back safe from his a___________ in Africa. .',
        '그는 아프리카의 모험에서 무사히 돌아왔다.', 'adventure'
    ],
    [
        '58',
        '8) V___________ capital investment is a high-risk, high-return field. .',
        '벤처 사업투자는 위험도 높고 보상도 높은 분야이다.', 'Venture'
    ],
    [
        '58', '9) They v___________ deep into the jungle. .',
        '그들은 위험을 무릅쓰고 정글 깊이 들어갔다.', 'ventured'
    ],
    [
        '58',
        '10) The Democratic and Republican Parties hold c___________ every four years. ',
        '민주당과 공화당은 4년마다 집회를 갖는다.', 'conventions'
    ],
    [
        '58',
        "11) The e___________ brought the company's eventual collapse. .",
        '그 사건은 그 회사의 최종적인 붕괴를 가져왔다.', 'event'
    ],
    [
        '58',
        '12) Sarah Breedlove i___________ a successful hair care product and sold it across the country. Sarah Breedlove .',
        'Sarah Breedlove는 성공적인 모발관리 제품을 발명해서 전국에 팔았다.', 'invented'
    ],
    [
        '58', '13) The heavy rain p___________ me from going out. .',
        '나는 폭우 때문에 외출하지 못했다.', 'prevented'
    ],
    [
        '58',
        '14) Fifth A___________in New York is one of the most expensive and elegant shopping districts in the world. .',
        '뉴욕의 5번가는 세계에서 가장 비싸고 고상한 쇼핑구역 중 하나다.', 'Avenue'
    ],
    [
        '58', 'When is the most c_______________ time for you to come?',
        '오시기에 가장 편리한 시간은 언제입니까?', 'convenient'
    ],
    [
        '58', '16) The government i___________ in the strike. ',
        '정부는 그 파업에 개입했다. ★', 'intervened'
    ],
    [
        '58', '17) We bought several s___________ in Thailand. ',
        '우리는 태국에서 여러 개의 기념품을 샀다. ', 'souvenirs'
    ],
    [
        '58', '18) They a___________ their new product on TV. TV .',
        '그들은 신제품을 에 광고한다.', 'advertise'
    ],
    [
        '58', '19) The warehouse was c___________ into apartments. .',
        '그 창고는 아파트로 개조되었다.', 'converted'
    ],
    [
        '58', '20) V___________ stripes on clothing make people look taller. ',
        '옷의 세로 줄무늬는 사람의 키를 더 커보이게 한다. ★', 'Vertical'
    ],
    [
        '58',
        '21) All squares are rectangles, but the c___________ ㅡ that all rectangles are squares ㅡ is not true. ',
        '모든 정사각형들은 사각형이지만 반대로 모든 사각형은 정사각형이라는 것은 사실이 아니다.', 'converse'
    ],
    [
        '58',
        '22) A person of d___________ interests can talk about many subjects. .',
        '다양한 관심사를 가진 사람은 많은 주제에 관해 이야기할 수 있다.', 'diverse'
    ],
    [
        '58', '23) The court r___________ the judgement. .', '법원은 판결을 뒤집었다.',
        'reversed'
    ],
    ['58', '24) I drove my car in r___________ . .', '나는 차를 후진했다.', 'reverse'],
    [
        '58', "25) The tune is his, but the v___________ are his mother's. .",
        '그가 곡을 쓰고 그의 어머니가 가사를 썼다.', 'verses'
    ],
    [
        '58', "26) The book is a modern v___________ of 'Romeo and Juliet.' ",
        "그 책은 현대판 '로미오와 줄리엣'이다.", 'version'
    ],
    [
        '58',
        '27) The two news media gave different v___________ of what happened. .',
        '두 뉴스 매체는 일어난 사건에 대해 다른 해석을 내놓았다.', 'versions'
    ],
    [
        '58',
        '28) The couple decided to get counseling before getting d___________. . ',
        '그 부부는 이혼을 하기 전에 상담을 받기로 결정했다. ', 'divorced'
    ],
    [
        '59', '1) This flight goes to Houston v___________ Miami. ',
        '이 비행기는 마이애미를 경유해서 휴스턴으로 갑니다. ★', 'via'
    ],
    [
        '59', '2) Can you send us a résumé v___________ email? ',
        '이메일로 이력서를 보내주시겠어요? ★', 'via'
    ],
    [
        '59',
        '3) People do not argue against an o___________ fact for no reason. .',
        '사람들은 아무 이유없이 분명한 것에 대해 언쟁하지는 않는다.', 'obvious'
    ], ['59', '4) a p___________ engagement[appointment] ', '선약', 'previous'],
    [
        '59', "5) I can't c___________ my feelings in words. .",
        '나는 내 감정을 말로 전할 수 없다.', 'convey'
    ],
    [
        '59', '6) This pipeline c___________ oil across the country. .',
        '이 수송관은 전국적으로 석유를 수송한다.', 'conveys'
    ],
    [
        '59',
        '7) Nelly Bly took a v___________ around the world in 1889. 1889 ',
        '넬리 블라이는 1889년에 세계 일주를 했다. ★', 'voyage'
    ],
    [
        '59', '8) It was teamwork that led them to v___________ .',
        '그들을 승리로 이끈 것은 팀워크였다.', 'victory'
    ],
    [
        '59',
        '9) If c___________ , they face up to one year in prison and a fine of ten million won.',
        '유죄 판결을 받을 경우, 그들은 1년 이하의 징역 또는 천만 원 이하의 벌금에 처해진다.', 'convicted'
    ],
    [
        '59',
        '10) I tried to c___________ them of the value of animal life. .',
        '나는 그들에게 동물의 생명의 가치를 납득시키려고 애썼다.', 'convince'
    ],
    [
        '59', '11) She failed to c___________ her mother to see a doctor. .',
        '그녀는 자신의 어머니가 진찰을 받도록 설득하는 데 실패했다.', 'convince,'
    ],
    [
        '59', '12) The teacher d___________ the students into three groups. .',
        '선생님은 학생들을 세 그룹으로 나누었다.', 'divided'
    ],
    [
        '59',
        '13) The National Assembly was d___________ on approving the bill. .',
        '국회는 그 법안의 승인여부를 놓고 분열되었다.', 'divided'
    ],
    [
        '59',
        '14) The rights of the i___________ are the most important in democracy. .',
        '민주주의 사회에서는 개인의 권리가 중요하다.', 'individual'
    ],
    [
        '59',
        '15) Because of problems with the current device , engineers are d___________ a new model. ',
        '현재 사용하고 있는 (기계) 장치의 문제들 때문에, 기술자들은 새로운 모델을 고안하고 있다.', 'devising'
    ],
    [
        '59',
        '16) Mrs. Jones became a w___________ after her husband died of cancer. .',
        '존스부인은 남편이 암으로 죽은 후 미망인이 되었다.', 'widow'
    ],
    [
        '59', '17) For a man of 80, he still has surprising v___________ . .',
        '여든의 나이에 비해 그는 여전히 놀라운 기력을 가지고 있다.', 'vigor'
    ],
    [
        '59', '18) She has a clear v___________ of the future she wants. .',
        '그녀는 자신이 원하는 확실한 미래상을 가지고 있다.', 'vision'
    ],
    [
        '59',
        '19) She needs to r___________ her essay before she gives it to her teacher. .',
        '선생님께 숙제를 내기 전에 그것을 수정할 필요가 있다.', 'revise'
    ],
    [
        '59',
        '20) He s___________ all the students taking the English examination. .',
        '그는 영어 시험을 치르는 모든 학생들을 감독했다.', 'supervised'
    ],
    [
        '59',
        "21) The police didn't have enough e___________ to convict the suspect. .",
        '경찰은 그 용의자가 유죄라고 입증할 만한 충분한 증거가 없었다.', 'evidence'
    ],
    [
        '59',
        '22) He p___________ the stranger with food. (=He p___________ food for the stranger.) .',
        '그는 그 낯선 사람에게 음식을 제공하였다.', 'provided'
    ],
    [
        '59', '23) I work hard to p___________ for my family. .',
        '나는 내 가족을 부양하기 위해 열심히 일한다.', 'provide'
    ],
    [
        '59',
        '24) Many viewers are criticizing the prejudiced v___________ of the broadcaster. .',
        '많은 시청자들이 그 방송인의 편파적인 시각을 비판하고 있다.', 'view'
    ],
    [
        '59', '25) The rare bird suddenly disappeared from v___________. . ',
        '그 희귀새는 갑자기 사라졌다. ', 'view'
    ],
    [
        '59', '26) The v___________from the top of the hill is marvelous. .',
        '언덕 꼭대기에서 보이는 풍경이 훌륭하다.', 'view'
    ],
    [
        '59', '27) How did your job i___________ go? ', '네 구직 면접은 어떻게 되었니?',
        'interview'
    ],
    [
        '59', '28) The president gave a formal i___________ .',
        '대통령이 공식 회견을 했다.', 'interview'
    ],
    [
        '59',
        "29) I haven't read a positive r___________ of that movie yet. .",
        '나는 아직 그 영화에 대한 호평을 읽어보지 못했다.', 'review'
    ],
    [
        '59', '30) We must r___________ our economic situation. .',
        '우리는 우리의 경제 상황을 재검토해야 한다.', 'review'
    ],
    [
        '59', "31) Let's r___________ what you learned in our last class. .",
        '지난 수업에서 배운 것을 복습하자.', 'review'
    ],
    [
        '59', '32) We often e___________ those who have more than us. .',
        '우리는 종종 우리보다 더 많이 가진 사람들을 부러워한다.', 'envy'
    ], ['59', '33) a s___________ of public opinion ', '여론 조사', 'survey'],
    [
        '59',
        "34) A market s___________ was taken to learn consumers' likes and dislikes. . ",
        '소비자들의 기호를 알아보기 위해 시장 조사가 이루어졌다. ', 'survey'
    ],
    [
        '60',
        '1) Most garment workers were paid barely enough to s___________ . ',
        '대부분의 옷을 만드는 노동자들은 겨우 생존할 만큼의 임금밖에 받지 못했다.', 'survive'
    ],
    [
        '60',
        '2) Only one passenger s___________ the terrible airplane crash. .',
        '오직 한명의 탑승자만이 그 끔찍한 비행기 추락 하사고에서 살아남았다.', 'survived'
    ],
    [
        '60',
        '3) We have a v___________ memories of our exciting adventure in the Himalayan Mountains. ',
        '우리는 히말라야 산맥에서의 흥미진진한 모험을 생생하게 기억하고 있다.', 'vivid'
    ],
    [
        '60',
        '4) Vitamin E plays a v___________ role in improving circulation. ',
        '비타민 는 혈액 순환 개선에 매우 중요한 역할을 한다.', 'vital'
    ],
    [
        '60',
        '5) The v___________ organs organs are very sensitive to temperature and humidity. ',
        '발성 기관은 온도와 습도에 매우 민감하다. ★', 'vocal'
    ],
    [
        '60', '6) He has a large English v___________ .', '그는 영어 어휘가 풍부하다.',
        'vocabulary'
    ],
    [
        '60',
        '7) "Nursing," said Florence Nightingale, "is a v___________ as well as a profession." ',
        '플로렌스 나이팅게일은 “간호하는 일은 직업일 뿐만 아니라 소명이기도 하다”라고 말했다.', 'vocation'
    ],
    [
        '60', '8) I a___________ a policy of gradual reform. ',
        '나는 점진적인 개혁 정책을 지지한다. ★', 'advocate'
    ],
    [
        '60', '9) He is an a___________ of free trade. .', '그는 자유무역 옹호자이다.',
        'advocate'
    ],
    [
        '60', '10) His story e___________ public sympathy. .',
        '그의 이야기는 대중의 연민을 자아냈다.', 'evoked'
    ],
    [
        '60', '11) It would be unwise to p___________ a sleeping lion. .',
        '잠자는 사자를 화나게 하는 건 현명하지 않아.', 'provoke'
    ],
    [
        '60',
        "12) The Red Cross Blood Campaign needs people's v___________ participation. ",
        '적십자의 헌혈 운동은 사람들의 자발적인 참여가 필요하다.', 'voluntary'
    ],
    [
        '60', '13) More and more students are doing v___________ work. .',
        '자원봉사활동을 하는 학생들이 점점 더 늘고 있다.', 'voluntary'
    ],
    [
        '60',
        "14) Darwin's theory of evolution claims that life has e___________ over time. .",
        '다윈의 진화론은 생물이 시간이 지나면서 진화해왔다고 주장한다.', 'evolved'
    ],
    [
        '60', '15) R___________ doors can conserve energy. .',
        '회전문은 에너지를 절약할 수 있다.', 'Revolving'
    ],
    [
        '60', '16) His new position i___________ increased responsibility. ',
        '그의 새 직책은 더 많은 책임을 수반한다.', 'involves'
    ],
    [
        '60', "17) Don't i___________ me in your quarrel. ",
        '나를 너희들의 말다툼에 끌어들이지 마.', 'involve'
    ],
    [
        '60', '18) The liquid was 5 liters in v___________. ',
        '그 액체의 양은 5리터였다.', 'volume'
    ],
    [
        '60', '19) We own a library of 500 v___________. ',
        '19우리는 500권의 장서를 가지고 있다. ', 'volumes'
    ],
    [
        '60',
        "20) You should v___________ if you care about your country's future. ",
        '너는 나라의 미래를 생각한다면 투표해야한다.', 'vote'
    ],
    [
        '60',
        '21) Emily d___________ her spare time t___________ helping the elderly. Emily ',
        'Emily는 여가를 노인들을 돕는데 헌신한다.', 'devotes'
    ],
    [
        '60', '22) The actress was a___________ an Academy A___________ . ',
        '그 여배우는 아카데미 상을 수상했다.', 'awarded, Award'
    ],
    [
        '60',
        '23) Our salaries were increased as a r___________ for our efforts. 우리의 노고에 대한 보상으로 월급이 인상되었다.',
        '우리의 노고에 대한 보상으로 월급이 인상되었다.', 'reward'
    ],
    [
        '60',
        '24) I’m fully a___________ of the problem. 나는 그 문제를 아주 잘 인식하고 있다.',
        '나는 그 문제를 아주 잘 인식하고 있다.', 'aware'
    ],
    [
        '60',
        '25) My mother w___________ me about staying out late. 엄마는 나에게 늦게 다니는 것에 대해 주의를 주셨다.',
        '엄마는 나에게 늦게 다니는 것에 대해 주의를 주셨다. ', 'warned'
    ]
]
quiz_list = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz', methods=['POST'])
def quiz():
    global quiz_list
    selected_days = request.form.getlist('days')  # 체크된 날짜 가져오기

    # 선택된 날짜에 맞는 퀴즈 데이터를 필터링
    quiz_list = [entry for entry in data if entry[0] in selected_days]

    shuffle(quiz_list)  # 퀴즈 순서 섞기

    if not quiz_list:
        return render_template('done.html', message="선택한 day에 해당하는 퀴즈가 없습니다.")

    return render_template('quiz.html', quiz=quiz_list[0],
                           rest=len(quiz_list))  # rest 값 전달


@app.route('/check', methods=['POST'])
def check():
    global quiz_list
    answer = request.form['answer'].strip().lower()
    correct_answer = quiz_list[0][3].lower()

    if answer == correct_answer:
        quiz_list.pop(0)  # 정답을 맞히면 퀴즈에서 제거
        if len(quiz_list) == 0:
            return render_template('done.html')  # 모든 퀴즈를 맞힌 경우
        else:
            return render_template('quiz.html',
                                   quiz=quiz_list[0],
                                   result="정답!",
                                   rest=len(quiz_list))  # 정답 메시지와 남은 단어 수
    else:
        quiz_list.append(quiz_list.pop(0))
        return render_template('quiz.html',
                               quiz=quiz_list[0],
                               result=f"오답! 정답은 '{correct_answer}' 입니다.",
                               rest=len(quiz_list))  # 오답 메시지와 남은 단어 수


if __name__ == '__main__':
    app.run(debug=True)
