#!/usr/bin/env python
# coding: utf-8

# In[50]:


data_text= """Buffalo Bills at Los Angeles Rams	Thursday, Sep 8
BUF 451
Cover: +19
31@10
FINAL	452 LA
Under: 41
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BUF	-2	-125		0-0	0-0-0	0-0-0	25.8	52.7
LA	+2	+105	52	0-0	0-0-0	0-0-0	26.8	-1
Referee: C CHEFFERS ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BUF	J ALLEN	0	0.0	0	0	0.0	0.0	0.0
LA	M STAFFORD	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BUF	-2.5	65%	66%	-130	55%	52%	o52	49%	62%
LA	+2.5	35%	34%	+110	45%	48%	u52	51%	38%
Baltimore Ravens at New York Jets	Sunday, Sep 11
BAL 453
Cover: +8.5
24@9
FINAL	454 NYJ
Under: 33
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BAL	-6.5	-320		0-0	0-0-0	0-0-0	24.5	46.4
NYJ	+6.5	+260	44	0-0	0-0-0	0-0-0	21.9	+2.6
Referee: C WROLSTAD ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BAL	L JACKSON	0	0.0	0	0	0.0	0.0	0.0
NYJ	J FLACCO	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BAL	-6.5	87%	88%	-285	87%	92%	o44	41%	47%
NYJ	+6.5	13%	12%	+240	13%	8%	u44	59%	53%
New Orleans Saints at Atlanta Falcons	Sunday, Sep 11
NO 455
Over: 53
27@26
FINAL	456 ATL
Cover: +4.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NO	-5.5	-240		0-0	0-0-0	0-0-0	23.3	42.9
ATL	+5.5	+200	43½	0-0	0-0-0	0-0-0	19.6	+3.8
Referee: A KEMP ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NO	J WINSTON	0	0.0	0	0	0.0	0.0	0.0
ATL	M MARIOTA	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NO	-5.5	73%	77%	-250	73%	85%	o44	77%	67%
ATL	+5.5	27%	23%	+210	27%	15%	u44	23%	33%
New England Patriots at Miami Dolphins	Sunday, Sep 11
NE 457
Under: 27
7@20
FINAL	458 MIA
Cover: +10
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NE	+3	+145		0-0	0-0-0	0-0-0	20.8	44
MIA	-3	-165	46½	0-0	0-0-0	0-0-0	23.2	-2.4
Referee: J HUSSEY ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NE	M JONES	0	0.0	0	0	0.0	0.0	0.0
MIA	T TAGOVAILOA	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NE	+3	51%	44%	+145	50%	44%	o46	20%	40%
MIA	-3	49%	56%	-170	50%	56%	u46	80%	60%
Cleveland Browns at Carolina Panthers	Sunday, Sep 11
CLE 459
Cover: +3.5
26@24
FINAL	460 CAR
Over: 50
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CLE	+1.5	+105		0-0	0-0-0	0-0-0	23.3	43.8
CAR	-1.5	-125	42	0-0	0-0-0	0-0-0	20.4	+2.9
Referee: B ROGERS ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CLE	J BRISSETT	0	0.0	0	0	0.0	0.0	0.0
CAR	B MAYFIELD	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CLE	+1.5	24%	20%	+100	30%	23%	o42	48%	53%
CAR	-1.5	76%	80%	-120	70%	77%	u42	52%	47%
Pittsburgh Steelers at Cincinnati Bengals	Sunday, Sep 11
PIT 461
Cover: +10
23@20
FINAL	462 CIN
Under: 43
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PIT	+7	+270		0-0	0-0-0	0-0-0	19.6	44.7
CIN	-7	-330	44½	0-0	0-0-0	0-0-0	25.1	-5.5
Referee: S HOCHULI ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PIT	M TRUBISKY	0	0.0	0	0	0.0	0.0	0.0
CIN	J BURROW	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PIT	+7	49%	37%	+265	30%	16%	o44.5	71%	64%
CIN	-7	51%	63%	-320	70%	84%	u44.5	29%	36%
San Francisco 49ers at Chicago Bears	Sunday, Sep 11
SF 463
Under: 29
10@19
FINAL	464 CHI
Cover: +15.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SF	-6.5	-280		0-0	0-0-0	0-0-0	24.1	43.1
CHI	+6.5	+240	38	0-0	0-0-0	0-0-0	19.1	+5
Referee: C MARTIN ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SF	T LANCE	0	0.0	0	0	0.0	0.0	0.0
CHI	J FIELDS	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SF	-6	59%	63%	-255	70%	81%	o38.5	29%	44%
CHI	+6	41%	37%	+215	30%	19%	u38.5	71%	56%
Philadelphia Eagles at Detroit Lions	Sunday, Sep 11
PHI 465
Over: 73
38@35
FINAL	466 DET
Cover: +3
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PHI	-6	-250		0-0	0-0-0	0-0-0	25.7	47.6
DET	+6	+210	48½	0-0	0-0-0	0-0-0	21.8	+3.9
Referee: B ALLEN ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PHI	J HURTS	0	0.0	0	0	0.0	0.0	0.0
DET	J GOFF	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PHI	-6	66%	69%	-255	68%	79%	o49	65%	46%
DET	+6	34%	31%	+215	32%	21%	u49	35%	54%
Indianapolis Colts at Houston Texans	Sunday, Sep 11
IND 467
Under: 40
20@20
FINAL	468 HOU
Cover: +7
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
IND	-7	-340		0-0	0-0-0	0-0-0	28	44.9
HOU	+7	+280	45½	0-0	0-0-0	0-0-0	16.8	+11.2
Referee: L CLARK ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
IND	M RYAN	0	0.0	0	0	0.0	0.0	0.0
HOU	D MILLS	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
IND	-7	71%	78%	-300	84%	92%	o46	64%	47%
HOU	+7	29%	22%	+250	16%	8%	u46	36%	53%
Jacksonville Jaguars at Washington Commanders	Sunday, Sep 11
JAC 469
Over: 50
22@28
FINAL	470 WAS
Cover: +3
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
JAC	+3	+130		0-0	0-0-0	0-0-0	19.9	45.4
WAS	-3	-150	43½	0-0	0-0-0	0-0-0	25.5	-5.6
Referee: T BLAKE ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
JAC	T LAWRENCE	0	0.0	0	0	0.0	0.0	0.0
WAS	C WENTZ	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
JAC	+3	54%	56%	+125	58%	55%	o43	49%	40%
WAS	-3	46%	44%	-145	42%	45%	u43	51%	60%
Kansas City Chiefs at Arizona Cardinals	Sunday, Sep 11
KC 471
Cover: +17
44@21
FINAL	472 ARI
Over: 65
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
KC	-6	-250		0-0	0-0-0	0-0-0	27	54½
ARI	+6	+210	54	0-0	0-0-0	0-0-0	27.5	-0.5
Referee: S NOVAK ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
KC	P MAHOMES	0	0.0	0	0	0.0	0.0	0.0
ARI	K MURRAY	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
KC	-6.5	58%	63%	-265	66%	77%	o54	74%	68%
ARI	+6.5	42%	37%	+225	34%	23%	u54	26%	32%
Las Vegas Raiders at Los Angeles Chargers	Sunday, Sep 11
LV 473
Under: 43
19@24
FINAL	474 LAC
Cover: +1.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LV	+3.5	+150		0-0	0-0-0	0-0-0	23.9	51.6
LAC	-3.5	-170	53	0-0	0-0-0	0-0-0	27.7	-3.9
Referee: S SMITH ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LV	D CARR	0	0.0	0	0	0.0	0.0	0.0
LAC	J HERBERT	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LV	+3.5	47%	50%	+150	42%	38%	o52.5	83%	73%
LAC	-3.5	53%	50%	-175	58%	62%	u52.5	17%	27%
Green Bay Packers at Minnesota Vikings	Sunday, Sep 11
GB 475
Under: 30
7@23
FINAL	476 MIN
Cover: +14
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
GB	+2	+120		0-0	0-0-0	0-0-0	23.5	46.2
MIN	-2	-140	46½	0-0	0-0-0	0-0-0	22.6	+0.9
Referee: B VINOVICH ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
GB	A RODGERS	0	0.0	0	0	0.0	0.0	0.0
MIN	K COUSINS	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
GB	+1.5	51%	60%	+100	48%	57%	o46.5	69%	71%
MIN	-1.5	49%	40%	-120	52%	43%	u46.5	31%	29%
New York Giants at Tennessee Titans	Sunday, Sep 11
NYG 477
Cover: +6.5
21@20
FINAL	478 TEN
Under: 41
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYG	+5.5	+210		0-0	0-0-0	0-0-0	18.5	44.2
TEN	-5.5	-250	44	0-0	0-0-0	0-0-0	25.8	-7.3
Referee: J BOGER ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYG	D JONES	0	0.0	0	0	0.0	0.0	0.0
TEN	R TANNEHILL	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYG	+5	30%	22%	+195	33%	14%	o44	60%	40%
TEN	-5	70%	78%	-230	67%	86%	u44	40%	60%
Tampa Bay Buccaneers at Dallas Cowboys	Sunday, Sep 11
TB 479
Cover: +13.5
19@3
FINAL	480 DAL
Under: 22
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TB	-2.5	-145		0-0	0-0-0	0-0-0	26.5	51.6
DAL	+2.5	+125	50	0-0	0-0-0	0-0-0	25.1	+1.4
Referee: R TORBERT ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TB	T BRADY	0	0.0	0	0	0.0	0.0	0.0
DAL	D PRESCOTT	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TB	-2.5	55%	66%	-135	54%	59%	o49.5	44%	58%
DAL	+2.5	45%	34%	+115	46%	41%	u49.5	56%	42%
Denver Broncos at Seattle Seahawks	Monday, Sep 12
DEN 481
Under: 33
16@17
FINAL	482 SEA
Cover: +7
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DEN	-6	-250		0-0	0-0-0	0-0-0	25	44½
SEA	+6	+210	43½	0-0	0-0-0	0-0-0	19.5	+5.5
Referee: C BLAKEMAN ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DEN	R WILSON	0	0.0	0	0	0.0	0.0	0.0
SEA	D LOCK	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DEN	-6.5	70%	85%	-295	82%	87%	o43.5	53%	50%
SEA	+6.5	30%	15%	+245	18%	13%	u43.5	47%	50%
Los Angeles Chargers at Kansas City Chiefs	Thursday, Sep 15
LAC 103
Cover: +1
24@27
FINAL	104 KC
Under: 51
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LAC	+4	+180		1-0	1-0-0	0-1-0	25.7	53.6
KC	-4	-210	52½	1-0	1-0-0	1-0-0	27.9	-2.3
Referee: J HUSSEY ( 0 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LAC	J HERBERT	1	279.0	3	0	129.4	8.2	10.7
KC	P MAHOMES	1	360.0	5	0	144.2	9.2	12.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LAC	+4	32%	32%	+165	41%	43%	o52.5	56%	67%
KC	-4	68%	68%	-195	59%	57%	u52.5	44%	33%
Miami Dolphins at Baltimore Ravens	Sunday, Sep 18
MIA 263
Cover: +7.5
42@38
FINAL	264 BAL
Over: 80
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIA	+3.5	+155		1-0	1-0-0	0-1-0	19.3	43.4
BAL	-3.5	-175	43½	1-0	1-0-0	0-1-0	24.1	-4.8
Referee: A HILL ( 0 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIA	T TAGOVAILOA	1	270.0	1	0	104.4	8.2	11.7
BAL	L JACKSON	1	213.0	3	1	98.3	7.1	12.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIA	+3.5	57%	48%	+145	50%	39%	o43.5	61%	69%
BAL	-3.5	43%	52%	-170	50%	61%	u43.5	39%	31%
New York Jets at Cleveland Browns	Sunday, Sep 18
NYJ 265
Cover: +7
31@30
FINAL	266 CLE
Over: 61
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYJ	+6	+220		0-1	0-1-0	0-1-0	18.5	42.9
CLE	-6	-260	39	1-0	1-0-0	1-0-0	24.4	-5.9
Referee: T BLAKE ( 1 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYJ	J FLACCO	1	307.0	1	1	74.6	5.2	8.3
CLE	J BRISSETT	1	147.0	1	0	74.0	4.3	8.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYJ	+6	35%	33%	+195	33%	16%	o38.5	42%	52%
CLE	-6	65%	67%	-230	67%	84%	u38.5	58%	48%
Washington Commanders at Detroit Lions	Sunday, Sep 18
WAS 267
Over: 63
27@36
FINAL	268 DET
Cover: +9
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
WAS	PICK	-110		1-0	1-0-0	1-0-0	23.7	48.6
DET	PICK	-110	48	0-1	1-0-0	1-0-0	24.9	-1.2
Referee: B VINOVICH ( 0 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
WAS	C WENTZ	1	313.0	4	2	101.0	7.6	11.6
DET	J GOFF	1	215.0	2	1	80.4	5.8	10.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
WAS	-1	34%	37%	-115	43%	49%	o48	78%	61%
DET	+1	66%	63%	-105	57%	51%	u48	22%	39%
Indianapolis Colts at Jacksonville Jaguars	Sunday, Sep 18
IND 269
Under: 24
0@24
FINAL	270 JAC
Cover: +27
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
IND	-3	-150		0-0-1	0-1-0	0-1-0	26.4	44.6
JAC	+3	+130	43½	0-1	0-1-0	1-0-0	18.1	+8.3
Referee: A KEMP ( 1 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
IND	M RYAN	1	352.0	1	1	83.1	7.0	11.0
JAC	T LAWRENCE	1	275.0	1	1	75.0	6.6	11.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
IND	-3	68%	70%	-155	65%	74%	o43.5	72%	48%
JAC	+3	32%	30%	+135	35%	26%	u43.5	28%	52%
Tampa Bay Buccaneers at New Orleans Saints	Sunday, Sep 18
TB 271
Cover: +7.5
20@10
FINAL	272 NO
Under: 30
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TB	-2.5	-145		1-0	1-0-0	0-1-0	24.8	46.1
NO	+2.5	+125	43½	1-0	0-1-0	1-0-0	21.4	+3.4
Referee: S HOCHULI ( 0 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TB	T BRADY	1	212.0	1	1	87.3	7.9	11.8
NO	J WINSTON	1	269.0	2	0	111.0	7.9	11.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TB	-3	63%	67%	-145	60%	66%	o43.5	68%	64%
NO	+3	37%	33%	+125	40%	34%	u43.5	32%	36%
Carolina Panthers at New York Giants	Sunday, Sep 18
CAR 273
Under: 35
16@19
FINAL	274 NYG
Cover: +4
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CAR	-1	-120		0-1	0-1-0	1-0-0	19.9	43.3
NYG	+1	EVEN	43½	1-0	1-0-0	0-1-0	23.4	-3.5
Referee: R TORBERT ( 0 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CAR	B MAYFIELD	1	235.0	1	1	84.7	8.7	14.7
NYG	D JONES	1	188.0	2	1	115.9	9.0	11.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CAR	-1	46%	46%	-125	45%	50%	o43.5	62%	56%
NYG	+1	54%	54%	+105	55%	50%	u43.5	38%	44%
New England Patriots at Pittsburgh Steelers	Sunday, Sep 18
NE 275
Under: 31
17@14
FINAL	276 PIT
Under: 25
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NE	-3	-160		0-1	0-1-0	0-1-0	24.1	46
PIT	+3	+140	40	1-0	1-0-0	0-1-0	21.8	+2.3
Referee: L CLARK ( 0 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NE	M JONES	1	213.0	1	1	87.2	7.1	10.1
PIT	M TRUBISKY	1	194.0	1	0	78.2	5.1	9.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NE	-3	41%	28%	-145	36%	25%	o40	32%	41%
PIT	+3	59%	72%	+125	64%	75%	u40	68%	59%
Atlanta Falcons at Los Angeles Rams	Sunday, Sep 18
ATL 277
Cover: +6
27@31
FINAL	278 LA
Over: 58
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ATL	+10	+400		0-1	1-0-0	1-0-0	19.1	46.4
LA	-10	-500	46	0-1	0-1-0	0-1-0	27.3	-8.2
Referee: C MARTIN ( 0 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ATL	M MARIOTA	1	215.0	0	0	79.7	6.5	10.8
LA	M STAFFORD	1	240.0	1	3	63.1	5.9	8.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ATL	+10	38%	40%	+360	18%	10%	o46	37%	59%
LA	-10	62%	60%	-450	82%	90%	u46	63%	41%
Seattle Seahawks at San Francisco 49ers	Sunday, Sep 18
SEA 279
Under: 34
7@27
FINAL	280 SF
Cover: +11.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SEA	+8.5	+320		1-0	1-0-0	0-1-0	18.7	40
SF	-8.5	-380	39½	0-1	0-1-0	0-1-0	21.4	-2.7
Referee: B ROGERS ( 1 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SEA	G SMITH	1	195.0	2	0	119.5	7.0	8.5
SF	T LANCE	1	164.0	0	1	50.3	5.9	12.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SEA	+8.5	53%	76%	+300	46%	36%	o39.5	74%	54%
SF	-8.5	47%	24%	-365	54%	64%	u39.5	26%	46%
Cincinnati Bengals at Dallas Cowboys	Sunday, Sep 18
CIN 281
Under: 37
17@20
FINAL	282 DAL
Cover: +10
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CIN	-7	-350		0-1	0-1-0	0-1-0	26.7	45.4
DAL	+7	+290	41½	0-1	0-1-0	0-1-0	18.7	+8
Referee: B ALLEN ( 1 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CIN	J BURROW	1	338.0	2	4	61.7	6.4	10.2
DAL	C RUSH	0	64.0	0	0	67.5	4.9	9.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CIN	-7.5	86%	85%	-295	80%	91%	o42	55%	59%
DAL	+7.5	14%	15%	+245	20%	9%	u42	45%	41%
Houston Texans at Denver Broncos	Sunday, Sep 18
HOU 283
Cover: +3.5
9@16
FINAL	284 DEN
Under: 25
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
HOU	+10.5	+400		0-0-1	1-0-0	0-1-0	17.5	44.3
DEN	-10.5	-500	45½	0-1	0-1-0	0-1-0	26.8	-9.3
Referee: C CHEFFERS ( 0 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
HOU	D MILLS	1	240.0	2	0	98.9	6.5	10.4
DEN	R WILSON	1	340.0	1	0	101.3	8.1	11.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
HOU	+10	41%	53%	+370	34%	13%	o45.5	51%	39%
DEN	-10	59%	47%	-460	66%	87%	u45.5	49%	61%
Arizona Cardinals at Las Vegas Raiders	Sunday, Sep 18
ARI 285
Cover: +11.5
29@23
FINAL	286 LV
Under: 25
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ARI	+5.5	+200		0-1	0-1-0	1-0-0	24.8	51½
LV	-5.5	-240	52	0-1	0-1-0	0-1-0	26.7	-2
Referee: C BLAKEMAN ( 0 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ARI	K MURRAY	1	193.0	2	0	99.3	5.7	8.8
LV	D CARR	1	295.0	2	3	69.1	8.0	13.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ARI	+5.5	36%	45%	+190	54%	33%	o51.5	74%	59%
LV	-5.5	64%	55%	-225	46%	67%	u51.5	26%	41%
Chicago Bears at Green Bay Packers	Sunday, Sep 18
CHI 287
Under: 37
10@27
FINAL	288 GB
Cover: +6.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CHI	+10.5	+390		1-0	1-0-0	0-1-0	17.1	44.3
GB	-10.5	-490	42	0-1	0-1-0	0-1-0	27.1	-10
Referee: C WROLSTAD ( 0 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CHI	J FIELDS	1	121.0	2	1	85.7	7.1	15.1
GB	A RODGERS	1	195.0	0	1	67.7	5.7	8.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CHI	+10	35%	64%	+350	40%	30%	o41.5	62%	60%
GB	-10	65%	36%	-435	60%	70%	u41.5	38%	40%
Tennessee Titans at Buffalo Bills	Monday, Sep 19
TEN 289
Over: 48
7@41
FINAL	290 BUF
Cover: +24
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TEN	+10	+360		0-1	0-1-0	0-1-0	18.8	48
BUF	-10	-460	47½	1-0	1-0-0	0-1-0	29.1	-10.3
Referee: S SMITH ( 0 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TEN	R TANNEHILL	1	266.0	2	0	106.4	8.1	13.3
BUF	J ALLEN	1	297.0	3	2	112.0	9.6	11.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TEN	+10	40%	36%	+350	18%	14%	o47.5	41%	62%
BUF	-10	60%	64%	-435	82%	86%	u47.5	59%	38%
Minnesota Vikings at Philadelphia Eagles	Monday, Sep 19
MIN 291
Under: 31
7@24
FINAL	292 PHI
Cover: +14
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIN	+3	+130		1-0	1-0-0	0-1-0	26.2	52.1
PHI	-3	-150	50	1-0	0-1-0	1-0-0	25.8	+0.4
Referee: S NOVAK ( 1 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIN	K COUSINS	1	277.0	2	0	118.9	8.7	12.0
PHI	J HURTS	1	243.0	0	0	80.6	7.6	13.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIN	+3	42%	59%	+120	57%	69%	o49	59%	66%
PHI	-3	58%	41%	-140	43%	31%	u49	41%	34%
Pittsburgh Steelers at Cleveland Browns	Thursday, Sep 22
PIT 301
Over: 46
17@29
FINAL	302 CLE
Cover: +7.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PIT	+4.5	+190		1-1	1-0-1	0-2-0	17.3	41.3
CLE	-4.5	-220	38	1-1	1-1-0	2-0-0	24	-6.7
Referee: C MARTIN ( 1 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PIT	M TRUBISKY	2	181.0	2	1	76.1	5.1	8.6
CLE	J BRISSETT	2	188.0	2	1	86.5	6.2	9.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PIT	+4.5	54%	60%	+170	53%	63%	o38	49%	49%
CLE	-4.5	46%	40%	-200	47%	37%	u38	51%	51%
Baltimore Ravens at New England Patriots	Sunday, Sep 25
BAL 461
Cover: +8.5
37@26
FINAL	462 NE
Over: 63
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BAL	-2.5	-140		1-1	1-1-0	1-1-0	23.1	43.3
NE	+2.5	+120	44½	1-1	0-1-1	0-2-0	20.2	+2.9
Referee: B VINOVICH ( 1 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BAL	L JACKSON	2	265.5	6	1	120.1	9.0	14.0
NE	M JONES	2	232.5	2	2	83.2	7.2	11.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BAL	-2.5	85%	86%	-135	85%	84%	o45	49%	57%
NE	+2.5	15%	14%	+115	15%	16%	u45	51%	43%
Buffalo Bills at Miami Dolphins	Sunday, Sep 25
BUF 463
Under: 40
19@21
FINAL	464 MIA
Cover: +6.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BUF	-4.5	-200		2-0	2-0-0	1-1-0	28.5	52.2
MIA	+4.5	+175	54	2-0	2-0-0	1-1-0	23.7	+4.8
Referee: A KEMP ( 1 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BUF	J ALLEN	2	307.0	7	2	123.7	8.9	11.8
MIA	T TAGOVAILOA	2	369.5	7	2	116.5	8.9	12.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BUF	-4	80%	75%	-195	80%	79%	o54.5	83%	79%
MIA	+4	20%	25%	+165	20%	21%	u54.5	17%	21%
Cincinnati Bengals at New York Jets	Sunday, Sep 25
CIN 465
Cover: +8.5
27@12
FINAL	466 NYJ
Under: 39
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CIN	-6.5	-280		0-2	0-2-0	0-2-0	27.1	45.7
NYJ	+6.5	+240	45½	1-1	1-1-0	1-1-0	18.6	+8.5
Referee: J BOGER ( 0 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CIN	J BURROW	2	268.5	3	4	73.1	6.0	9.4
NYJ	J FLACCO	2	307.0	5	1	90.0	6.0	9.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CIN	-6.5	81%	70%	-265	79%	80%	o45.5	81%	66%
NYJ	+6.5	19%	30%	+225	21%	20%	u45.5	19%	34%
New Orleans Saints at Carolina Panthers	Sunday, Sep 25
NO 467
Under: 36
14@22
FINAL	468 CAR
Cover: +10
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NO	-2	-130		1-1	0-2-0	1-1-0	22.2	42.1
CAR	+2	+110	41	0-2	0-2-0	1-1-0	19.8	+2.4
Referee: C CHEFFERS ( 0 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NO	J WINSTON	2	252.5	3	3	81.2	6.8	10.5
CAR	B MAYFIELD	2	190.0	2	1	79.5	6.8	12.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NO	-1	59%	67%	-120	59%	64%	o41	57%	59%
CAR	+1	41%	33%	+100	41%	36%	u41	43%	41%
Detroit Lions at Minnesota Vikings	Sunday, Sep 25
DET 469
Cover: +2.5
24@28
FINAL	470 MIN
Over: 52
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DET	+6.5	+230		1-1	2-0-0	2-0-0	22.3	51.8
MIN	-6.5	-270	51½	1-1	1-1-0	0-2-0	29.5	-7.2
Referee: J HUSSEY ( 0 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DET	J GOFF	2	235.5	6	1	100.2	6.6	11.5
MIN	K COUSINS	2	249.0	3	3	78.9	6.4	10.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DET	+6.5	47%	69%	+225	55%	42%	o51.5	82%	64%
MIN	-6.5	53%	31%	-265	45%	58%	u51.5	18%	36%
Kansas City Chiefs at Indianapolis Colts	Sunday, Sep 25
KC 471
Under: 37
17@20
FINAL	472 IND
Cover: +8
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
KC	-5	-210		2-0	1-1-0	1-1-0	26.6	49.2
IND	+5	+180	51	0-1-1	0-2-0	0-2-0	22.6	+4
Referee: S SMITH ( 1 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
KC	P MAHOMES	2	297.5	7	0	127.9	8.0	11.0
IND	M RYAN	2	273.5	1	4	63.9	6.8	11.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
KC	-5	81%	89%	-240	92%	93%	o51.5	59%	58%
IND	+5	19%	11%	+200	8%	7%	u51.5	41%	42%
Las Vegas Raiders at Tennessee Titans	Sunday, Sep 25
LV 473
Over: 46
22@24
FINAL	474 TEN
Cover: +4.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LV	-2.5	-145		0-2	0-2-0	1-1-0	22.1	44.2
TEN	+2.5	+125	45½	0-2	0-2-0	1-1-0	22.1	0
Referee: B ROGERS ( 1 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LV	D CARR	2	273.5	4	3	84.7	7.2	11.6
TEN	R TANNEHILL	2	191.5	2	2	77.8	7.2	12.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LV	-1.5	70%	72%	-125	67%	66%	o44.5	56%	57%
TEN	+1.5	30%	28%	+105	33%	34%	u44.5	44%	43%
Philadelphia Eagles at Washington Commanders	Sunday, Sep 25
PHI 475
Cover: +10
24@8
FINAL	476 WAS
Under: 32
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PHI	-6	-260		2-0	1-1-0	1-1-0	27.5	49
WAS	+6	+220	47½	1-1	1-1-0	2-0-0	21.4	+6.1
Referee: R TORBERT ( 0 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PHI	J HURTS	2	288.0	1	1	97.1	9.1	13.1
WAS	C WENTZ	2	325.0	7	3	100.3	7.5	11.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PHI	-5.5	71%	72%	-240	84%	89%	o47.5	70%	69%
WAS	+5.5	29%	28%	+200	16%	11%	u47.5	30%	31%
Houston Texans at Chicago Bears	Sunday, Sep 25
HOU 477
Over: 43
20@23
FINAL	478 CHI
Over: 43
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
HOU	+3	+150		0-1-1	2-0-0	0-2-0	18.2	40.4
CHI	-3	-170	39	1-1	1-1-0	0-2-0	22.1	-3.9
Referee: C BLAKEMAN ( 1 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
HOU	D MILLS	2	208.5	2	0	80.8	5.6	9.9
CHI	J FIELDS	2	95.5	2	2	69.2	6.8	12.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
HOU	+3.5	47%	45%	+155	21%	34%	o39.5	47%	47%
CHI	-3.5	53%	55%	-180	79%	66%	u39.5	53%	53%
Jacksonville Jaguars at Los Angeles Chargers	Sunday, Sep 25
JAC 479
Cover: +34.5
38@10
FINAL	480 LAC
Over: 48
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
JAC	+6.5	+220		1-1	1-1-0	1-1-0	19.4	43.2
LAC	-6.5	-260	45½	1-1	2-0-0	0-2-0	23.8	-4.4
Referee: C WROLSTAD ( 0 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
JAC	T LAWRENCE	2	255.0	3	1	96.4	7.1	10.4
LAC	J HERBERT	2	306.5	6	1	112.5	7.5	10.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
JAC	+6.5	34%	31%	+215	18%	18%	o45.5	69%	63%
LAC	-6.5	66%	69%	-255	82%	82%	u45.5	31%	37%
Green Bay Packers at Tampa Bay Buccaneers	Sunday, Sep 25
GB 481
Cover: +3.5
14@12
FINAL	482 TB
Under: 26
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
GB	+1.5	+102		1-1	1-1-0	0-2-0	19.5	41.2
TB	-1.5	-122	42	2-0	2-0-0	0-2-0	21.6	-2.1
Referee: S NOVAK ( 1 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
GB	A RODGERS	2	214.5	2	1	94.5	7.3	10.5
TB	T BRADY	2	201.0	2	1	82.8	6.6	11.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
GB	+1.5	48%	38%	+100	49%	46%	o42	62%	65%
TB	-1.5	52%	62%	-120	51%	54%	u42	38%	35%
Atlanta Falcons at Seattle Seahawks	Sunday, Sep 25
ATL 483
Cover: +4
27@23
FINAL	484 SEA
Over: 50
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ATL	PICK	-110		0-2	2-0-0	2-0-0	19.8	41½
SEA	PICK	-110	43½	1-1	1-1-0	0-2-0	21.7	-1.9
Referee: T BLAKE ( 2 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ATL	M MARIOTA	2	205.5	2	2	80.5	7.0	11.1
SEA	G SMITH	2	196.0	2	1	99.1	6.8	8.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ATL	+1	72%	58%	-105	66%	50%	o43.5	59%	53%
SEA	-1	28%	42%	-115	34%	50%	u43.5	41%	47%
Los Angeles Rams at Arizona Cardinals	Sunday, Sep 25
LA 485
Cover: +5
20@12
FINAL	486 ARI
Under: 32
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LA	-3	-160		1-1	0-2-0	1-1-0	25.7	50.3
ARI	+3	+140	48½	1-1	1-1-0	2-0-0	24.6	+1.1
Referee: A HILL ( 1 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LA	M STAFFORD	2	256.0	4	5	80.7	6.7	9.1
ARI	K MURRAY	2	235.0	3	1	85.9	5.7	8.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LA	-3.5	67%	72%	-190	67%	77%	o48.5	82%	76%
ARI	+3.5	33%	28%	+160	33%	23%	u48.5	18%	24%
San Francisco 49ers at Denver Broncos	Sunday, Sep 25
SF 487
Under: 21
10@11
FINAL	488 DEN
Cover: +3
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SF	-2	-125		1-1	1-1-0	0-2-0	20.9	45.2
DEN	+2	+105	44½	1-1	0-2-0	0-2-0	24.3	-3.4
Referee: S HOCHULI ( 0 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SF	J GAROPPOLO	0	154.0	1	0	100.1	7.3	11.9
DEN	R WILSON	2	279.5	2	1	86.5	7.7	13.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SF	-1.5	60%	69%	-120	48%	52%	o44.5	57%	44%
DEN	+1.5	40%	31%	+100	52%	48%	u44.5	43%	56%
Dallas Cowboys at New York Giants	Monday, Sep 26
DAL 489
Cover: +8.5
23@16
FINAL	490 NYG
Over: 39
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DAL	+1.5	+105		1-1	1-1-0	0-2-0	20.3	39.1
NYG	-1.5	-125	38½	2-0	2-0-0	0-2-0	18.9	+1.4
Referee: L CLARK ( 0 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DAL	C RUSH	1	149.5	1	0	87.2	6.8	11.5
NYG	D JONES	2	182.0	3	1	99.4	6.6	9.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DAL	+1	40%	40%	+100	31%	41%	o38.5	60%	57%
NYG	-1	60%	60%	-120	69%	59%	u38.5	40%	43%
Miami Dolphins at Cincinnati Bengals	Thursday, Sep 29
MIA 101
Under: 42
15@27
FINAL	102 CIN
Cover: +8
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIA	+4	+180		3-0	3-0-0	1-2-0	23.4	44.2
CIN	-4	-210	49	1-2	1-2-0	0-3-0	20.8	+2.6
Referee: T BLAKE ( 3 ov | 0 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIA	T TAGOVAILOA	3	308.3	8	2	117.8	9.2	12.9
CIN	J BURROW	3	270.7	6	4	85.2	6.5	10.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIA	+3.5	61%	63%	+155	62%	76%	o47	75%	68%
CIN	-3.5	39%	37%	-180	38%	24%	u47	25%	32%
Minnesota Vikings at New Orleans Saints	Sunday, Oct 2
MIN 251
Over: 53
28@25
FINAL	252 NO
Cover: +1
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIN	-4	-210		2-1	1-2-0	1-2-0	24.7	44.6
NO	+4	+180	42	1-2	0-3-0	1-2-0	19.9	+4.8
Referee: C BLAKEMAN ( 2 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIN	K COUSINS	3	252.7	5	3	84.0	6.4	10.2
NO	A DALTON	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIN	-3.5	62%	77%	-180	83%	76%	o41.5	54%	53%
NO	+3.5	38%	23%	+155	17%	24%	u41.5	46%	47%
Tennessee Titans at Indianapolis Colts	Sunday, Oct 2
TEN 253
Cover: +11
24@17
FINAL	254 IND
Under: 41
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TEN	+4	+170		1-2	1-2-0	2-1-0	17	38.1
IND	-4	-190	43	1-1-1	1-2-0	0-3-0	21.1	-4.1
Referee: S NOVAK ( 1 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TEN	R TANNEHILL	3	215.7	3	3	84.7	8.1	12.9
IND	M RYAN	3	256.3	3	4	77.2	6.6	10.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TEN	+4.5	59%	68%	+175	48%	56%	o43	48%	53%
IND	-4.5	41%	32%	-205	52%	44%	u43	52%	47%
Chicago Bears at New York Giants	Sunday, Oct 2
CHI 255
Under: 32
12@20
FINAL	256 NYG
Cover: +5.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CHI	+2.5	+130		2-1	1-2-0	1-2-0	18.9	38.9
NYG	-2.5	-150	39	2-1	2-1-0	1-2-0	20	-1
Referee: C CHEFFERS ( 0 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CHI	J FIELDS	3	99.0	2	4	50.0	6.6	12.9
NYG	D JONES	3	186.7	3	2	82.7	6.1	9.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CHI	+2.5	24%	36%	+130	32%	47%	o40	26%	39%
NYG	-2.5	76%	64%	-150	68%	53%	u40	74%	61%
Buffalo Bills at Baltimore Ravens	Sunday, Oct 2
BUF 257
Under: 43
23@20
FINAL	258 BAL
Cover: +0.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BUF	-3.5	-175		2-1	2-1-0	1-2-0	28.5	51
BAL	+3.5	+155	50½	2-1	2-1-0	2-1-0	22.4	+6.1
Referee: J BOGER ( 0 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BUF	J ALLEN	3	338.0	9	2	109.9	7.7	10.8
BAL	L JACKSON	3	249.7	10	2	119.0	8.5	13.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BUF	-3.5	52%	57%	-170	67%	61%	o50.5	71%	71%
BAL	+3.5	48%	43%	+145	33%	39%	u50.5	29%	29%
Los Angeles Chargers at Houston Texans	Sunday, Oct 2
LAC 259
Cover: +4.5
34@24
FINAL	260 HOU
Over: 58
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LAC	-5.5	-240		1-2	2-1-0	1-2-0	23.5	45½
HOU	+5.5	+200	45½	0-2-1	3-0-0	1-2-0	22	+1.6
Referee: A KEMP ( 1 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LAC	J HERBERT	3	303.3	7	2	98.9	7.2	10.8
HOU	D MILLS	3	220.7	3	2	77.7	6.2	10.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LAC	-5.5	59%	68%	-240	86%	88%	o45.5	51%	46%
HOU	+5.5	41%	32%	+200	14%	12%	u45.5	49%	54%
Seattle Seahawks at Detroit Lions	Sunday, Oct 2
SEA 261
Cover: +6
48@45
FINAL	262 DET
Over: 93
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SEA	+3	+145		1-2	1-2-0	1-2-0	19.1	45.4
DET	-3	-165	48	1-2	3-0-0	3-0-0	26.3	-7.2
Referee: C MARTIN ( 2 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SEA	G SMITH	3	239.0	4	2	100.8	7.0	9.1
DET	J GOFF	3	249.3	7	2	92.4	6.7	11.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SEA	+3	30%	32%	+150	28%	25%	o48	57%	39%
DET	-3	70%	68%	-175	72%	75%	u48	43%	61%
New York Jets at Pittsburgh Steelers	Sunday, Oct 2
NYJ 263
Cover: +7
24@20
FINAL	264 PIT
Over: 44
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYJ	+3	+155		1-2	1-2-0	1-2-0	19.6	42.2
PIT	-3	-175	41	1-2	1-1-1	1-2-0	22.6	-3
Referee: B ROGERS ( 2 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYJ	Z WILSON	0	0.0	0	0	0.0	0.0	0.0
PIT	M TRUBISKY	3	189.7	2	1	77.7	5.5	9.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYJ	+3.5	34%	37%	+150	39%	34%	o41	46%	38%
PIT	-3.5	66%	63%	-175	61%	66%	u41	54%	62%
Jacksonville Jaguars at Philadelphia Eagles	Sunday, Oct 2
JAC 265
Over: 50
21@29
FINAL	266 PHI
Cover: +1.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
JAC	+6.5	+230		2-1	2-1-0	2-1-0	17.4	42.7
PHI	-6.5	-270	44	3-0	2-1-0	1-2-0	25.3	-7.9
Referee: S HOCHULI ( 0 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
JAC	T LAWRENCE	3	257.3	6	1	103.1	7.0	10.0
PHI	J HURTS	3	305.3	4	1	106.5	9.4	13.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
JAC	+6.5	43%	44%	+220	18%	18%	o43.5	62%	66%
PHI	-6.5	57%	56%	-265	82%	82%	u43.5	38%	34%
Washington Commanders at Dallas Cowboys	Sunday, Oct 2
WAS 267
Under: 35
10@25
FINAL	268 DAL
Cover: +12
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
WAS	+3	+145		1-2	1-2-0	2-1-0	16.2	38.1
DAL	-3	-165	41	2-1	2-1-0	1-2-0	21.9	-5.7
Referee: S SMITH ( 1 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
WAS	C WENTZ	3	287.0	7	3	90.6	6.6	10.5
DAL	C RUSH	2	171.3	2	0	91.8	6.9	10.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
WAS	+3	30%	22%	+140	24%	21%	o41	62%	60%
DAL	-3	70%	78%	-165	76%	79%	u41	38%	40%
Cleveland Browns at Atlanta Falcons	Sunday, Oct 2
CLE 269
Under: 43
20@23
FINAL	270 ATL
Cover: +4
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CLE	-1	-120		2-1	2-1-0	3-0-0	26.4	53.8
ATL	+1	EVEN	48	1-2	3-0-0	3-0-0	27.4	-1
Referee: C WROLSTAD ( 1 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CLE	J BRISSETT	3	198.7	4	1	94.3	6.5	9.8
ATL	M MARIOTA	3	213.3	3	3	85.4	8.1	12.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CLE	-1	64%	70%	-120	53%	61%	o49	69%	44%
ATL	+1	36%	30%	+100	47%	39%	u49	31%	56%
Arizona Cardinals at Carolina Panthers	Sunday, Oct 2
ARI 271
Cover: +11
26@16
FINAL	272 CAR
Under: 42
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ARI	+1	EVEN		1-2	1-2-0	2-1-0	22.1	44.8
CAR	-1	-120	44	1-2	1-2-0	1-2-0	22.7	-0.7
Referee: J HUSSEY ( 1 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ARI	K MURRAY	3	261.3	3	1	82.6	5.6	8.7
CAR	B MAYFIELD	3	183.3	3	1	80.8	6.8	13.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ARI	+1	75%	80%	-105	74%	80%	o44	74%	69%
CAR	-1	25%	20%	-115	26%	20%	u44	26%	31%
Denver Broncos at Las Vegas Raiders	Sunday, Oct 2
DEN 273
Over: 55
23@32
FINAL	274 LV
Cover: +6.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DEN	+2.5	+125		2-1	1-2-0	0-3-0	16.9	36.3
LV	-2.5	-145	45½	0-3	0-3-0	2-1-0	19.4	-2.5
Referee: L CLARK ( 1 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DEN	R WILSON	3	247.7	2	1	83.2	7.0	11.8
LV	D CARR	3	283.3	6	4	85.1	7.1	11.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DEN	+2.5	35%	37%	+130	30%	41%	o45.5	48%	42%
LV	-2.5	65%	63%	-150	70%	59%	u45.5	52%	58%
New England Patriots at Green Bay Packers	Sunday, Oct 2
NE 275
Cover: +6.5
24@27
FINAL	276 GB
Over: 51
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NE	+9.5	+350		1-2	0-2-1	1-2-0	12.5	36.9
GB	-9.5	-450	40	2-1	2-1-0	0-3-0	24.4	-12
Referee: A HILL ( 1 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NE	B HOYER	0	0.0	0	0	0.0	0.0	0.0
GB	A RODGERS	3	228.0	4	2	98.0	7.3	10.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NE	+9.5	30%	39%	+350	10%	8%	o40	50%	57%
GB	-9.5	70%	61%	-435	90%	92%	u40	50%	43%
Kansas City Chiefs at Tampa Bay Buccaneers	Sunday, Oct 2
KC 277
Cover: +12
41@31
FINAL	278 TB
Over: 72
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
KC	+2	+115		2-1	1-2-0	1-2-0	18.8	41.4
TB	-2	-135	48	2-1	2-1-0	0-3-0	22.6	-3.8
Referee: B VINOVICH ( 2 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
KC	P MAHOMES	3	285.7	8	1	112.1	7.9	11.6
TB	T BRADY	3	224.3	3	1	89.2	6.5	10.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
KC	+2	60%	69%	+105	54%	69%	o47.5	68%	67%
TB	-2	40%	31%	-125	46%	31%	u47.5	32%	33%
Los Angeles Rams at San Francisco 49ers	Monday, Oct 3
LA 279
Under: 33
9@24
FINAL	280 SF
Cover: +13.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LA	+1.5	EVEN		2-1	1-2-0	1-2-0	18.8	39.7
SF	-1.5	-120	42	1-2	1-2-0	0-3-0	20.9	-2.1
Referee: B ALLEN ( 1 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LA	M STAFFORD	3	253.7	4	5	86.3	7.5	10.3
SF	J GAROPPOLO	1	182.5	2	1	89.2	7.3	11.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LA	+2	64%	71%	+100	54%	79%	o42	65%	66%
SF	-2	36%	29%	-120	46%	21%	u42	35%	34%
Indianapolis Colts at Denver Broncos	Thursday, Oct 6
IND 301
Cover: +6.5
12@9
FINAL	302 DEN
Under: 21
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
IND	+3.5	+155		1-2-1	1-3-0	0-4-0	17.6	38.3
DEN	-3.5	-175	42	2-2	1-3-0	1-3-0	20.8	-3.2
Referee: B ROGERS ( 3 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
IND	M RYAN	4	281.3	5	5	85.0	7.3	11.0
DEN	R WILSON	4	245.0	4	1	91.1	7.5	12.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
IND	+3.5	40%	38%	+155	31%	39%	o42	47%	35%
DEN	-3.5	60%	62%	-180	69%	61%	u42	53%	65%
New York Giants at Green Bay Packers	Sunday, Oct 9
NYG 451
Cover: +14
27@22
FINAL	452 GB
Over: 49
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYG	+9	+335		3-1	3-1-0	1-3-0	18.5	41.2
GB	-9	-420	42	3-1	2-2-0	1-3-0	22.7	-4.2
Referee: A KEMP ( 2 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYG	D JONES	4	157.8	3	2	81.9	6.0	9.4
GB	A RODGERS	4	233.8	6	3	95.6	7.3	10.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYG	+8	37%	49%	+300	15%	15%	o41.5	63%	64%
GB	-8	63%	51%	-365	85%	85%	u41.5	37%	36%
Seattle Seahawks at New Orleans Saints	Sunday, Oct 9
SEA 453
Over: 71
32@39
FINAL	454 NO
Cover: +1.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SEA	+5.5	+195		2-2	2-2-0	2-2-0	19.9	46½
NO	-5.5	-230	45	1-3	1-3-0	2-2-0	26.6	-6.6
Referee: B ALLEN ( 1 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SEA	G SMITH	4	259.3	6	2	108.1	7.9	10.2
NO	A DALTON	1	236.0	1	0	108.6	8.4	11.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SEA	+5	64%	72%	+195	46%	50%	o45.5	76%	53%
NO	-5	36%	28%	-230	54%	50%	u45.5	24%	47%
Houston Texans at Jacksonville Jaguars	Sunday, Oct 9
HOU 455
Cover: +14
13@6
FINAL	456 JAC
Under: 19
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
HOU	+7	+260		0-3-1	3-1-0	2-2-0	19.5	43.8
JAC	-7	-320	43½	2-2	2-2-0	3-1-0	24.2	-4.7
Referee: R TORBERT ( 0 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
HOU	D MILLS	4	227.0	5	4	80.4	6.4	10.3
JAC	T LAWRENCE	4	236.5	8	2	99.9	7.1	10.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
HOU	+6.5	26%	33%	+260	17%	11%	o43.5	65%	63%
JAC	-6.5	74%	67%	-315	83%	89%	u43.5	35%	37%
Pittsburgh Steelers at Buffalo Bills	Sunday, Oct 9
PIT 457
Under: 41
3@38
FINAL	458 BUF
Cover: +21
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PIT	+14	+600		1-3	1-2-1	2-2-0	13.4	42.4
BUF	-14	-900	44	3-1	2-2-0	1-3-0	29	-15.6
Referee: J HUSSEY ( 1 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PIT	K PICKETT	0	120.0	0	3	65.1	9.2	12.0
BUF	J ALLEN	4	306.8	10	3	101.0	7.3	10.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PIT	+14	38%	47%	+550	13%	9%	o44	68%	65%
BUF	-14	62%	53%	-750	87%	91%	u44	32%	35%
Atlanta Falcons at Tampa Bay Buccaneers	Sunday, Oct 9
ATL 459
Cover: +4
15@21
FINAL	460 TB
Under: 36
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ATL	+10	+360		2-2	4-0-0	3-1-0	17.1	43
TB	-10	-460	46½	2-2	2-2-0	1-3-0	26	-8.9
Referee: J BOGER ( 0 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ATL	M MARIOTA	4	194.8	3	4	76.9	8.0	13.7
TB	T BRADY	4	264.5	6	1	97.7	6.8	10.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ATL	+10.5	42%	48%	+400	13%	8%	o46.5	59%	52%
TB	-10.5	58%	52%	-500	87%	92%	u46.5	41%	48%
Chicago Bears at Minnesota Vikings	Sunday, Oct 9
CHI 461
Cover: +1
22@29
FINAL	462 MIN
Over: 51
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CHI	+8	+330		2-2	1-3-0	1-3-0	18.7	43.1
MIN	-8	-400	44	3-1	1-3-0	2-2-0	24.5	-5.8
Referee: S HOCHULI ( 1 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CHI	J FIELDS	4	117.8	2	4	58.7	7.0	13.9
MIN	K COUSINS	4	257.8	6	4	84.1	6.6	10.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CHI	+8.5	45%	40%	+300	14%	11%	o43.5	37%	38%
MIN	-8.5	55%	60%	-365	86%	89%	u43.5	63%	62%
Tennessee Titans at Washington Commanders	Sunday, Oct 9
TEN 463
Cover: +4
21@17
FINAL	464 WAS
Under: 38
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TEN	PICK	-110		2-2	2-2-0	2-2-0	22.8	42.4
WAS	PICK	-110	43	1-3	1-3-0	2-2-0	19.6	+3.2
Referee: L CLARK ( 2 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TEN	R TANNEHILL	4	196.0	5	3	93.8	7.8	11.7
WAS	C WENTZ	4	257.8	8	5	82.3	6.0	9.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TEN	+1	65%	83%	-110	64%	77%	o43	71%	59%
WAS	-1	35%	17%	-110	36%	23%	u43	29%	41%
Miami Dolphins at New York Jets	Sunday, Oct 9
MIA 465
Over: 57
17@40
FINAL	466 NYJ
Cover: +26
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIA	-3	-170		3-1	3-1-0	1-3-0	23.7	45
NYJ	+3	+150	46	2-2	2-2-0	2-2-0	21.3	+2.5
Referee: C MARTIN ( 3 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIA	T BRIDGEWATER	0	96.5	1	1	77.6	7.7	13.8
NYJ	Z WILSON	1	252.0	1	2	59.0	7.0	14.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIA	-3.5	55%	55%	-170	54%	61%	o46	53%	42%
NYJ	+3.5	45%	45%	+145	46%	39%	u46	47%	58%
Los Angeles Chargers at Cleveland Browns	Sunday, Oct 9
LAC 467
Cover: +0.5
30@28
FINAL	468 CLE
Over: 58
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LAC	-1.5	-125		2-2	3-1-0	2-2-0	25.5	48.7
CLE	+1.5	+105	47	2-2	2-2-0	3-1-0	23.2	+2.4
Referee: A HILL ( 2 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LAC	J HERBERT	4	312.5	9	2	102.2	7.5	11.3
CLE	J BRISSETT	4	207.5	4	2	87.1	6.5	10.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LAC	-2.5	56%	73%	-125	76%	72%	o47.5	52%	57%
CLE	+2.5	44%	27%	+105	24%	28%	u47.5	48%	43%
Detroit Lions at New England Patriots	Sunday, Oct 9
DET 469
Under: 29
0@29
FINAL	470 NE
Cover: +26
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DET	+3	+135		1-3	3-1-0	4-0-0	22.5	46.9
NE	-3	-155	47	1-3	1-2-1	2-2-0	24.4	-1.9
Referee: C WROLSTAD ( 1 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DET	J GOFF	4	281.5	11	3	99.9	7.5	12.2
NE	B ZAPPE	0	99.0	1	0	107.4	6.6	9.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DET	+3	45%	68%	+135	44%	67%	o47	61%	63%
NE	-3	55%	32%	-155	56%	33%	u47	39%	37%
San Francisco 49ers at Carolina Panthers	Sunday, Oct 9
SF 471
Cover: +16
37@15
FINAL	472 CAR
Over: 52
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SF	-6	-250		2-2	2-2-0	0-4-0	22.7	37.6
CAR	+6	+210	39½	1-3	1-3-0	1-3-0	15	+7.7
Referee: S SMITH ( 1 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SF	J GAROPPOLO	2	201.3	3	1	93.2	7.8	12.9
CAR	B MAYFIELD	4	186.8	4	3	75.0	6.4	11.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SF	-6	68%	80%	-250	90%	92%	o39.5	45%	54%
CAR	+6	32%	20%	+210	10%	8%	u39.5	55%	46%
Philadelphia Eagles at Arizona Cardinals	Sunday, Oct 9
PHI 473
Under: 37
20@17
FINAL	474 ARI
Cover: +2
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PHI	-5	-230		4-0	3-1-0	2-2-0	27	46.9
ARI	+5	+195	48½	2-2	2-2-0	2-2-0	19.9	+7.1
Referee: T BLAKE ( 3 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PHI	J HURTS	4	280.0	4	2	99.6	9.1	13.7
ARI	K MURRAY	4	247.8	5	2	85.2	5.7	8.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PHI	-5.5	57%	64%	-230	54%	75%	o48.5	76%	73%
ARI	+5.5	43%	36%	+185	46%	25%	u48.5	24%	27%
Dallas Cowboys at Los Angeles Rams	Sunday, Oct 9
DAL 475
Cover: +17.5
22@10
FINAL	476 LA
Under: 32
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DAL	+5.5	+200		3-1	3-1-0	1-3-0	16.5	38.9
LA	-5.5	-240	41½	2-2	1-3-0	1-3-0	22.4	-6
Referee: B VINOVICH ( 3 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DAL	C RUSH	3	184.3	4	0	95.9	7.2	11.9
LA	M STAFFORD	4	253.8	4	6	81.4	6.8	9.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DAL	+5	49%	61%	+190	33%	38%	o42	59%	63%
LA	-5	51%	39%	-225	67%	62%	u42	41%	37%
Cincinnati Bengals at Baltimore Ravens	Sunday, Oct 9
CIN 477
Cover: +1
17@19
FINAL	478 BAL
Under: 36
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CIN	+3	+150		2-2	2-2-0	0-4-0	21.6	47½
BAL	-3	-170	48	2-2	3-1-0	2-2-0	25.9	-4.3
Referee: S NOVAK ( 1 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CIN	J BURROW	4	274.8	8	4	91.3	7.0	11.0
BAL	L JACKSON	4	223.3	11	4	105.1	7.6	11.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CIN	+3	36%	44%	+140	43%	44%	o48	75%	77%
BAL	-3	64%	56%	-165	57%	56%	u48	25%	23%
Las Vegas Raiders at Kansas City Chiefs	Monday, Oct 10
LV 479
Cover: +6
29@30
FINAL	480 KC
Over: 59
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LV	+7	+290		1-3	1-3-0	3-1-0	22.1	51.8
KC	-7	-350	51½	3-1	2-2-0	2-2-0	29.6	-7.5
Referee: C CHEFFERS ( 0 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LV	D CARR	4	259.5	6	4	83.2	6.7	11.0
KC	P MAHOMES	4	276.5	11	2	108.4	7.6	11.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LV	+7	39%	24%	+290	22%	13%	o51.5	63%	67%
KC	-7	61%	76%	-350	78%	87%	u51.5	37%	33%
Washington Commanders at Chicago Bears	Thursday, Oct 13
WAS 105
Cover: +4
12@7
FINAL	106 CHI
Under: 19
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
WAS	-1	-115		1-4	1-4-0	2-3-0	18.4	40.7
CHI	+1	-105	39	2-3	2-3-0	2-3-0	22.2	-3.8
Referee: A HILL ( 3 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
WAS	C WENTZ	5	278.0	10	6	86.0	6.6	10.5
CHI	J FIELDS	5	135.8	3	4	73.1	7.7	13.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
WAS	-1.5	47%	42%	-120	43%	35%	o39	54%	51%
CHI	+1.5	53%	58%	+100	57%	65%	u39	46%	49%
Tampa Bay Buccaneers at Pittsburgh Steelers	Sunday, Oct 16
TB 251
Under: 38
18@20
FINAL	252 PIT
Cover: +12
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TB	-10	-480		3-2	2-3-0	1-4-0	27.3	43.2
PIT	+10	+380	46½	1-4	1-3-1	2-3-0	15.9	+11.4
Referee: S SMITH ( 2 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TB	T BRADY	5	281.8	7	1	96.5	6.8	10.0
PIT	K PICKETT	1	223.5	0	4	61.5	6.9	10.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TB	-9.5	59%	68%	-425	90%	94%	o46.5	55%	35%
PIT	+9.5	41%	32%	+340	10%	6%	u46.5	45%	65%
Cincinnati Bengals at New Orleans Saints	Sunday, Oct 16
CIN 253
Cover: +1
30@26
FINAL	254 NO
Over: 56
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CIN	-3	-180		2-3	3-2-0	0-5-0	23.4	43.4
NO	+3	+160	42½	2-3	2-3-0	3-2-0	20	+3.5
Referee: L CLARK ( 2 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CIN	J BURROW	5	263.2	9	5	89.7	6.9	10.6
NO	A DALTON	2	211.5	2	1	98.5	8.1	11.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CIN	-3	65%	76%	-165	86%	78%	o43	74%	77%
NO	+3	35%	24%	+140	14%	22%	u43	26%	23%
Jacksonville Jaguars at Indianapolis Colts	Sunday, Oct 16
JAC 255
Over: 61
27@34
FINAL	256 IND
Cover: +5.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
JAC	+1.5	+110		2-3	2-3-0	3-2-0	18.8	38.7
IND	-1.5	-130	41	2-2-1	2-3-0	0-5-0	19.9	-1.1
Referee: J BOGER ( 0 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
JAC	T LAWRENCE	5	246.4	8	4	88.0	6.8	10.9
IND	M RYAN	5	275.2	5	7	79.8	7.1	10.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
JAC	+1.5	55%	56%	+100	62%	61%	o41.5	38%	41%
IND	-1.5	45%	44%	-120	38%	39%	u41.5	62%	59%
New England Patriots at Cleveland Browns	Sunday, Oct 16
NE 257
Cover: +25.5
38@15
FINAL	258 CLE
Over: 53
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NE	+2.5	+130		2-3	2-2-1	2-3-0	20.3	42
CLE	-2.5	-150	43	2-3	3-2-0	4-1-0	21.6	-1.3
Referee: S NOVAK ( 1 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NE	B ZAPPE	1	143.5	2	1	104.8	8.0	10.6
CLE	J BRISSETT	5	212.0	5	3	85.4	6.6	10.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NE	+3	58%	55%	+120	43%	50%	o43.5	65%	51%
CLE	-3	42%	45%	-140	57%	50%	u43.5	35%	49%
New York Jets at Green Bay Packers	Sunday, Oct 16
NYJ 259
Cover: +25
27@10
FINAL	260 GB
Under: 37
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYJ	+8	+315		3-2	3-2-0	3-2-0	20.3	44
GB	-8	-375	45	3-2	2-3-0	2-3-0	23.6	-3.3
Referee: C BLAKEMAN ( 3 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYJ	Z WILSON	2	231.0	1	2	73.9	8.1	14.4
GB	A RODGERS	5	231.4	8	3	95.8	6.9	10.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYJ	+7.5	51%	60%	+285	19%	19%	o45	57%	58%
GB	-7.5	49%	40%	-345	81%	81%	u45	43%	42%
Baltimore Ravens at New York Giants	Sunday, Oct 16
BAL 261
Under: 44
20@24
FINAL	262 NYG
Cover: +9.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BAL	-5.5	-250		3-2	3-2-0	2-3-0	24.8	44.6
NYG	+5.5	+210	46	4-1	4-1-0	2-3-0	19.8	+5
Referee: C MARTIN ( 4 ov | 1 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BAL	L JACKSON	5	213.4	12	5	97.9	7.2	11.2
NYG	D JONES	5	169.6	3	2	85.7	6.4	9.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BAL	-5.5	66%	55%	-240	76%	75%	o46	64%	62%
NYG	+5.5	34%	45%	+200	24%	25%	u46	36%	38%
Minnesota Vikings at Miami Dolphins	Sunday, Oct 16
MIN 263
Cover: +5
24@16
FINAL	264 MIA
Under: 40
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIN	-3	-175		4-1	1-4-0	3-2-0	23.3	43.8
MIA	+3	+155	45	3-2	3-2-0	2-3-0	20.4	+2.9
Referee: B ROGERS ( 3 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIN	K COUSINS	5	265.4	7	5	86.4	6.7	10.1
MIA	S THOMPSON	0	166.0	0	1	58.4	5.0	8.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIN	-3.5	57%	74%	-175	77%	78%	o45	48%	55%
MIA	+3.5	43%	26%	+150	23%	22%	u45	52%	45%
San Francisco 49ers at Atlanta Falcons	Sunday, Oct 16
SF 265
Under: 42
14@28
FINAL	266 ATL
Cover: +17.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SF	-3.5	-185		3-2	3-2-0	1-4-0	23.9	40.9
ATL	+3.5	+165	45½	2-3	5-0-0	3-2-0	16.9	+7
Referee: C CHEFFERS ( 1 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SF	J GAROPPOLO	3	214.3	5	1	97.8	8.0	13.2
ATL	M MARIOTA	5	185.2	4	4	78.8	7.5	13.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SF	-3.5	63%	73%	-195	86%	89%	o46	53%	43%
ATL	+3.5	37%	27%	+165	14%	11%	u46	47%	57%
Carolina Panthers at Los Angeles Rams	Sunday, Oct 16
CAR 267
Under: 34
10@24
FINAL	268 LA
Cover: +5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CAR	+9	+375		1-4	1-4-0	2-3-0	18.4	40.4
LA	-9	-475	41	2-3	1-4-0	1-4-0	21.9	-3.5
Referee: T BLAKE ( 3 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CAR	P WALKER	0	60.0	0	0	108.3	10.0	12.0
LA	M STAFFORD	5	264.6	5	7	82.4	6.9	9.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CAR	+9.5	37%	38%	+350	7%	7%	o41	51%	58%
LA	-9.5	63%	62%	-435	93%	93%	u41	49%	42%
Arizona Cardinals at Seattle Seahawks	Sunday, Oct 16
ARI 269
Under: 28
9@19
FINAL	270 SEA
Cover: +12
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ARI	-2	-130		2-3	3-2-0	2-3-0	26.3	49.7
SEA	+2	+110	50½	2-3	2-3-0	3-2-0	23.4	+2.9
Referee: S HOCHULI ( 2 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ARI	K MURRAY	5	248.2	6	3	84.3	5.8	8.8
SEA	G SMITH	5	261.0	9	2	113.2	8.3	11.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ARI	-2.5	52%	59%	-135	63%	56%	o50.5	80%	61%
SEA	+2.5	48%	41%	+115	37%	44%	u50.5	20%	39%
Buffalo Bills at Kansas City Chiefs	Sunday, Oct 16
BUF 271
Cover: +1.5
24@20
FINAL	272 KC
Under: 44
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BUF	-2.5	-160		4-1	3-2-0	1-4-0	26.5	50.1
KC	+2.5	+140	55	4-1	2-3-0	3-2-0	23.6	+3
Referee: B ALLEN ( 2 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BUF	J ALLEN	5	330.2	14	4	107.4	8.3	12.4
KC	P MAHOMES	5	279.6	15	2	110.5	7.4	11.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BUF	-2.5	65%	57%	-150	64%	51%	o54	89%	85%
KC	+2.5	35%	43%	+130	36%	49%	u54	11%	15%
Dallas Cowboys at Philadelphia Eagles	Sunday, Oct 16
DAL 273
Cover: +.5
17@26
FINAL	274 PHI
Cover: +2.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DAL	+6.5	+230		4-1	4-1-0	1-4-0	17.9	39.1
PHI	-6.5	-270	43	5-0	3-2-0	2-3-0	21.2	-3.2
Referee: J HUSSEY ( 1 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DAL	C RUSH	4	167.8	4	0	93.9	7.1	11.7
PHI	J HURTS	5	271.8	4	2	97.4	8.6	12.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DAL	+7	67%	60%	+235	50%	36%	o42.5	50%	67%
PHI	-7	33%	40%	-280	50%	64%	u42.5	50%	33%
Denver Broncos at Los Angeles Chargers	Monday, Oct 17
DEN 275
Cover: +0.5
16@19
FINAL	276 LAC
Under: 35
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DEN	+3.5	+170		2-3	1-4-0	1-4-0	21.1	45.2
LAC	-3.5	-190	45	3-2	3-2-0	3-2-0	24.1	-3
Referee: R TORBERT ( 0 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DEN	R WILSON	5	250.8	4	3	82.8	7.4	12.4
LAC	J HERBERT	5	295.6	10	2	100.8	7.4	11.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DEN	+3.5	39%	26%	+155	30%	20%	o45.5	40%	34%
LAC	-3.5	61%	74%	-180	70%	80%	u45.5	60%	66%
New Orleans Saints at Arizona Cardinals	Thursday, Oct 20
NO 303
Over: 76
34@42
FINAL	304 ARI
Cover: +5.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NO	+2.5	+125		2-4	2-4-0	4-2-0	22	45
ARI	-2.5	-145	44	2-4	3-3-0	2-4-0	23	-1.1
Referee: J BOGER ( 1 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NO	A DALTON	3	195.0	3	1	90.6	7.0	11.0
ARI	K MURRAY	6	243.8	6	4	81.8	5.8	8.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NO	+2.5	30%	30%	+125	33%	34%	o43.5	48%	48%
ARI	-2.5	70%	70%	-145	67%	66%	u43.5	52%	52%
Detroit Lions at Dallas Cowboys	Sunday, Oct 23
DET 451
Under: 30
6@24
FINAL	452 DAL
Cover: +11
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DET	+7	+250		1-4	3-2-0	4-1-0	20.5	49½
DAL	-7	-300	49½	4-2	4-2-0	2-4-0	29	-8.5
Referee: A HILL ( 3 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DET	J GOFF	5	271.0	11	4	92.9	7.3	12.2
DAL	D PRESCOTT	1	134.0	0	1	47.2	4.6	9.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DET	+7	38%	39%	+255	19%	16%	o49.5	55%	51%
DAL	-7	62%	61%	-305	81%	84%	u49.5	45%	49%
New York Giants at Jacksonville Jaguars	Sunday, Oct 23
NYG 453
Cover: +9.5
23@17
FINAL	454 JAC
Under: 40
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYG	+3.5	+160		5-1	5-1-0	2-4-0	19.2	41.7
JAC	-3.5	-180	44	2-4	2-4-0	4-2-0	22.4	-3.2
Referee: T BLAKE ( 3 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYG	D JONES	6	170.2	5	2	90.2	6.4	9.5
JAC	T LAWRENCE	6	232.8	9	4	91.9	6.9	10.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYG	+3	49%	73%	+135	64%	82%	o44	64%	59%
JAC	-3	51%	27%	-155	36%	18%	u44	36%	41%
Indianapolis Colts at Tennessee Titans	Sunday, Oct 23
IND 455
Under: 29
10@19
FINAL	456 TEN
Cover: +6.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
IND	+2.5	+115		3-2-1	3-3-0	1-5-0	18.6	40.8
TEN	-2.5	-135	43	3-2	3-2-0	2-3-0	22.1	-3.5
Referee: R TORBERT ( 0 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
IND	M RYAN	6	294.2	8	7	86.2	7.0	10.4
TEN	R TANNEHILL	5	193.0	6	3	94.2	7.7	11.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
IND	+2.5	30%	33%	+115	36%	43%	o43	57%	65%
TEN	-2.5	70%	67%	-135	64%	57%	u43	43%	35%
Atlanta Falcons at Cincinnati Bengals	Sunday, Oct 23
ATL 457
Over: 52
17@35
FINAL	458 CIN
Cover: +11.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ATL	+6.5	+225		3-3	6-0-0	3-3-0	20	44.3
CIN	-6.5	-265	47½	3-3	4-2-0	1-5-0	24.3	-4.3
Referee: C BLAKEMAN ( 3 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ATL	M MARIOTA	6	175.8	6	4	87.7	7.7	12.6
CIN	J BURROW	6	269.3	12	5	95.6	7.1	10.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ATL	+6.5	38%	53%	+245	16%	19%	o48	85%	70%
CIN	-6.5	62%	47%	-295	84%	81%	u48	15%	30%
Cleveland Browns at Baltimore Ravens	Sunday, Oct 23
CLE 459
Cover: +3.5
20@23
FINAL	460 BAL
Under: 43
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CLE	+6.5	+245		2-4	3-3-0	5-1-0	21	49½
BAL	-6.5	-285	46½	3-3	3-3-0	2-4-0	28.5	-7.5
Referee: S SMITH ( 2 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CLE	J BRISSETT	6	221.0	6	5	78.7	6.4	10.7
BAL	L JACKSON	6	212.8	13	6	93.2	7.1	11.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CLE	+6.5	35%	39%	+250	10%	13%	o47	69%	65%
BAL	-6.5	65%	61%	-300	90%	87%	u47	31%	35%
Tampa Bay Buccaneers at Carolina Panthers	Sunday, Oct 23
TB 461
Under: 24
3@21
FINAL	462 CAR
Cover: +31
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TB	-13	-750		3-3	2-4-0	1-5-0	24.9	40.9
CAR	+13	+525	38½	1-5	1-5-0	2-4-0	16	+8.9
Referee: C WROLSTAD ( 1 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TB	T BRADY	6	275.3	8	1	95.1	6.7	10.0
CAR	P WALKER	1	60.0	0	0	81.6	5.5	8.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TB	-13	69%	64%	-660	91%	93%	o39.5	43%	62%
CAR	+13	31%	36%	+490	9%	7%	u39.5	57%	38%
Green Bay Packers at Washington Commanders	Sunday, Oct 23
GB 463
Over: 44
21@23
FINAL	464 WAS
Cover: +6
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
GB	-4	-210		3-3	2-4-0	2-4-0	21.8	40
WAS	+4	+180	41½	2-4	2-4-0	2-4-0	18.2	+3.6
Referee: C MARTIN ( 4 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
GB	A RODGERS	6	233.8	9	3	94.3	6.7	10.0
WAS	T HEINICKE	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
GB	-4.5	74%	78%	-210	81%	87%	o41.5	59%	59%
WAS	+4.5	26%	22%	+180	19%	13%	u41.5	41%	41%
New York Jets at Denver Broncos	Sunday, Oct 23
NYJ 465
Cover: +5
16@9
FINAL	466 DEN
Under: 25
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYJ	-2	-135		4-2	4-2-0	3-3-0	17.7	39.7
DEN	+2	+115	37	2-4	2-4-0	1-5-0	22	-4.3
Referee: B VINOVICH ( 3 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYJ	Z WILSON	3	190.7	1	2	73.9	7.6	13.6
DEN	B RYPIEN	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYJ	-2	57%	76%	-125	77%	78%	o36.5	26%	52%
DEN	+2	43%	24%	+105	23%	22%	u36.5	74%	48%
Houston Texans at Las Vegas Raiders	Sunday, Oct 23
HOU 467
Over: 58
20@38
FINAL	468 LV
Cover: +11
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
HOU	+7	+280		1-3-1	4-1-0	2-3-0	19.5	46.1
LV	-7	-340	46	1-4	2-3-0	4-1-0	26.6	-7
Referee: J HUSSEY ( 2 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
HOU	D MILLS	5	209.6	5	4	80.6	6.3	10.1
LV	D CARR	5	255.8	8	4	87.7	7.0	11.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
HOU	+7	30%	34%	+255	8%	10%	o46	59%	49%
LV	-7	70%	66%	-305	92%	90%	u46	41%	51%
Kansas City Chiefs at San Francisco 49ers	Sunday, Oct 23
KC 469
Cover: +20
44@23
FINAL	470 SF
Over: 67
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
KC	-1	-115		4-2	2-4-0	3-3-0	24.9	46.6
SF	+1	-105	49	3-3	3-3-0	1-5-0	21.7	+3.2
Referee: A KEMP ( 3 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
KC	P MAHOMES	6	289.3	17	4	106.1	7.6	11.5
SF	J GAROPPOLO	4	230.6	7	3	94.8	7.8	12.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
KC	-1	80%	83%	-120	79%	73%	o49	57%	61%
SF	+1	20%	17%	+100	21%	27%	u49	43%	39%
Seattle Seahawks at Los Angeles Chargers	Sunday, Oct 23
SEA 471
Cover: +19
37@23
FINAL	472 LAC
Over: 60
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SEA	+5	+200		3-3	3-3-0	3-3-0	22.8	50.4
LAC	-5	-240	51½	4-2	3-3-0	3-3-0	27.5	-4.7
Referee: L CLARK ( 3 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SEA	G SMITH	6	250.3	9	2	108.1	8.0	10.9
LAC	J HERBERT	6	286.0	10	3	93.1	6.7	10.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SEA	+5	56%	52%	+185	28%	24%	o51	67%	51%
LAC	-5	44%	48%	-215	72%	76%	u51	33%	49%
Pittsburgh Steelers at Miami Dolphins	Sunday, Oct 23
PIT 473
Cover: +1
10@16
FINAL	474 MIA
Under: 26
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PIT	+7	+250		2-4	2-3-1	2-4-0	18.8	45
MIA	-7	-300	44	3-3	3-3-0	2-4-0	26.2	-7.4
Referee: S NOVAK ( 2 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PIT	K PICKETT	2	171.3	1	4	67.0	6.2	9.4
MIA	T TAGOVAILOA	4	258.8	8	3	109.9	9.0	12.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PIT	+7	39%	52%	+255	30%	28%	o44.5	65%	56%
MIA	-7	61%	48%	-305	70%	72%	u44.5	35%	44%
Chicago Bears at New England Patriots	Monday, Oct 24
CHI 475
Cover: +28
33@14
FINAL	476 NE
Over: 47
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CHI	+9	+335		2-4	2-4-0	2-4-0	16.1	40.3
NE	-9	-420	40	3-3	3-2-1	3-3-0	24.2	-8.1
Referee: S NOVAK ( 2 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CHI	J FIELDS	6	144.8	4	5	72.7	7.6	13.8
NE	B ZAPPE	2	198.7	4	1	111.4	8.5	11.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CHI	+8.5	41%	42%	+320	20%	21%	o39.5	57%	39%
NE	-8.5	59%	58%	-410	80%	79%	u39.5	43%	61%
Baltimore Ravens at Tampa Bay Buccaneers	Thursday, Oct 27
BAL 101
Cover: +7.5
27@22
FINAL	102 TB
Over: 49
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BAL	+2.5	+115		4-3	3-4-0	2-5-0	22.4	42.6
TB	-2.5	-135	46½	3-4	2-5-0	1-6-0	20.3	+2.1
Referee: C CHEFFERS ( 1 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BAL	L JACKSON	7	199.6	13	6	92.1	7.1	11.6
TB	T BRADY	7	277.4	8	1	92.8	6.6	9.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BAL	+1.5	47%	60%	+105	48%	66%	o46	67%	56%
TB	-1.5	53%	40%	-125	52%	34%	u46	33%	44%
Denver Broncos at Jacksonville Jaguars	Sunday, Oct 30
DEN 251
Cover: +5
21@17
FINAL	252 JAC
Under: 38
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DEN	+1	EVEN		2-5	2-5-0	1-6-0	17.3	37.9
JAC	-1	-120	40½	2-5	2-5-0	4-3-0	20.6	-3.2
Referee: A HILL ( 3 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DEN	B RYPIEN	1	225.0	0	1	56.9	4.9	9.4
JAC	T LAWRENCE	7	243.9	9	4	88.9	6.9	11.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DEN	+2.5	52%	28%	+115	42%	35%	o39.5	33%	38%
JAC	-2.5	48%	72%	-135	58%	65%	u39.5	67%	62%
Chicago Bears at Dallas Cowboys	Sunday, Oct 30
CHI 253
Over: 78
29@49
FINAL	254 DAL
Cover: +10
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CHI	+10	+340		3-4	3-4-0	3-4-0	17.1	42.7
DAL	-10	-440	42½	5-2	5-2-0	2-5-0	25.7	-8.6
Referee: B ROGERS ( 3 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CHI	J FIELDS	7	149.7	5	6	74.6	7.7	13.8
DAL	D PRESCOTT	2	170.5	1	1	77.8	6.3	10.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CHI	+9.5	46%	64%	+350	28%	18%	o43	52%	49%
DAL	-9.5	54%	36%	-435	72%	82%	u43	48%	51%
Las Vegas Raiders at New Orleans Saints	Sunday, Oct 30
LV 255
Under: 24
0@24
FINAL	256 NO
Cover: +25
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LV	-1	-120		2-4	3-3-0	5-1-0	23.3	45.8
NO	+1	EVEN	48½	2-5	2-5-0	5-2-0	22.5	+0.8
Referee: S NOVAK ( 2 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LV	D CARR	6	253.3	9	4	91.3	7.2	11.3
NO	A DALTON	4	236.5	7	4	90.1	7.2	11.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LV	-1.5	65%	75%	-120	72%	64%	o48.5	65%	58%
NO	+1.5	35%	25%	+100	28%	36%	u48.5	35%	42%
Carolina Panthers at Atlanta Falcons	Sunday, Oct 30
CAR 257
Cover: +1
34@37
FINAL	258 ATL
Over: 71
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CAR	+4	+175		2-5	2-5-0	2-5-0	18.7	41.8
ATL	-4	-200	41	3-4	6-1-0	4-3-0	23.1	-4.4
Referee: S HOCHULI ( 2 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CAR	P WALKER	2	99.0	2	0	104.1	6.8	9.6
ATL	M MARIOTA	7	168.4	7	4	90.4	7.9	12.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CAR	+4	40%	40%	+170	27%	30%	o41	61%	64%
ATL	-4	60%	60%	-200	73%	70%	u41	39%	36%
Pittsburgh Steelers at Philadelphia Eagles	Sunday, Oct 30
PIT 259
Over: 48
13@35
FINAL	260 PHI
Cover: +11
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PIT	+11	+435		2-5	3-3-1	2-5-0	17.7	42½
PHI	-11	-575	43	6-0	4-2-0	3-3-0	24.8	-7.1
Referee: C BLAKEMAN ( 4 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PIT	K PICKETT	3	192.8	2	7	66.8	6.1	8.9
PHI	J HURTS	6	252.3	6	2	98.4	8.2	12.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PIT	+11.5	41%	48%	+420	13%	10%	o43	59%	65%
PHI	-11.5	59%	52%	-540	87%	90%	u43	41%	35%
Miami Dolphins at Detroit Lions	Sunday, Oct 30
MIA 261
Over: 58
31@27
FINAL	262 DET
Over: 11
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIA	-4	-200		4-3	3-4-0	2-5-0	27.3	51.4
DET	+4	+175	52	1-5	3-3-0	4-2-0	24.1	+3.2
Referee: A KEMP ( 4 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIA	T TAGOVAILOA	5	259.2	9	3	105.9	8.6	12.8
DET	J GOFF	6	263.8	11	6	90.6	7.5	12.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIA	-4	58%	71%	-190	80%	82%	o52	74%	53%
DET	+4	42%	29%	+160	20%	18%	u52	26%	47%
Arizona Cardinals at Minnesota Vikings	Sunday, Oct 30
ARI 263
Over: 60
26@34
FINAL	264 MIN
Cover: +4
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ARI	+4	+170		3-4	4-3-0	3-4-0	21.2	45.6
MIN	-4	-190	48½	5-1	2-4-0	3-3-0	24.4	-3.2
Referee: B ALLEN ( 3 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ARI	K MURRAY	7	238.1	7	4	83.7	5.9	9.1
MIN	K COUSINS	6	250.3	9	5	88.7	6.6	10.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ARI	+4	74%	54%	+165	50%	38%	o48.5	79%	71%
MIN	-4	26%	46%	-195	50%	62%	u48.5	21%	29%
New England Patriots at New York Jets	Sunday, Oct 30
NE 265
Cover: +2
22@17
FINAL	266 NYJ
Under: 39
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NE	-3	-155		3-4	3-3-1	4-3-0	20.5	41.7
NYJ	+3	+135	40	5-2	5-2-0	3-4-0	21.2	-0.7
Referee: S SMITH ( 2 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NE	M JONES	4	199.8	2	6	70.8	7.8	11.9
NYJ	Z WILSON	4	173.3	1	2	73.6	6.9	12.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NE	-3	54%	36%	-155	46%	28%	o40	36%	55%
NYJ	+3	46%	64%	+135	54%	72%	u40	64%	45%
Tennessee Titans at Houston Texans	Sunday, Oct 30
TEN 267
Cover: +5.5
17@10
FINAL	268 HOU
Under: 27
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TEN	-1.5	-125		4-2	4-2-0	2-4-0	21.7	41.7
HOU	+1.5	+105	39½	1-4-1	4-2-0	3-3-0	20	+1.7
Referee: C MARTIN ( 5 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TEN	M WILLIS	0	6.0	0	0	39.6	1.5	6.0
HOU	D MILLS	6	225.0	7	5	83.6	6.5	10.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TEN	-1.5	77%	83%	-120	77%	81%	o39.5	58%	61%
HOU	+1.5	23%	17%	+100	23%	19%	u39.5	42%	39%
New York Giants at Seattle Seahawks	Sunday, Oct 30
NYG 269
Under: 40
13@27
FINAL	270 SEA
Cover: +10.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYG	+3.5	+155		6-1	6-1-0	2-5-0	19.5	43.9
SEA	-3.5	-175	44½	4-3	4-3-0	4-3-0	24.4	-4.9
Referee: J BOGER ( 2 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYG	D JONES	7	174.7	6	2	90.8	6.5	9.7
SEA	G SMITH	7	244.6	11	3	107.7	8.0	10.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYG	+3	53%	68%	+135	54%	71%	o44.5	71%	70%
SEA	-3	47%	32%	-155	46%	29%	u44.5	29%	30%
Washington Commanders at Indianapolis Colts	Sunday, Oct 30
WAS 271
Cover: +4
17@16
FINAL	272 IND
Under: 33
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
WAS	+3	+130		3-4	3-4-0	3-4-0	18	40.3
IND	-3	-150	40	3-3-1	3-4-0	1-6-0	22.2	-4.2
Referee: C WROLSTAD ( 1 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
WAS	T HEINICKE	1	201.0	2	1	85.5	6.1	10.1
IND	S EHLINGER	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
WAS	+3	40%	60%	+125	53%	55%	o40	58%	60%
IND	-3	60%	40%	-145	47%	45%	u40	42%	40%
San Francisco 49ers at Los Angeles Rams	Sunday, Oct 30
SF 273
Cover: +18
31@14
FINAL	274 LA
Over: 45
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SF	+1	EVEN		3-4	3-4-0	2-5-0	20.6	39.4
LA	-1	-120	42	3-3	2-4-0	1-5-0	18.8	+1.8
Referee: J HUSSEY ( 3 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SF	J GAROPPOLO	5	242.7	9	4	95.7	7.9	12.2
LA	M STAFFORD	6	262.7	6	8	84.6	7.0	9.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SF	-1	62%	64%	-115	58%	61%	o42	56%	72%
LA	+1	38%	36%	-105	42%	39%	u42	44%	28%
Green Bay Packers at Buffalo Bills	Sunday, Oct 30
GB 275
Cover: +1
17@27
FINAL	276 BUF
Under: 44
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
GB	+11	+400		3-4	2-5-0	3-4-0	16.7	43.9
BUF	-11	-500	47½	5-1	4-2-0	1-5-0	27.1	-10.4
Referee: R TORBERT ( 0 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
GB	A RODGERS	7	228.1	11	3	94.9	6.6	9.8
BUF	J ALLEN	6	330.0	17	4	109.1	8.3	12.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
GB	+10.5	45%	43%	+360	20%	15%	o47.5	65%	70%
BUF	-10.5	55%	57%	-450	80%	85%	u47.5	35%	30%
Cincinnati Bengals at Cleveland Browns	Monday, Oct 31
CIN 277
Cover: +1
13@32
FINAL	278 CLE
Cover: +22
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CIN	-3	-185		4-3	5-2-0	2-5-0	26.1	45.9
CLE	+3	+165	45	2-5	4-3-0	5-2-0	19.8	+6.3
Referee: B VINOVICH ( 3 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CIN	J BURROW	7	299.6	15	5	102.7	7.8	11.3
CLE	J BRISSETT	7	226.3	6	5	82.3	6.8	10.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CIN	-3.5	66%	75%	-180	65%	78%	o45	67%	68%
CLE	+3.5	34%	25%	+155	35%	22%	u45	33%	32%
Philadelphia Eagles at Houston Texans	Thursday, Nov 3
PHI 309
Over: 46
29@17
FINAL	310 HOU
Cover: +2
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PHI	-14	-800		7-0	5-2-0	4-3-0	28.9	43.6
HOU	+14	+550	45½	1-5-1	4-3-0	3-4-0	14.7	+14.2
Referee: C WROLSTAD ( 1 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PHI	J HURTS	7	257.0	10	2	105.1	8.5	12.7
HOU	D MILLS	7	214.6	8	6	81.9	6.4	10.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PHI	-14	56%	66%	-800	85%	79%	o45	65%	54%
HOU	+14	44%	34%	+575	15%	21%	u45	35%	46%
Indianapolis Colts at New England Patriots	Sunday, Nov 6
IND 451
Under: 29
3@26
FINAL	452 NE
Cover: +18
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
IND	+5	+180		3-4-1	3-5-0	1-7-0	16.5	39.1
NE	-5	-210	40	4-4	4-3-1	4-4-0	22.6	-6
Referee: C MARTIN ( 5 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
IND	S EHLINGER	1	201.0	0	0	100.1	8.7	11.8
NE	M JONES	5	198.6	3	7	73.1	7.2	10.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
IND	+4.5	32%	31%	+190	8%	17%	o40	28%	46%
NE	-4.5	68%	69%	-225	92%	83%	u40	72%	54%
Buffalo Bills at New York Jets	Sunday, Nov 6
BUF 453
Under: 37
17@20
FINAL	454 NYJ
Cover: +13.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BUF	-10.5	-600		6-1	4-3-0	1-6-0	28.4	44.3
NYJ	+10.5	+450	46	5-3	5-3-0	3-5-0	15.9	+12.5
Referee: L CLARK ( 4 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BUF	J ALLEN	7	314.0	19	6	105.9	8.3	12.7
NYJ	Z WILSON	5	209.6	3	5	71.0	7.4	13.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BUF	-10.5	66%	61%	-520	88%	89%	o46	33%	54%
NYJ	+10.5	34%	39%	+410	12%	11%	u46	67%	46%
Miami Dolphins at Chicago Bears	Sunday, Nov 6
MIA 455
Over: 67
35@32
FINAL	456 CHI
Cover: +1
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIA	-4	-180		5-3	3-4-1	3-5-0	22.8	44.3
CHI	+4	+160	46	3-5	3-5-0	4-4-0	21.5	+1.2
Referee: R TORBERT ( 0 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIA	T TAGOVAILOA	6	279.7	12	3	112.7	9.0	12.9
CHI	J FIELDS	8	149.9	7	6	81.2	7.5	12.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIA	-4	66%	76%	-195	84%	84%	o46	78%	73%
CHI	+4	34%	24%	+165	16%	16%	u46	22%	27%
Minnesota Vikings at Washington Commanders	Sunday, Nov 6
MIN 457
Under: 37
20@17
FINAL	458 WAS
Cover: +10
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIN	-3	-165		6-1	3-4-0	4-3-0	24.7	44.4
WAS	+3	+145	43½	4-4	4-4-0	3-5-0	19.7	+5
Referee: J BOGER ( 2 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIN	K COUSINS	7	247.7	11	5	90.7	6.6	9.9
WAS	T HEINICKE	2	240.0	3	2	91.9	7.5	11.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIN	-3.5	47%	73%	-165	84%	83%	o43	76%	75%
WAS	+3.5	53%	27%	+140	16%	17%	u43	24%	25%
Green Bay Packers at Detroit Lions	Sunday, Nov 6
GB 459
Under: 24
9@15
FINAL	460 DET
Cover: +10
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
GB	-4	-200		3-5	3-5-0	3-5-0	24.6	48.2
DET	+4	+175	49½	1-6	3-3-1	5-2-0	23.6	+1
Referee: T BLAKE ( 3 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
GB	A RODGERS	8	225.0	13	4	94.5	6.6	9.9
DET	J GOFF	7	272.0	12	6	93.2	7.7	12.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
GB	-4	62%	62%	-195	76%	70%	o49.5	57%	52%
DET	+4	38%	38%	+165	24%	30%	u49.5	43%	48%
Los Angeles Chargers at Atlanta Falcons	Sunday, Nov 6
LAC 461
Cover: +0.5
20@17
FINAL	462 ATL
Under: 37
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LAC	-2.5	-140		4-3	3-4-0	4-3-0	24	50
ATL	+2.5	+120	50	4-4	6-2-0	5-3-0	26	-2
Referee: J HUSSEY ( 4 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LAC	J HERBERT	7	287.0	12	4	91.8	6.5	9.9
ATL	M MARIOTA	8	179.0	10	6	92.7	8.0	12.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LAC	-2.5	66%	56%	-140	60%	59%	o49.5	75%	54%
ATL	+2.5	34%	44%	+120	40%	41%	u49.5	25%	46%
Carolina Panthers at Cincinnati Bengals	Sunday, Nov 6
CAR 463
Over: 63
21@42
FINAL	464 CIN
Cover: +14
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CAR	+7	+260		2-6	3-5-0	3-5-0	18.6	43.1
CIN	-7	-320	42½	4-4	5-3-0	2-5-1	24.5	-5.9
Referee: A KEMP ( 5 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CAR	P WALKER	3	153.5	3	1	93.4	7.7	12.3
CIN	J BURROW	8	291.1	17	6	101.9	7.6	11.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CAR	+7	38%	44%	+255	9%	13%	o42.5	62%	74%
CIN	-7	62%	56%	-305	91%	87%	u42.5	38%	26%
Las Vegas Raiders at Jacksonville Jaguars	Sunday, Nov 6
LV 465
Under: 47
20@27
FINAL	466 JAC
Cover: +9.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LV	-2.5	-140		2-5	3-4-0	5-2-0	22.1	46.8
JAC	+2.5	+120	48	2-6	2-6-0	4-4-0	24.7	-2.5
Referee: B VINOVICH ( 3 ov | 3 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LV	D CARR	7	231.6	9	5	86.8	6.8	10.9
JAC	T LAWRENCE	8	230.0	10	6	84.8	6.6	10.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LV	-2.5	68%	57%	-145	57%	46%	o48	73%	39%
JAC	+2.5	32%	43%	+125	43%	54%	u48	27%	61%
Seattle Seahawks at Arizona Cardinals	Sunday, Nov 6
SEA 467
Cover: +12
31@21
FINAL	468 ARI
Over: 52
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SEA	+2	+120		5-3	5-3-0	4-4-0	23.9	48.8
ARI	-2	-140	49	3-5	4-4-0	4-4-0	24.9	-1
Referee: C CHEFFERS ( 2 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SEA	G SMITH	8	240.5	13	3	107.2	7.7	10.6
ARI	K MURRAY	8	249.1	10	6	85.3	6.1	9.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SEA	+2.5	45%	56%	+105	45%	62%	o49	54%	60%
ARI	-2.5	55%	44%	-130	55%	38%	u49	46%	40%
Los Angeles Rams at Tampa Bay Buccaneers	Sunday, Nov 6
LA 469
Under: 29
13@16
FINAL	470 TB
Under: 37
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LA	+3	+135		3-4	2-5-0	2-5-0	18.6	41.9
TB	-3	-155	42½	3-5	2-6-0	2-6-0	23.3	-4.7
Referee: S HOCHULI ( 3 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LA	M STAFFORD	7	251.9	7	8	85.5	6.8	9.7
TB	T BRADY	8	283.4	9	1	92.4	6.7	10.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LA	+3	25%	45%	+135	40%	52%	o43	76%	64%
TB	-3	75%	55%	-155	60%	48%	u43	24%	36%
Tennessee Titans at Kansas City Chiefs	Sunday, Nov 6
TEN 471
Cover: +11
17@20
FINAL	472 KC
Under: 37
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TEN	+14	+600		5-2	5-2-0	2-5-0	15.9	45.7
KC	-14	-900	45	5-2	3-4-0	4-3-0	29.8	-13.8
Referee: C BLAKEMAN ( 5 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TEN	M WILLIS	1	30.5	0	1	32.1	4.4	8.7
KC	P MAHOMES	7	308.4	20	5	109.5	8.2	12.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TEN	+14	53%	63%	+550	22%	18%	o45	59%	70%
KC	-14	47%	37%	-750	78%	82%	u45	41%	30%
Baltimore Ravens at New Orleans Saints	Monday, Nov 7
BAL 473
Cover: +12
27@13
FINAL	474 NO
Under: 40
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BAL	-2	-130		5-3	4-4-0	3-5-0	26.1	48.9
NO	+2	+110	45½	3-5	3-5-0	5-3-0	22.7	+3.4
Referee: B ROGERS ( 4 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BAL	L JACKSON	8	204.4	15	6	94.2	7.0	11.1
NO	A DALTON	5	235.0	9	4	95.1	7.3	11.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BAL	-2	64%	75%	-135	63%	71%	o46	53%	51%
NO	+2	36%	25%	+115	37%	29%	u46	47%	49%
Atlanta Falcons at Carolina Panthers	Thursday, Nov 10
ATL 113
Under: 40
15@25
FINAL	114 CAR
Cover: +12.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ATL	-2.5	-145		4-5	6-3-0	5-4-0	24.5	45.4
CAR	+2.5	+125	41½	2-7	3-6-0	4-5-0	20.9	+3.6
Referee: A HILL ( 3 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ATL	M MARIOTA	9	173.4	10	6	90.0	7.8	12.6
CAR	P WALKER	4	124.6	3	3	77.2	6.9	11.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ATL	-2.5	63%	75%	-145	64%	69%	o41.5	47%	51%
CAR	+2.5	37%	25%	+125	36%	31%	u41.5	53%	49%
Seattle Seahawks at Tampa Bay Buccaneers	Sunday, Nov 13
SEA 241
Under: 37
16@21
FINAL	242 TB
Cover: +2.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SEA	+2.5	+130		6-3	6-3-0	5-4-0	22.5	45½
TB	-2.5	-150	45	4-5	2-6-1	2-7-0	23	-0.5
Referee: J HUSSEY ( 4 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SEA	G SMITH	9	244.3	15	4	107.2	7.8	10.6
TB	T BRADY	9	283.0	10	1	90.5	6.4	9.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SEA	+2.5	43%	53%	+120	50%	58%	o45	48%	49%
TB	-2.5	57%	47%	-140	50%	42%	u45	52%	51%
Jacksonville Jaguars at Kansas City Chiefs	Sunday, Nov 13
JAC 243
Under: 44
17@27
FINAL	244 KC
Cover: +0.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
JAC	+9.5	+380		3-6	3-6-0	4-5-0	20.9	50.9
KC	-9.5	-480	51½	6-2	3-5-0	4-4-0	29.9	-9
Referee: B ROGERS ( 4 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
JAC	T LAWRENCE	9	230.6	11	6	87.5	6.7	10.5
KC	P MAHOMES	8	325.6	21	6	103.6	7.9	11.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
JAC	+9.5	36%	31%	+360	6%	5%	o51.5	49%	45%
KC	-9.5	64%	69%	-450	94%	95%	u51.5	51%	55%
Houston Texans at New York Giants	Sunday, Nov 13
HOU 245
Under: 40
16@24
FINAL	246 NYG
Cover: +3.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
HOU	+4.5	+190		1-6-1	5-3-0	4-4-0	16.7	38.8
NYG	-4.5	-220	41½	6-2	6-2-0	2-6-0	22.2	-5.5
Referee: B VINOVICH ( 3 ov | 4 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
HOU	D MILLS	8	207.0	10	8	81.2	6.4	10.2
NYG	D JONES	8	174.9	6	2	88.1	6.4	9.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
HOU	+4.5	29%	21%	+195	10%	9%	o41.5	45%	49%
NYG	-4.5	71%	79%	-230	90%	91%	u41.5	55%	51%
New Orleans Saints at Pittsburgh Steelers	Sunday, Nov 13
NO 247
Under: 30
10@20
FINAL	248 PIT
Cover: +8.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NO	+1.5	+110		3-6	3-6-0	5-4-0	22.8	43.2
PIT	-1.5	-130	39	2-6	3-4-1	3-5-0	20.4	+2.4
Referee: C CHEFFERS ( 3 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NO	A DALTON	6	230.8	10	5	93.4	7.3	11.2
PIT	K PICKETT	4	192.4	2	8	66.8	5.8	8.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NO	+1	32%	48%	+100	37%	55%	o39.5	54%	48%
PIT	-1	68%	52%	-120	63%	45%	u39.5	46%	52%
Detroit Lions at Chicago Bears	Sunday, Nov 13
DET 249
Cover: +4
31@30
FINAL	250 CHI
Over: 61
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DET	+3	+130		2-6	4-3-1	5-3-0	22.7	47.7
CHI	-3	-150	48½	3-6	4-5-0	5-4-0	25.1	-2.4
Referee: L CLARK ( 4 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DET	J GOFF	8	255.1	14	7	91.8	7.4	11.8
CHI	J FIELDS	9	146.9	10	6	85.0	7.1	12.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DET	+3	24%	23%	+130	34%	31%	o48	77%	62%
CHI	-3	76%	77%	-150	66%	69%	u48	23%	38%
Cleveland Browns at Miami Dolphins	Sunday, Nov 13
CLE 251
Over: 56
17@39
FINAL	252 MIA
Cover: +18.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CLE	+3.5	+160		3-5	5-3-0	5-2-1	23	48.8
MIA	-3.5	-180	49½	6-3	3-5-1	4-5-0	25.8	-2.8
Referee: S HOCHULI ( 3 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CLE	J BRISSETT	8	232.8	7	5	86.8	7.3	11.4
MIA	T TAGOVAILOA	7	282.9	15	3	115.9	9.2	13.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CLE	+3.5	48%	30%	+160	24%	16%	o49.5	75%	61%
MIA	-3.5	52%	70%	-190	76%	84%	u49.5	25%	39%
Minnesota Vikings at Buffalo Bills	Sunday, Nov 13
MIN 253
Cover: +9.5
33@30
FINAL	254 BUF
Over: 63
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIN	+6.5	+220		7-1	3-4-1	4-4-0	18.8	47.2
BUF	-6.5	-260	46½	6-2	4-4-0	1-7-0	28.4	-9.6
Referee: C WROLSTAD ( 2 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIN	K COUSINS	8	249.9	13	6	89.5	6.6	10.2
BUF	J ALLEN	8	300.4	19	8	99.2	8.1	12.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIN	+6.5	56%	62%	+235	45%	41%	o46	54%	68%
BUF	-6.5	44%	38%	-280	55%	59%	u46	46%	32%
Denver Broncos at Tennessee Titans	Sunday, Nov 13
DEN 255
Under: 27
10@17
FINAL	256 TEN
Cover: +5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DEN	+2	+110		3-5	3-5-0	1-7-0	17.2	38.8
TEN	-2	-130	40	5-3	6-2-0	2-6-0	21.7	-4.5
Referee: S NOVAK ( 2 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DEN	R WILSON	7	242.0	6	4	83.5	7.4	12.6
TEN	R TANNEHILL	6	182.8	6	3	92.8	7.5	11.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DEN	+2.5	31%	21%	+115	26%	28%	o39.5	38%	43%
TEN	-2.5	69%	79%	-135	74%	72%	u39.5	62%	57%
Indianapolis Colts at Las Vegas Raiders	Sunday, Nov 13
IND 257
Cover: +9
25@20
FINAL	258 LV
Over: 45
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
IND	+4	+175		3-5-1	3-6-0	1-8-0	18.5	43.1
LV	-4	-200	41	2-6	3-5-0	5-3-0	24.5	-6
Referee: T BLAKE ( 3 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
IND	M RYAN	7	286.9	9	9	84.7	6.8	9.9
LV	D CARR	8	235.0	11	5	88.5	6.9	11.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
IND	+4	33%	30%	+170	39%	27%	o42	46%	45%
LV	-4	67%	70%	-200	61%	73%	u42	54%	55%
Arizona Cardinals at Los Angeles Rams	Sunday, Nov 13
ARI 259
Cover: +13.5
27@17
FINAL	260 LA
Over: 44
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ARI	+3.5	+155		3-6	4-5-0	5-4-0	19.8	42
LA	-3.5	-175	38	3-5	2-5-1	2-6-0	22.2	-2.4
Referee: C BLAKEMAN ( 5 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ARI	K MURRAY	9	240.9	12	6	86.9	6.0	9.0
LA	M STAFFORD	8	241.0	8	8	85.0	6.8	9.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ARI	+3.5	38%	42%	+160	40%	46%	o38	41%	64%
LA	-3.5	62%	58%	-190	60%	54%	u38	59%	36%
Dallas Cowboys at Green Bay Packers	Sunday, Nov 13
DAL 261
Over: 59
28@31
FINAL	262 GB
Cover: +6.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DAL	-3.5	-180		6-2	6-2-0	3-5-0	22.8	42.6
GB	+3.5	+160	44½	3-6	3-6-0	3-6-0	19.8	+3.1
Referee: B ALLEN ( 4 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DAL	D PRESCOTT	3	197.0	3	2	90.1	7.3	10.9
GB	A RODGERS	9	232.3	14	7	89.0	6.6	10.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DAL	-3.5	63%	72%	-200	68%	77%	o44.5	45%	56%
GB	+3.5	37%	28%	+170	32%	23%	u44.5	55%	44%
Los Angeles Chargers at San Francisco 49ers	Sunday, Nov 13
LAC 263
Cover: +2
16@22
FINAL	264 SF
Under: 38
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LAC	+8	+310		5-3	4-4-0	4-4-0	17.9	44½
SF	-8	-370	46	4-4	4-4-0	3-5-0	26.6	-8.7
Referee: S SMITH ( 2 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LAC	J HERBERT	8	281.8	13	5	90.6	6.4	9.7
SF	J GAROPPOLO	6	241.6	11	4	100.7	8.1	12.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LAC	+8	58%	60%	+270	29%	23%	o45.5	53%	63%
SF	-8	42%	40%	-325	71%	77%	u45.5	47%	37%
Washington Commanders at Philadelphia Eagles	Monday, Nov 14
WAS 265
Cover: +22
32@21
FINAL	266 PHI
Over: 53
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
WAS	+11	+400		4-5	4-4-1	3-6-0	18.7	44
PHI	-11	-500	42½	8-0	5-3-0	5-3-0	25.3	-6.6
Referee: A KEMP ( 6 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
WAS	T HEINICKE	3	209.7	5	3	87.6	6.8	10.8
PHI	J HURTS	8	255.3	12	2	107.8	8.5	12.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
WAS	+11	52%	54%	+400	17%	17%	o43	52%	58%
PHI	-11	48%	46%	-500	83%	83%	u43	48%	42%
Tennessee Titans at Green Bay Packers	Thursday, Nov 17
TEN 311
Cover: +13.5
27@17
FINAL	312 GB
Over: 44
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TEN	+3.5	+165		6-3	7-2-0	2-7-0	19.9	41.1
GB	-3.5	-185	40½	4-6	4-6-0	4-6-0	21.2	-1.3
Referee: B VINOVICH ( 3 ov | 5 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TEN	R TANNEHILL	7	193.1	8	3	93.0	7.4	11.9
GB	A RODGERS	10	231.5	17	7	93.0	6.9	10.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TEN	+3	52%	57%	+140	48%	59%	o40.5	56%	54%
GB	-3	48%	43%	-165	52%	41%	u40.5	44%	46%
Carolina Panthers at Baltimore Ravens	Sunday, Nov 20
CAR 451
Cover: +2.5
3@13
FINAL	452 BAL
Under: 16
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CAR	+12.5	+550		3-7	4-6-0	4-6-0	14.3	41.9
BAL	-12.5	-800	41½	6-3	5-4-0	3-6-0	27.5	-13.2
Referee: J BOGER ( 2 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CAR	B MAYFIELD	5	186.2	6	4	78.1	6.5	11.4
BAL	L JACKSON	9	196.4	16	6	93.7	6.9	11.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CAR	+12.5	56%	60%	+470	13%	8%	o41.5	46%	63%
BAL	-12.5	44%	40%	-625	87%	92%	u41.5	54%	37%
Philadelphia Eagles at Indianapolis Colts	Sunday, Nov 20
PHI 455
Under: 33
17@16
FINAL	456 IND
Cover: +5.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PHI	-6.5	-300		8-1	5-4-0	6-3-0	26.4	43.4
IND	+6.5	+250	45½	4-5-1	4-6-0	2-8-0	17	+9.4
Referee: L CLARK ( 5 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PHI	J HURTS	9	246.3	14	3	106.4	8.4	12.3
IND	M RYAN	8	278.8	10	9	86.8	6.9	10.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PHI	-6.5	65%	71%	-285	83%	87%	o45.5	77%	67%
IND	+6.5	35%	29%	+240	17%	13%	u45.5	23%	33%
Washington Commanders at Houston Texans	Sunday, Nov 20
WAS 457
Cover: +10
23@10
FINAL	458 HOU
Under: 33
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
WAS	-3	-160		5-5	5-4-1	4-6-0	22.2	41.4
HOU	+3	+140	41	1-7-1	5-4-0	4-5-0	19.2	+3
Referee: S NOVAK ( 2 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
WAS	T HEINICKE	4	210.0	5	4	82.7	6.9	11.2
HOU	D MILLS	9	219.4	11	9	81.7	6.7	10.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
WAS	-3	52%	73%	-155	82%	82%	o41	67%	59%
HOU	+3	48%	27%	+135	18%	18%	u41	33%	41%
New York Jets at New England Patriots	Sunday, Nov 20
NYJ 459
Under: 13
3@10
FINAL	460 NE
Cover: +3.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYJ	+3.5	+155		6-3	6-3-0	3-6-0	19	40.1
NE	-3.5	-175	38½	5-4	5-3-1	4-5-0	21.2	-2.2
Referee: C CHEFFERS ( 3 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYJ	Z WILSON	6	200.3	4	5	75.5	7.2	12.5
NE	M JONES	5	190.0	4	7	76.0	6.8	10.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYJ	+3.5	62%	65%	+145	58%	57%	o38	50%	52%
NE	-3.5	38%	35%	-170	42%	43%	u38	50%	48%
Detroit Lions at New York Giants	Sunday, Nov 20
DET 461
Cover: +16
31@18
FINAL	462 NYG
Over: 49
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DET	+3	+140		3-6	5-3-1	6-3-0	21.3	45.8
NYG	-3	-160	44½	7-2	7-2-0	2-7-0	24.5	-3.2
Referee: B ROGERS ( 4 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DET	J GOFF	9	253.0	15	7	93.7	7.6	11.9
NYG	D JONES	9	177.3	8	2	92.7	6.7	10.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DET	+3	32%	25%	+140	23%	24%	o44	50%	59%
NYG	-3	68%	75%	-170	77%	76%	u44	50%	41%
Los Angeles Rams at New Orleans Saints	Sunday, Nov 20
LA 463
Over: 47
20@27
FINAL	464 NO
Cover: +5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LA	+2	+120		3-6	2-6-1	3-6-0	16.1	40
NO	-2	-140	39	3-7	3-7-0	5-5-0	23.9	-7.8
Referee: R TORBERT ( 1 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LA	M STAFFORD	8	241.0	8	8	85.0	6.8	9.9
NO	A DALTON	7	222.7	11	7	89.6	7.2	11.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LA	+2	35%	48%	+120	67%	56%	o39	35%	51%
NO	-2	65%	52%	-140	33%	44%	u39	65%	49%
Chicago Bears at Atlanta Falcons	Sunday, Nov 20
CHI 465
Over: 51
24@27
FINAL	466 ATL
Cover: +1
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CHI	+2	+120		3-7	4-6-0	6-4-0	22.8	48.2
ATL	-2	-140	48	4-6	6-4-0	5-5-0	25.4	-2.6
Referee: T BLAKE ( 4 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CHI	J FIELDS	10	148.9	12	7	86.4	7.2	12.2
ATL	M MARIOTA	10	174.7	12	7	89.9	7.6	12.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CHI	+2.5	72%	75%	+115	73%	75%	o48.5	61%	55%
ATL	-2.5	28%	25%	-135	27%	25%	u48.5	39%	45%
Cleveland Browns at Buffalo Bills	Sunday, Nov 20
CLE 477
Over: 54
23@31
FINAL	478 BUF
Cover: +0.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CLE	+7.5	+300		3-6	5-4-0	6-2-1	20.5	47.6
BUF	-7.5	-360	50½	6-3	4-5-0	2-7-0	27.1	-6.5
Referee: A HILL ( 3 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CLE	J BRISSETT	9	230.4	8	5	87.1	7.2	11.2
BUF	J ALLEN	9	303.7	20	10	96.6	8.0	12.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CLE	+7.5	32%	29%	+300	6%	8%	o50.5	46%	41%
BUF	-7.5	68%	71%	-365	94%	92%	u50.5	54%	59%
Las Vegas Raiders at Denver Broncos	Sunday, Nov 20
LV 467
Cover: +8.5
22@16
FINAL	468 DEN
Under: 38
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LV	+2.5	+125		2-7	3-6-0	6-3-0	19.1	40.3
DEN	-2.5	-145	41½	3-6	3-6-0	1-8-0	21.3	-2.2
Referee: S SMITH ( 2 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LV	D CARR	9	236.4	13	5	89.8	6.8	11.0
DEN	R WILSON	8	247.5	7	5	81.4	7.3	12.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LV	+2.5	47%	55%	+120	55%	55%	o41.5	34%	37%
DEN	-2.5	53%	45%	-140	45%	45%	u41.5	66%	63%
Dallas Cowboys at Minnesota Vikings	Sunday, Nov 20
DAL 471
Cover: +34.5
40@3
FINAL	472 MIN
Under: 43
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DAL	-2.5	-145		6-3	6-3-0	4-5-0	23.9	47.9
MIN	+2.5	+125	48½	8-1	4-4-1	5-4-0	24	-0.1
Referee: C MARTIN ( 5 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DAL	D PRESCOTT	4	214.0	6	4	85.9	6.7	10.6
MIN	K COUSINS	9	261.8	14	8	87.0	6.7	10.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DAL	-2	57%	42%	-130	50%	29%	o49	76%	71%
MIN	+2	43%	58%	+110	50%	71%	u49	24%	29%
Cincinnati Bengals at Pittsburgh Steelers	Sunday, Nov 20
CIN 473
Cover: +3.5
37@30
FINAL	474 PIT
Over: 67
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CIN	-3.5	-175		5-4	6-3-0	3-5-1	23.8	40.6
PIT	+3.5	+155	39½	3-6	4-4-1	3-6-0	16.7	+7.1
Referee: B ALLEN ( 5 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CIN	J BURROW	9	281.7	18	6	102.6	7.6	10.9
PIT	K PICKETT	5	193.5	2	8	68.8	6.0	8.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CIN	-3.5	55%	65%	-190	73%	78%	o39.5	64%	72%
PIT	+3.5	45%	35%	+160	27%	22%	u39.5	36%	28%
Kansas City Chiefs at Los Angeles Chargers	Sunday, Nov 20
KC 469
Over: 57
30@27
FINAL	470 LAC
Cover: +1.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
KC	-4.5	-220		7-2	4-5-0	4-5-0	27.9	49.8
LAC	+4.5	+190	53	5-4	5-4-0	4-5-0	21.9	+6
Referee: S HOCHULI ( 4 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
KC	P MAHOMES	9	326.2	25	7	106.1	8.0	12.0
LAC	J HERBERT	9	272.2	14	6	89.0	6.4	9.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
KC	-5.5	51%	65%	-230	65%	82%	o52.5	63%	65%
LAC	+5.5	49%	35%	+195	35%	18%	u52.5	37%	35%
San Francisco 49ers at Arizona Cardinals	Monday, Nov 21
SF 475
Cover: +18.5
38@10
FINAL	476 ARI
Over: 48
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SF	-9.5	-450		5-4	4-5-0	3-6-0	24.8	39.9
ARI	+9.5	+350	43	4-6	5-5-0	6-4-0	15.2	+9.6
Referee: C WROLSTAD ( 3 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SF	J GAROPPOLO	7	241.4	11	4	100.0	8.1	12.1
ARI	K MURRAY	9	240.9	12	6	86.9	6.0	9.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SF	-9.5	38%	40%	-410	68%	75%	o43	54%	63%
ARI	+9.5	62%	60%	+330	32%	25%	u43	46%	37%
Buffalo Bills at Detroit Lions	Thursday, Nov 24
BUF 105
Under: 53
28@25
FINAL	106 DET
Cover: +6.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BUF	-9.5	-450		7-3	5-5-0	3-7-0	31	49½
DET	+9.5	+350	55	4-6	6-3-1	7-3-0	18.5	+12.5
Referee: C BLAKEMAN ( 6 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BUF	J ALLEN	10	293.0	21	10	96.9	8.0	12.3
DET	J GOFF	10	244.2	15	7	92.8	7.5	11.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BUF	-9.5	51%	47%	-410	74%	75%	o54.5	59%	57%
DET	+9.5	49%	53%	+330	26%	25%	u54.5	41%	43%
New York Giants at Dallas Cowboys	Thursday, Nov 24
NYG 107
Cover: +2
20@28
FINAL	108 DAL
Over: 48
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYG	+10	+400		7-3	7-3-0	3-7-0	17	43.4
DAL	-10	-500	45½	7-3	7-3-0	4-6-0	26.4	-9.5
Referee: S NOVAK ( 2 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYG	D JONES	10	193.7	9	4	89.8	6.9	10.6
DAL	D PRESCOTT	5	226.4	8	4	96.2	7.5	11.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYG	+10	59%	65%	+350	32%	36%	o45.5	63%	64%
DAL	-10	41%	35%	-435	68%	64%	u45.5	37%	36%
New England Patriots at Minnesota Vikings	Thursday, Nov 24
NE 109
Over: 59
26@33
FINAL	110 MIN
Cover: +4.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NE	+2.5	+125		6-4	6-3-1	4-6-0	21.1	42.6
MIN	-2.5	-145	42	8-2	4-5-1	5-5-0	21.5	-0.4
Referee: A KEMP ( 7 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NE	M JONES	6	198.0	4	7	80.8	7.1	10.3
MIN	K COUSINS	10	246.1	14	8	85.7	6.5	10.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NE	+2.5	26%	25%	+125	31%	34%	o42	51%	44%
MIN	-2.5	74%	75%	-145	69%	66%	u42	49%	56%
Baltimore Ravens at Jacksonville Jaguars	Sunday, Nov 27
BAL 251
Over: 55
27@28
FINAL	252 JAC
Cover: +4.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BAL	-3.5	-165		7-3	5-5-0	3-7-0	23.9	44.7
JAC	+3.5	+145	43	3-7	3-7-0	4-6-0	20.8	+3.1
Referee: L CLARK ( 5 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BAL	L JACKSON	10	197.7	16	7	91.7	6.8	10.7
JAC	T LAWRENCE	10	233.4	13	6	89.7	6.7	10.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BAL	-3	72%	79%	-175	91%	88%	o43	58%	60%
JAC	+3	28%	21%	+150	9%	12%	u43	42%	40%
Denver Broncos at Carolina Panthers	Sunday, Nov 27
DEN 253
Under: 33
10@23
FINAL	254 CAR
Cover: +13
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DEN	PICK	-110		3-7	3-7-0	1-9-0	17.9	36.3
CAR	PICK	-110	36½	3-8	5-6-0	4-7-0	18.4	-0.5
Referee: C MARTIN ( 5 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DEN	R WILSON	9	247.4	7	5	83.3	7.4	12.4
CAR	S DARNOLD	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DEN	-1	70%	71%	-110	65%	61%	o37	38%	44%
CAR	+1	30%	29%	-110	35%	39%	u37	62%	56%
Atlanta Falcons at Washington Commanders	Sunday, Nov 27
ATL 255
Under: 32
13@19
FINAL	256 WAS
Cover: +2.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ATL	+3.5	+175		5-6	7-4-0	6-5-0	18.6	40.9
WAS	-3.5	-200	40½	6-5	6-4-1	4-7-0	22.4	-3.8
Referee: B ROGERS ( 5 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ATL	M MARIOTA	11	170.7	13	7	90.7	7.5	12.0
WAS	T HEINICKE	5	206.2	5	4	81.8	7.0	11.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ATL	+3.5	32%	35%	+165	25%	27%	o40.5	77%	76%
WAS	-3.5	68%	65%	-195	75%	73%	u40.5	23%	24%
Tampa Bay Buccaneers at Cleveland Browns	Sunday, Nov 27
TB 257
Under: 40
17@23
FINAL	258 CLE
Cover: +9.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TB	-3.5	-165		5-5	3-6-1	2-8-0	22.4	43
CLE	+3.5	+145	42	3-7	5-5-0	7-2-1	20.6	+1.8
Referee: T BLAKE ( 5 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TB	T BRADY	10	280.5	12	2	91.9	6.6	10.0
CLE	J BRISSETT	10	239.8	11	5	90.7	7.2	11.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TB	-3.5	59%	70%	-180	81%	79%	o42	59%	67%
CLE	+3.5	41%	30%	+155	19%	21%	u42	41%	33%
Cincinnati Bengals at Tennessee Titans	Sunday, Nov 27
CIN 259
Cover: +4
20@16
FINAL	260 TEN
Under: 36
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CIN	PICK	-110		6-4	7-3-0	4-5-1	21.7	42.8
TEN	PICK	-110	42½	7-3	8-2-0	3-7-0	21.1	+0.6
Referee: C CHEFFERS ( 3 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CIN	J BURROW	10	289.0	22	8	102.8	7.8	11.3
TEN	R TANNEHILL	8	210.6	10	4	97.9	8.1	12.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CIN	-1	47%	44%	-105	44%	41%	o42	73%	79%
TEN	+1	53%	56%	-115	56%	59%	u42	27%	21%
Houston Texans at Miami Dolphins	Sunday, Nov 27
HOU 261
Under: 45
15@30
FINAL	262 MIA
Cover: +1
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
HOU	+14	+600		1-8-1	5-5-0	4-6-0	15.9	45
MIA	-14	-900	47½	7-3	4-5-1	5-5-0	29.1	-13.2
Referee: J BOGER ( 2 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
HOU	K ALLEN	0	0.0	0	0	0.0	0.0	0.0
MIA	T TAGOVAILOA	8	283.1	18	3	118.4	9.1	12.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
HOU	+14	38%	38%	+625	16%	8%	o47.5	57%	52%
MIA	-14	62%	62%	-900	84%	92%	u47.5	43%	48%
Chicago Bears at New York Jets	Sunday, Nov 27
CHI 263
Over: 41
10@31
FINAL	264 NYJ
Cover: +13
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CHI	+8	+300		3-8	4-7-0	7-4-0	18.6	41.4
NYJ	-8	-360	36½	6-4	6-4-0	3-7-0	22.8	-4.2
Referee: J HUSSEY ( 4 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CHI	T SIEMIAN	0	5.0	0	0	87.5	5.0	5.0
NYJ	M WHITE	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CHI	+8	39%	54%	+300	39%	35%	o36.5	26%	42%
NYJ	-8	61%	46%	-365	61%	65%	u36.5	74%	58%
Las Vegas Raiders at Seattle Seahawks	Sunday, Nov 27
LV 265
Cover: +10
40@34
FINAL	266 SEA
Over: 74
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LV	+4	+165		3-7	4-6-0	6-4-0	22.3	48.2
SEA	-4	-185	48	6-4	6-4-0	5-5-0	25.9	-3.5
Referee: B ALLEN ( 6 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LV	D CARR	10	243.5	15	5	91.6	7.0	11.2
SEA	G SMITH	10	247.4	17	4	108.0	7.8	10.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LV	+4	38%	32%	+170	33%	26%	o47.5	79%	58%
SEA	-4	62%	68%	-200	67%	74%	u47.5	21%	42%
Los Angeles Chargers at Arizona Cardinals	Sunday, Nov 27
LAC 267
Over: 49
25@24
FINAL	268 ARI
Cover: +1.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LAC	-2.5	-145		5-5	6-4-0	5-5-0	24	47.7
ARI	+2.5	+125	48½	4-7	5-6-0	7-4-0	23.8	+0.2
Referee: R TORBERT ( 2 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LAC	J HERBERT	10	273.0	16	7	90.7	6.6	9.9
ARI	K MURRAY	9	240.9	12	6	86.9	6.0	9.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LAC	-2.5	75%	77%	-150	76%	72%	o49	78%	65%
ARI	+2.5	25%	23%	+130	24%	28%	u49	22%	35%
Los Angeles Rams at Kansas City Chiefs	Sunday, Nov 27
LA 269
Under: 36
10@26
FINAL	270 KC
Cover: +0.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LA	+15.5	+800		3-7	2-7-1	4-6-0	14.3	43.9
KC	-15.5	-1400	42	8-2	4-6-0	5-5-0	29.5	-15.2
Referee: A HILL ( 4 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LA	B PERKINS	0	30.5	0	0	70.6	5.6	10.2
KC	P MAHOMES	10	326.5	28	7	107.3	8.2	12.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LA	+16	43%	55%	+800	23%	11%	o42	82%	85%
KC	-16	57%	45%	-1250	77%	89%	u42	18%	15%
New Orleans Saints at San Francisco 49ers	Sunday, Nov 27
NO 271
Under: 13
0@13
FINAL	272 SF
Cover: +4
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NO	+9	+335		4-7	4-7-0	6-5-0	16.9	43½
SF	-9	-420	43½	6-4	5-5-0	4-6-0	26.6	-9.7
Referee: S HOCHULI ( 5 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NO	A DALTON	8	227.4	14	7	96.4	7.5	11.2
SF	J GAROPPOLO	8	239.9	15	4	104.1	8.1	12.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NO	+8.5	35%	38%	+330	11%	8%	o43.5	62%	68%
SF	-8.5	65%	62%	-410	89%	92%	u43.5	38%	32%
Green Bay Packers at Philadelphia Eagles	Sunday, Nov 27
GB 273
Over: 73
33@40
FINAL	274 PHI
Cover: +1
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
GB	+6	+250		4-7	4-7-0	5-6-0	19.1	44.6
PHI	-6	-300	46½	9-1	5-5-0	6-4-0	25.4	-6.3
Referee: S SMITH ( 2 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
GB	A RODGERS	11	231.1	19	7	93.2	6.8	10.5
PHI	J HURTS	10	240.7	15	3	106.5	8.3	12.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
GB	+6.5	35%	35%	+225	34%	23%	o46	69%	65%
PHI	-6.5	65%	65%	-265	66%	77%	u46	31%	35%
Pittsburgh Steelers at Indianapolis Colts	Monday, Nov 28
PIT 275
Cover: +9.5
24@17
FINAL	276 IND
Over: 41
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PIT	+2.5	+120		3-7	4-5-1	4-6-0	18.4	39.9
IND	-2.5	-140	39½	4-6-1	5-6-0	2-9-0	21.5	-3.1
Referee: B VINOVICH ( 4 ov | 5 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PIT	K PICKETT	6	203.7	3	8	71.8	6.0	9.2
IND	M RYAN	9	271.4	10	9	87.1	6.8	9.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PIT	+2.5	38%	37%	+120	42%	48%	o39.5	63%	58%
IND	-2.5	62%	63%	-140	58%	52%	u39.5	37%	42%
Buffalo Bills at New England Patriots	Thursday, Dec 1
BUF 301
Cover: +10.5
24@10
FINAL	302 NE
Under: 34
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BUF	-3.5	-200		8-3	5-6-0	3-8-0	23.4	43.6
NE	+3.5	+175	43½	6-5	6-4-1	5-6-0	20.2	+3.2
Referee: S HOCHULI ( 5 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BUF	J ALLEN	11	289.4	23	11	95.2	7.8	12.2
NE	M JONES	7	221.0	6	7	87.3	7.6	10.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BUF	-4	66%	73%	-205	82%	79%	o43.5	66%	67%
NE	+4	34%	27%	+175	18%	21%	u43.5	34%	33%
New York Jets at Minnesota Vikings	Sunday, Dec 4
NYJ 451
Over: 49
22@27
FINAL	452 MIN
Cover: +2.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYJ	+2.5	+130		7-4	7-4-0	4-7-0	22.5	45.1
MIN	-2.5	-150	43½	9-2	5-5-1	6-5-0	22.7	-0.2
Referee: C BLAKEMAN ( 6 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYJ	M WHITE	1	315.0	3	0	149.3	11.3	14.3
MIN	K COUSINS	11	250.9	17	9	88.6	6.7	10.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYJ	+3	47%	36%	+125	35%	31%	o44	75%	72%
MIN	-3	53%	64%	-145	65%	69%	u44	25%	28%
Denver Broncos at Baltimore Ravens	Sunday, Dec 4
DEN 453
Cover: +7.5
9@10
FINAL	454 BAL
Under: 19
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DEN	+8.5	+340		3-8	3-8-0	1-10-0	15.5	38.7
BAL	-8.5	-440	40½	7-4	5-6-0	4-7-0	23.3	-7.8
Referee: A KEMP ( 8 ov | 2 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DEN	R WILSON	10	236.9	8	5	82.3	7.1	12.0
BAL	L JACKSON	11	202.8	17	7	91.3	6.9	11.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DEN	+8.5	36%	40%	+330	9%	8%	o40.5	37%	37%
BAL	-8.5	64%	60%	-410	91%	92%	u40.5	63%	63%
Pittsburgh Steelers at Atlanta Falcons	Sunday, Dec 4
PIT 455
Cover: +2
19@16
FINAL	456 ATL
Under: 35
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PIT	-1	-125		4-7	5-5-1	5-6-0	21	43½
ATL	+1	+105	42½	5-7	7-5-0	6-6-0	22.5	-1.4
Referee: R TORBERT ( 2 ov | 7 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PIT	K PICKETT	7	200.0	3	8	73.5	6.0	9.1
ATL	M MARIOTA	12	171.0	14	8	89.5	7.4	12.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PIT	-1	64%	59%	-120	60%	56%	o43	66%	54%
ATL	+1	36%	41%	+100	40%	44%	u43	34%	46%
Tennessee Titans at Philadelphia Eagles	Sunday, Dec 4
TEN 457
Over: 45
10@35
FINAL	458 PHI
Cover: +21
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TEN	+4	+180		7-4	8-3-0	3-8-0	19.9	45.7
PHI	-4	-210	44	10-1	6-5-0	7-4-0	25.8	-5.9
Referee: A HILL ( 4 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TEN	R TANNEHILL	9	219.6	10	4	97.0	8.1	12.5
PHI	J HURTS	11	232.7	17	3	105.6	8.1	12.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TEN	+4.5	55%	51%	+190	31%	24%	o44.5	68%	72%
PHI	-4.5	45%	49%	-225	69%	76%	u44.5	32%	28%
Jacksonville Jaguars at Detroit Lions	Sunday, Dec 4
JAC 459
Over: 54
14@40
FINAL	460 DET
Cover: +24.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
JAC	+1.5	+110		4-7	4-7-0	5-6-0	24.9	51.1
DET	-1.5	-130	51½	4-7	7-3-1	7-4-0	26.2	-1.3
Referee: J BOGER ( 2 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
JAC	T LAWRENCE	11	241.4	16	6	93.6	6.9	10.4
DET	J GOFF	11	243.8	17	7	93.5	7.4	11.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
JAC	+1.5	38%	29%	+100	30%	35%	o51.5	72%	64%
DET	-1.5	62%	71%	-120	70%	65%	u51.5	28%	36%
Washington Commanders at New York Giants	Sunday, Dec 4
WAS 461
Under: 40
20@20
FINAL	462 NYG
Cover: +2
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
WAS	-2	-130		7-5	7-4-1	4-8-0	19.9	39.8
NYG	+2	+110	40½	7-4	8-3-0	4-7-0	19.8	+0.1
Referee: B ALLEN ( 7 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
WAS	T HEINICKE	6	194.8	7	5	82.7	6.8	11.2
NYG	D JONES	11	196.8	10	4	89.7	6.9	10.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
WAS	-2	38%	43%	-130	45%	39%	o40	46%	61%
NYG	+2	62%	57%	+110	55%	61%	u40	54%	39%
Cleveland Browns at Houston Texans	Sunday, Dec 4
CLE 463
Cover: +5
27@14
FINAL	464 HOU
Under: 41
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CLE	-8	-320		4-7	6-5-0	7-3-1	26.6	45.9
HOU	+8	+260	46	1-9-1	5-6-0	4-7-0	19.4	+7.2
Referee: L CLARK ( 6 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CLE	D WATSON	0	0.0	0	0	0.0	0.0	0.0
HOU	K ALLEN	1	215.0	1	2	67.8	5.5	8.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CLE	-7.5	55%	65%	-330	87%	90%	o46	31%	31%
HOU	+7.5	45%	35%	+275	13%	10%	u46	69%	69%
Green Bay Packers at Chicago Bears	Sunday, Dec 4
GB 465
Cover: +5.5
28@19
FINAL	466 CHI
Over: 47
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
GB	-3.5	-185		4-8	4-8-0	6-6-0	21.4	41.7
CHI	+3.5	+165	45	3-9	4-8-0	8-4-0	20.3	+1.1
Referee: S NOVAK ( 3 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
GB	A RODGERS	12	223.5	21	9	92.9	6.8	10.6
CHI	J FIELDS	11	149.3	13	8	86.2	7.2	12.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
GB	-3.5	55%	55%	-180	65%	69%	o45	73%	61%
CHI	+3.5	45%	45%	+155	35%	31%	u45	27%	39%
Seattle Seahawks at Los Angeles Rams	Sunday, Dec 4
SEA 467
Over: 50
27@23
FINAL	468 LA
Cover: +2.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SEA	-6.5	-330		6-5	6-5-0	6-5-0	24.4	40.7
LA	+6.5	+270	41	3-8	2-7-2	4-7-0	16.3	+8
Referee: S SMITH ( 3 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SEA	G SMITH	11	254.7	19	5	107.9	7.9	10.9
LA	J WOLFORD	1	212.0	1	1	79.9	5.9	8.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SEA	-6.5	68%	74%	-275	85%	87%	o41	46%	59%
LA	+6.5	32%	26%	+230	15%	13%	u41	54%	41%
Miami Dolphins at San Francisco 49ers	Sunday, Dec 4
MIA 469
Over: 50
17@33
FINAL	470 SF
Cover: +11
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIA	+5	+190		8-3	5-5-1	5-6-0	21.8	46.7
SF	-5	-220	46	7-4	6-5-0	4-7-0	24.9	-3.1
Referee: T BLAKE ( 5 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIA	T TAGOVAILOA	9	284.9	19	3	115.7	9.0	13.0
SF	J GAROPPOLO	9	238.1	16	4	103.0	7.8	11.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIA	+5	59%	71%	+195	47%	56%	o46	65%	76%
SF	-5	41%	29%	-230	53%	44%	u46	35%	24%
Los Angeles Chargers at Las Vegas Raiders	Sunday, Dec 4
LAC 471
Under: 47
20@27
FINAL	472 LV
Cover: +4.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LAC	+2.5	+120		6-5	6-5-0	5-5-1	24.7	50
LV	-2.5	-140	49½	4-7	5-6-0	7-4-0	25.3	-0.6
Referee: C WROLSTAD ( 4 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LAC	J HERBERT	11	273.1	19	7	92.7	6.5	9.6
LV	D CARR	11	248.2	18	7	92.3	7.1	11.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LAC	+2.5	55%	66%	+115	64%	69%	o49.5	74%	69%
LV	-2.5	45%	34%	-135	36%	31%	u49.5	26%	31%
Kansas City Chiefs at Cincinnati Bengals	Sunday, Dec 4
KC 473
Under: 51
24@27
FINAL	474 CIN
Cover: +5.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
KC	-2.5	-135		9-2	4-6-1	5-6-0	25.5	50.8
CIN	+2.5	+115	54	7-4	8-3-0	4-6-1	25.3	+0.2
Referee: J HUSSEY ( 5 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
KC	P MAHOMES	11	325.9	29	8	105.3	8.1	12.3
CIN	J BURROW	11	287.3	23	8	101.7	7.7	11.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
KC	-2.5	77%	78%	-150	76%	74%	o53.5	86%	82%
CIN	+2.5	23%	22%	+130	24%	26%	u53.5	14%	18%
Indianapolis Colts at Dallas Cowboys	Sunday, Dec 4
IND 475
Over: 73
19@54
FINAL	476 DAL
Cover: +24
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
IND	+11	+450		4-7-1	5-7-0	3-9-0	16.8	44.4
DAL	-11	-600	45	8-3	7-4-0	5-6-0	27.6	-10.7
Referee: C CHEFFERS ( 3 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
IND	M RYAN	10	264.2	11	10	86.3	6.8	9.8
DAL	D PRESCOTT	6	232.2	10	6	95.3	7.7	11.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
IND	+11	46%	43%	+420	18%	12%	o44.5	53%	59%
DAL	-11	54%	57%	-540	82%	88%	u44.5	47%	41%
New Orleans Saints at Tampa Bay Buccaneers	Monday, Dec 5
NO 477
Cover: +2.5
16@17
FINAL	478 TB
Under: 33
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NO	+3.5	+175		4-8	4-8-0	6-6-0	18.9	41.6
TB	-3.5	-200	41	5-6	3-7-1	2-9-0	22.6	-3.7
Referee: C MARTIN ( 5 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NO	A DALTON	9	224.8	14	7	95.0	7.5	11.2
TB	T BRADY	11	277.4	14	2	92.4	6.5	9.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NO	+3.5	41%	31%	+165	18%	21%	o40.5	54%	54%
TB	-3.5	59%	69%	-195	82%	79%	u40.5	46%	46%
Las Vegas Raiders at Los Angeles Rams	Thursday, Dec 8
LV 101
Under: 33
16@17
FINAL	102 LA
Cover: +7
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LV	-6	-270		5-7	6-6-0	7-5-0	24.4	43.4
LA	+6	+230	42	3-9	3-7-2	5-7-0	19	+5.5
Referee: B ROGERS ( 5 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LV	D CARR	12	248.3	20	8	92.1	7.2	11.6
LA	B MAYFIELD	6	187.6	6	6	74.4	6.4	11.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LV	-6.5	71%	70%	-295	81%	76%	o42	64%	59%
LA	+6.5	29%	30%	+245	19%	24%	u42	36%	41%
Minnesota Vikings at Detroit Lions	Sunday, Dec 11
MIN 105
Over: 57
23@34
FINAL	106 DET
Cover: +9
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIN	+2	+115		10-2	6-5-1	7-5-0	22.9	49
DET	-2	-135	51½	5-7	8-3-1	8-4-0	26.1	-3.2
Referee: R TORBERT ( 2 ov | 8 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIN	K COUSINS	12	244.4	18	9	88.1	6.5	10.1
DET	J GOFF	12	251.8	19	7	95.7	7.5	11.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIN	+2.5	48%	64%	+120	68%	75%	o51	82%	77%
DET	-2.5	52%	36%	-140	32%	25%	u51	18%	23%
New York Jets at Buffalo Bills	Sunday, Dec 11
NYJ 107
Cover: +2
12@20
FINAL	108 BUF
Under: 32
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYJ	+10	+375		7-5	7-5-0	5-7-0	16.6	43.7
BUF	-10	-475	43½	9-3	6-6-0	3-9-0	27.1	-10.5
Referee: A KEMP ( 8 ov | 3 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYJ	M WHITE	2	342.0	3	2	89.5	8.1	12.9
BUF	J ALLEN	12	283.8	25	11	96.0	7.7	12.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYJ	+9.5	61%	70%	+370	17%	15%	o44	57%	59%
BUF	-9.5	39%	30%	-460	83%	85%	u44	43%	41%
Baltimore Ravens at Pittsburgh Steelers	Sunday, Dec 11
BAL 109
Cover: +3.5
16@14
FINAL	110 PIT
Under: 30
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BAL	+1.5	+110		8-4	5-7-0	4-8-0	16.1	36.2
PIT	-1.5	-130	36½	5-7	6-5-1	5-7-0	20.1	-4
Referee: A HILL ( 5 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BAL	T HUNTLEY	0	187.0	0	1	78.0	5.8	6.9
PIT	K PICKETT	8	199.7	4	8	75.1	6.1	9.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BAL	+2	47%	44%	+110	48%	51%	o36.5	36%	41%
PIT	-2	53%	56%	-130	52%	49%	u36.5	64%	59%
Philadelphia Eagles at New York Giants	Sunday, Dec 11
PHI 111
Cover: +19
48@22
FINAL	112 NYG
Over: 70
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PHI	-7	-330		11-1	7-5-0	8-4-0	26.1	44
NYG	+7	+270	44½	7-4-1	9-3-0	4-7-1	17.8	+8.3
Referee: C BLAKEMAN ( 7 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PHI	J HURTS	12	245.0	20	3	108.3	8.2	12.1
NYG	D JONES	12	197.1	11	4	91.2	6.8	10.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PHI	-7	53%	56%	-325	81%	85%	o44.5	46%	59%
NYG	+7	47%	44%	+270	19%	15%	u44.5	54%	41%
Cleveland Browns at Cincinnati Bengals	Sunday, Dec 11
CLE 113
Under: 33
10@23
FINAL	114 CIN
Cover: +9
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CLE	+4	+175		5-7	7-5-0	7-4-1	22.2	49.3
CIN	-4	-200	47	8-4	9-3-0	4-7-1	27	-4.8
Referee: J BOGER ( 3 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CLE	D WATSON	1	131.0	0	1	53.4	6.0	10.9
CIN	J BURROW	12	287.2	25	8	103.7	7.8	11.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CLE	+4	31%	26%	+170	9%	15%	o47	59%	61%
CIN	-4	69%	74%	-200	91%	85%	u47	41%	39%
Jacksonville Jaguars at Tennessee Titans	Sunday, Dec 11
JAC 115
Cover: +17.5
36@22
FINAL	116 TEN
Over: 58
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
JAC	+3.5	+160		4-8	4-8-0	6-6-0	19.4	41.3
TEN	-3.5	-180	41½	7-5	8-4-0	4-8-0	22	-2.6
Referee: C MARTIN ( 5 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
JAC	T LAWRENCE	12	236.2	17	6	92.8	6.8	10.4
TEN	R TANNEHILL	10	211.7	11	4	97.0	8.0	12.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
JAC	+3	48%	27%	+150	13%	17%	o41.5	56%	55%
TEN	-3	52%	73%	-175	87%	83%	u41.5	44%	45%
Houston Texans at Dallas Cowboys	Sunday, Dec 11
HOU 117
Cover: +13
23@27
FINAL	118 DAL
Over: 50
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
HOU	+17	+1100		1-10-1	5-7-0	4-8-0	15.5	44½
DAL	-17	-2200	44½	9-3	8-4-0	6-6-0	29	-13.4
Referee: J HUSSEY ( 5 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
HOU	D MILLS	10	214.4	11	11	78.1	6.5	10.6
DAL	D PRESCOTT	7	223.3	13	7	96.1	7.4	10.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
HOU	+17	40%	48%	+1100	32%	10%	o44.5	55%	70%
DAL	-17	60%	52%	-2100	68%	90%	u44.5	45%	30%
Kansas City Chiefs at Denver Broncos	Sunday, Dec 11
KC 125
Over: 62
34@28
FINAL	126 DEN
Cover: +3
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
KC	-9	-450		9-3	4-7-1	5-7-0	25.4	42.8
DEN	+9	+350	44	3-9	4-8-0	1-11-0	17.3	+8.1
Referee: C WROLSTAD ( 4 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
KC	P MAHOMES	12	317.3	30	8	104.9	8.1	12.4
DEN	R WILSON	11	232.6	8	5	83.5	7.2	11.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
KC	-9	74%	79%	-435	93%	95%	o44	40%	43%
DEN	+9	26%	21%	+350	7%	5%	u44	60%	57%
Carolina Panthers at Seattle Seahawks	Sunday, Dec 11
CAR 121
Cover: +10
30@24
FINAL	122 SEA
Over: 54
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CAR	+4	+175		4-8	6-6-0	4-8-0	20.2	44
SEA	-4	-200	44½	7-5	6-6-0	7-5-0	23.8	-3.6
Referee: B VINOVICH ( 5 ov | 5 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CAR	S DARNOLD	1	164.0	1	0	103.8	8.6	14.9
SEA	G SMITH	12	264.1	22	6	108.7	8.1	11.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CAR	+3.5	47%	24%	+160	15%	11%	o44.5	59%	48%
SEA	-3.5	53%	76%	-190	85%	89%	u44.5	41%	52%
Tampa Bay Buccaneers at San Francisco 49ers	Sunday, Dec 11
TB 123
Over: 42
7@35
FINAL	124 SF
Cover: +24.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TB	+3.5	+170		6-6	3-8-1	2-10-0	16.9	37.8
SF	-3.5	-190	38	8-4	7-5-0	5-7-0	20.9	-4
Referee: B ALLEN ( 7 ov | 3 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TB	T BRADY	12	277.7	16	3	91.6	6.4	9.6
SF	B PURDY	0	69.0	2	2	76.0	6.0	9.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TB	+3.5	53%	51%	+150	57%	48%	o38.5	45%	56%
SF	-3.5	47%	49%	-175	43%	52%	u38.5	55%	44%
Miami Dolphins at Los Angeles Chargers	Sunday, Dec 11
MIA 119
Under: 40
17@23
FINAL	120 LAC
Cover: +9
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIA	-3	-175		8-4	5-6-1	6-6-0	25.8	49
LAC	+3	+155	55	6-6	6-6-0	5-6-1	23.2	+2.6
Referee: S NOVAK ( 4 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIA	T TAGOVAILOA	10	285.9	21	5	112.0	9.0	13.2
LAC	J HERBERT	12	278.3	20	7	92.3	6.6	9.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIA	-3	64%	63%	-175	56%	69%	o54.5	71%	63%
LAC	+3	36%	37%	+150	44%	31%	u54.5	29%	37%
New England Patriots at Arizona Cardinals	Monday, Dec 12
NE 127
Cover: +12
27@13
FINAL	128 ARI
Under: 40
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NE	-2	-135		6-6	6-5-1	5-7-0	23.1	44.2
ARI	+2	+115	44½	4-8	6-6-0	7-4-1	21.1	+2
Referee: S SMITH ( 4 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NE	M JONES	8	218.1	7	7	87.0	7.3	10.7
ARI	K MURRAY	10	235.9	14	7	87.1	6.1	9.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NE	-2.5	50%	49%	-130	45%	44%	o44	60%	53%
ARI	+2.5	50%	51%	+110	55%	56%	u44	40%	47%
San Francisco 49ers at Seattle Seahawks	Thursday, Dec 15
SF 301
Cover: +5
21@13
FINAL	302 SEA
Under: 34
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SF	-3	-175		9-4	8-5-0	6-7-0	22.8	44.4
SEA	+3	+155	43	7-6	6-7-0	8-5-0	21.6	+1.2
Referee: A KEMP ( 8 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SF	B PURDY	1	92.2	4	2	94.2	6.9	10.2
SEA	G SMITH	13	264.1	25	8	106.8	8.0	11.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SF	-3	46%	62%	-175	61%	70%	o42.5	55%	57%
SEA	+3	54%	38%	+150	39%	30%	u42.5	45%	43%
Indianapolis Colts at Minnesota Vikings	Saturday, Dec 17
IND 307
Cover: +0.5
36@39
FINAL	308 MIN
Over: 75
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
IND	+3.5	+170		4-8-1	5-8-0	4-9-0	18.7	43.9
MIN	-3.5	-190	46½	10-3	6-6-1	8-5-0	25.3	-6.6
Referee: T BLAKE ( 6 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
IND	M RYAN	11	261.4	13	13	84.0	6.7	9.9
MIN	K COUSINS	13	258.3	20	9	91.2	6.9	10.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
IND	+3.5	31%	18%	+170	8%	11%	o47	50%	41%
MIN	-3.5	69%	82%	-200	92%	89%	u47	50%	59%
Baltimore Ravens at Cleveland Browns	Saturday, Dec 17
BAL 305
Under: 16
3@13
FINAL	306 CLE
Cover: +7
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BAL	+3	+130		9-4	6-7-0	4-9-0	18.2	40
CLE	-3	-150	39½	5-8	7-6-0	7-5-1	21.8	-3.6
Referee: B ALLEN ( 8 ov | 3 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BAL	T HUNTLEY	1	137.5	0	1	83.2	6.3	7.9
CLE	D WATSON	2	203.5	1	2	70.3	6.4	10.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BAL	+2.5	35%	46%	+135	48%	52%	o38.5	49%	45%
CLE	-2.5	65%	54%	-155	52%	48%	u38.5	51%	55%
Miami Dolphins at Buffalo Bills	Saturday, Dec 17
MIA 309
Cover: +4
29@32
FINAL	310 BUF
Over: 61
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIA	+7	+320		8-5	5-7-1	6-7-0	17.7	45.1
BUF	-7	-380	44½	10-3	6-7-0	3-10-0	27.5	-9.8
Referee: B VINOVICH ( 6 ov | 5 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIA	T TAGOVAILOA	11	273.1	22	5	108.2	8.7	13.3
BUF	J ALLEN	13	273.3	26	11	95.5	7.6	11.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIA	+7	27%	34%	+290	23%	18%	o44.5	62%	51%
BUF	-7	73%	66%	-350	77%	82%	u44.5	38%	49%
Atlanta Falcons at New Orleans Saints	Sunday, Dec 18
ATL 311
Cover: +2
18@21
FINAL	312 NO
Under: 39
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ATL	+5	+190		5-8	7-6-0	6-7-0	19.8	43.1
NO	-5	-220	43½	4-9	5-8-0	6-7-0	23.3	-3.5
Referee: C BLAKEMAN ( 8 ov | 4 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ATL	D RIDDER	0	0.0	0	0	0.0	0.0	0.0
NO	A DALTON	10	225.2	15	7	96.2	7.5	11.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ATL	+5	52%	49%	+190	30%	29%	o43.5	17%	40%
NO	-5	48%	51%	-225	70%	71%	u43.5	83%	60%
Detroit Lions at New York Jets	Sunday, Dec 18
DET 313
Cover: +5
20@17
FINAL	314 NYJ
Under: 37
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DET	+2	+110		6-7	9-3-1	9-4-0	21.3	46.1
NYJ	-2	-130	44	7-6	8-5-0	5-8-0	24.8	-3.4
Referee: C WROLSTAD ( 5 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DET	J GOFF	13	257.9	22	7	97.9	7.6	11.6
NYJ	Z WILSON	7	182.7	4	5	72.6	6.8	12.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DET	+2.5	61%	69%	+110	61%	72%	o44	56%	61%
NYJ	-2.5	39%	31%	-130	39%	28%	u44	44%	39%
Kansas City Chiefs at Houston Texans	Sunday, Dec 18
KC 315
Over: 54
30@24
FINAL	316 HOU
Cover: +8
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
KC	-14	-1200		10-3	4-8-1	6-7-0	29.7	47½
HOU	+14	+750	48½	1-11-1	6-7-0	5-8-0	17.9	+11.8
Referee: C CHEFFERS ( 4 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
KC	P MAHOMES	13	320.0	33	11	103.4	8.1	12.4
HOU	D MILLS	11	210.8	11	12	78.2	6.6	10.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
KC	-14	59%	60%	-1050	93%	95%	o48.5	42%	54%
HOU	+14	41%	40%	+700	7%	5%	u48.5	58%	46%
Philadelphia Eagles at Chicago Bears	Sunday, Dec 18
PHI 317
Under: 45
25@20
FINAL	318 CHI
Cover: +4
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PHI	-9	-420		12-1	8-5-0	9-4-0	26.2	47.9
CHI	+9	+335	48	3-10	4-9-0	9-4-0	21.8	+4.4
Referee: B ROGERS ( 5 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PHI	J HURTS	13	242.9	22	3	108.4	8.1	12.0
CHI	J FIELDS	12	158.0	13	10	85.4	7.5	12.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PHI	-8.5	65%	71%	-390	90%	93%	o48	73%	67%
CHI	+8.5	35%	29%	+320	10%	7%	u48	27%	33%
Pittsburgh Steelers at Carolina Panthers	Sunday, Dec 18
PIT 319
Cover: +11
24@16
FINAL	320 CAR
Over: 40
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PIT	+3	+125		5-8	6-6-1	5-8-0	18.2	40.6
CAR	-3	-145	37½	5-8	7-6-0	5-8-0	22.4	-4.3
Referee: S NOVAK ( 4 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PIT	M TRUBISKY	4	178.8	4	5	78.4	6.8	10.7
CAR	S DARNOLD	2	142.0	2	0	93.6	6.6	11.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PIT	+2.5	43%	43%	+125	51%	47%	o37.5	30%	49%
CAR	-2.5	57%	57%	-145	49%	53%	u37.5	70%	51%
Dallas Cowboys at Jacksonville Jaguars	Sunday, Dec 18
DAL 321
Over: 74
34@40
FINAL	322 JAC
Cover: +10
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DAL	-4	-200		10-3	8-5-0	7-6-0	25.7	47.6
JAC	+4	+175	48	5-8	5-8-0	7-6-0	21.9	+3.8
Referee: S SMITH ( 4 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DAL	D PRESCOTT	8	230.9	14	9	92.2	7.4	11.0
JAC	T LAWRENCE	13	246.3	20	6	95.4	7.0	10.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DAL	-3.5	67%	71%	-205	84%	83%	o48	80%	77%
JAC	+3.5	33%	29%	+175	16%	17%	u48	20%	23%
Arizona Cardinals at Denver Broncos	Sunday, Dec 18
ARI 323
Over: 39
15@24
FINAL	324 DEN
Cover: +7.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ARI	+1.5	+105		4-9	6-7-0	7-5-1	17.4	37
DEN	-1.5	-125	37	3-10	5-8-0	2-11-0	19.5	-2.1
Referee: J BOGER ( 3 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ARI	C MCCOY	2	234.0	1	2	81.7	6.3	9.1
DEN	B RYPIEN	1	120.5	1	2	54.6	4.5	8.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ARI	+2	38%	46%	+105	51%	48%	o37	26%	37%
DEN	-2	62%	54%	-125	49%	52%	u37	74%	63%
New England Patriots at Las Vegas Raiders	Sunday, Dec 18
NE 329
Over: 54
24@30
FINAL	330 LV
Cover: +3.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NE	+2.5	+120		7-6	7-5-1	5-8-0	22.6	44.7
LV	-2.5	-140	45	5-8	6-7-0	7-6-0	22.1	+0.5
Referee: R TORBERT ( 3 ov | 8 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NE	M JONES	9	219.8	7	8	85.7	7.2	10.6
LV	D CARR	13	239.8	20	10	89.4	7.2	11.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NE	+2.5	44%	50%	+115	53%	53%	o45	53%	44%
LV	-2.5	56%	50%	-135	47%	47%	u45	47%	56%
Tennessee Titans at Los Angeles Chargers	Sunday, Dec 18
TEN 325
Under: 31
14@17
FINAL	326 LAC
Cover: -2.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TEN	+3	+130		7-6	8-5-0	5-8-0	22	44.2
LAC	-3	-150	46½	7-6	7-6-0	5-7-1	22.2	-0.2
Referee: L CLARK ( 6 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TEN	R TANNEHILL	11	215.6	13	5	96.3	7.8	12.0
LAC	J HERBERT	13	285.1	21	7	93.2	6.6	9.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TEN	+2.5	34%	36%	+135	25%	31%	o46.5	69%	61%
LAC	-2.5	66%	64%	-155	75%	69%	u46.5	31%	39%
Cincinnati Bengals at Tampa Bay Buccaneers	Sunday, Dec 18
CIN 327
Cover: +8
34@23
FINAL	328 TB
Over: 57
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CIN	-3	-165		9-4	10-3-0	4-8-1	23.4	44.3
TB	+3	+145	48	6-7	3-9-1	3-10-0	20.9	+2.5
Referee: A HILL ( 5 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CIN	J BURROW	13	283.5	27	9	102.4	7.8	11.4
TB	T BRADY	13	275.8	17	5	88.9	6.2	9.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CIN	-3.5	65%	75%	-180	77%	79%	o47.5	66%	68%
TB	+3.5	35%	25%	+155	23%	21%	u47.5	34%	32%
New York Giants at Washington Commanders	Sunday, Dec 18
NYG 303
Cover: +12
20@12
FINAL	304 WAS
Under: 32
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYG	+4	+170		7-5-1	9-4-0	5-7-1	17.8	40.3
WAS	-4	-190	41	7-5-1	7-5-1	4-8-1	22.6	-4.8
Referee: J HUSSEY ( 6 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYG	D JONES	13	194.9	12	4	91.6	6.8	10.3
WAS	T HEINICKE	7	206.3	9	5	86.3	6.8	11.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYG	+4	57%	61%	+175	58%	43%	o40.5	64%	69%
WAS	-4	43%	39%	-205	42%	57%	u40.5	36%	31%
Los Angeles Rams at Green Bay Packers	Monday, Dec 19
LA 331
Under: 36
12@24
FINAL	332 GB
Cover: +4.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LA	+7.5	+320		4-9	4-7-2	5-8-0	15.6	39.2
GB	-7.5	-380	40	5-8	5-8-0	7-6-0	23.7	-8.1
Referee: S HOCHULI ( 5 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LA	B MAYFIELD	7	192.9	7	6	76.8	6.4	10.9
GB	A RODGERS	13	220.3	22	9	92.4	6.8	10.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LA	+7.5	40%	53%	+295	34%	30%	o39.5	71%	63%
GB	-7.5	60%	47%	-360	66%	70%	u39.5	29%	37%
Jacksonville Jaguars at New York Jets	Thursday, Dec 22
JAC 451
Cover: +18.5
19@3
FINAL	452 NYJ
Under: 22
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
JAC	+2.5	+135		6-8	6-8-0	8-6-0	19	39.3
NYJ	-2.5	-155	36	7-7	8-6-0	5-9-0	20.4	-1.4
Referee: B ALLEN ( 8 ov | 4 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
JAC	T LAWRENCE	14	251.4	24	7	96.6	7.0	10.7
NYJ	Z WILSON	8	199.5	6	6	75.3	7.1	13.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
JAC	+2.5	49%	62%	+125	46%	68%	o36.5	54%	60%
NYJ	-2.5	51%	38%	-145	54%	32%	u36.5	46%	40%
New York Giants at Minnesota Vikings	Saturday, Dec 24
NYG 453
Cover: +1
24@27
FINAL	454 MIN
Over: 51
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYG	+4	+190		8-5-1	10-4-0	5-8-1	21.5	47.4
MIN	-4	-220	48	11-3	6-7-1	9-5-0	25.9	-4.5
Referee: A HILL ( 6 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYG	D JONES	14	192.4	12	4	90.5	6.6	10.1
MIN	K COUSINS	14	272.7	24	11	92.0	7.0	10.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYG	+4	29%	42%	+165	34%	24%	o48	74%	53%
MIN	-4	71%	58%	-195	66%	76%	u48	26%	47%
New Orleans Saints at Cleveland Browns	Saturday, Dec 24
NO 455
Cover: +10.5
17@10
FINAL	456 CLE
Under: 27
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NO	+3.5	+160		5-9	5-9-0	6-8-0	18.3	37.9
CLE	-3.5	-180	32	6-8	8-6-0	7-6-1	19.7	-1.4
Referee: B ROGERS ( 5 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NO	A DALTON	11	218.5	17	7	98.1	7.6	11.4
CLE	D WATSON	3	189.3	2	2	76.7	6.2	10.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NO	+2.5	46%	30%	+125	27%	32%	o32.5	48%	72%
CLE	-2.5	54%	70%	-145	73%	68%	u32.5	52%	28%
Detroit Lions at Carolina Panthers	Saturday, Dec 24
DET 457
Over: 60
23@37
FINAL	458 CAR
Cover: +16.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DET	-2.5	-130		7-7	10-3-1	9-5-0	22.1	45.2
CAR	+2.5	+110	43½	5-9	7-7-0	6-8-0	23.1	-1
Referee: S HOCHULI ( 5 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DET	J GOFF	14	257.4	23	7	97.2	7.5	11.5
CAR	S DARNOLD	3	169.7	3	0	98.6	7.7	13.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DET	-3	50%	88%	-150	74%	87%	o43.5	68%	69%
CAR	+3	50%	12%	+130	26%	13%	u43.5	32%	31%
Cincinnati Bengals at New England Patriots	Saturday, Dec 24
CIN 459
Cover: +1
22@18
FINAL	460 NE
Under: 40
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CIN	-3	-155		10-4	11-3-0	5-8-1	22.2	41.1
NE	+3	+135	41½	7-7	7-6-1	6-8-0	18.9	+3.3
Referee: C WROLSTAD ( 5 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CIN	J BURROW	14	277.5	31	10	102.6	7.6	11.1
NE	M JONES	10	210.0	7	8	82.6	6.9	10.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CIN	-3	54%	85%	-170	80%	87%	o41.5	70%	75%
NE	+3	46%	15%	+145	20%	13%	u41.5	30%	25%
Buffalo Bills at Chicago Bears	Saturday, Dec 24
BUF 461
Cover: +14
35@13
FINAL	462 CHI
Over: 48
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BUF	-8	-400		11-3	6-8-0	4-10-0	25.7	41.9
CHI	+8	+330	40½	3-11	5-9-0	9-5-0	16.2	+9.5
Referee: C CHEFFERS ( 5 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BUF	J ALLEN	14	275.5	30	11	97.3	7.6	11.9
CHI	J FIELDS	13	157.5	15	10	88.0	7.5	12.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BUF	-9	19%	44%	-380	93%	93%	o40.5	38%	65%
CHI	+9	81%	56%	+310	7%	7%	u40.5	62%	35%
Seattle Seahawks at Kansas City Chiefs	Saturday, Dec 24
SEA 465
Under: 34
10@24
FINAL	466 KC
Cover: +4
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SEA	+10	+350		7-7	6-8-0	8-6-0	21.4	48.1
KC	-10	-450	50	11-3	4-9-1	7-7-0	26.6	-5.2
Referee: C BLAKEMAN ( 8 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SEA	G SMITH	14	262.2	26	8	105.3	7.8	10.9
KC	P MAHOMES	14	321.1	35	11	105.0	8.1	12.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SEA	+10	50%	66%	+370	14%	9%	o49	54%	57%
KC	-10	50%	34%	-460	86%	91%	u49	46%	43%
Atlanta Falcons at Baltimore Ravens	Saturday, Dec 24
ATL 467
Under: 26
9@17
FINAL	468 BAL
Cover: +1.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ATL	+6.5	+245		5-9	8-6-0	6-8-0	16.1	39.9
BAL	-6.5	-290	35	9-5	6-8-0	4-10-0	23.8	-7.7
Referee: C BLAKEMAN ( 8 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ATL	D RIDDER	1	97.0	0	0	59.3	3.7	7.5
BAL	T HUNTLEY	2	137.7	0	2	72.6	5.6	7.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ATL	+7.5	70%	70%	+285	32%	18%	o37.5	21%	35%
BAL	-7.5	30%	30%	-345	68%	82%	u37.5	79%	65%
Houston Texans at Tennessee Titans	Saturday, Dec 24
HOU 463
Cover: +8
19@14
FINAL	464 TEN
Under: 33
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
HOU	+3	+155		1-12-1	7-7-0	6-8-0	17.2	40.3
TEN	-3	-175	34	7-7	8-6-0	5-9-0	23.2	-6
Referee: S SMITH ( 5 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
HOU	D MILLS	12	203.3	13	12	79.2	6.5	10.6
TEN	M WILLIS	2	29.5	0	1	47.8	4.7	10.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
HOU	+3	26%	31%	+145	22%	22%	o34	38%	52%
TEN	-3	74%	69%	-170	78%	78%	u34	62%	48%
Washington Commanders at San Francisco 49ers	Saturday, Dec 24
WAS 469
Over: 57
20@37
FINAL	470 SF
Cover: +10.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
WAS	+6.5	+250		7-6-1	7-6-1	4-9-1	15.8	38.7
SF	-6.5	-300	37½	10-4	9-5-0	6-8-0	22.9	-7.1
Referee: J BOGER ( 4 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
WAS	T HEINICKE	8	211.6	10	5	87.7	7.0	11.4
SF	B PURDY	2	113.0	6	2	100.6	7.3	10.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
WAS	+6	32%	30%	+235	19%	11%	o37	59%	66%
SF	-6	68%	70%	-300	81%	89%	u37	41%	34%
Philadelphia Eagles at Dallas Cowboys	Saturday, Dec 24
PHI 471
Over: 74
34@40
FINAL	472 DAL
Cover: +2
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PHI	+4	+180		13-1	8-6-0	9-5-0	19.8	45.7
DAL	-4	-210	48	10-4	8-6-0	8-6-0	25.9	-6.1
Referee: A KEMP ( 8 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PHI	G MINSHEW	0	11.3	0	0	79.2	8.5	17.0
DAL	D PRESCOTT	9	233.7	17	11	93.8	7.5	11.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PHI	+3.5	57%	62%	+160	53%	51%	o48	68%	60%
DAL	-3.5	43%	38%	-190	47%	49%	u48	32%	40%
Las Vegas Raiders at Pittsburgh Steelers	Saturday, Dec 24
LV 473
Under: 23
10@13
FINAL	474 PIT
Cover: +1
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LV	+2	+110		6-8	7-7-0	8-6-0	19.4	39½
PIT	-2	-130	37½	6-8	7-6-1	6-8-0	20.2	-0.8
Referee: T BLAKE ( 7 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LV	D CARR	14	239.1	23	11	89.2	7.1	11.6
PIT	K PICKETT	9	179.7	4	8	74.9	6.1	9.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LV	+2.5	32%	42%	+115	49%	60%	o38	54%	49%
PIT	-2.5	68%	58%	-135	51%	40%	u38	46%	51%
Green Bay Packers at Miami Dolphins	Sunday, Dec 25
GB 475
Cover: +9.5
26@20
FINAL	476 MIA
Under: 46
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
GB	+3.5	+155		6-8	6-8-0	7-7-0	20.1	46
MIA	-3.5	-175	49½	8-6	6-7-1	7-7-0	25.9	-5.8
Referee: L CLARK ( 6 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
GB	A RODGERS	14	220.9	23	10	92.3	6.8	10.5
MIA	T TAGOVAILOA	12	269.8	24	5	107.8	8.6	13.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
GB	+3.5	51%	42%	+150	46%	33%	o49.5	55%	62%
MIA	-3.5	49%	58%	-175	54%	67%	u49.5	45%	38%
Denver Broncos at Los Angeles Rams	Sunday, Dec 25
DEN 477
Over: 65
14@51
FINAL	478 LA
Cover: +40
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DEN	-3	-180		4-10	6-8-0	3-11-0	18.6	34.9
LA	+3	+160	36½	4-10	4-8-2	5-9-0	16.3	+2.3
Referee: R TORBERT ( 4 ov | 8 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DEN	R WILSON	12	233.8	11	6	85.1	7.1	11.8
LA	B MAYFIELD	8	183.8	8	7	76.1	6.3	10.8
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DEN	-3	64%	52%	-180	50%	47%	o36	57%	48%
LA	+3	36%	48%	+155	50%	53%	u36	43%	52%
Tampa Bay Buccaneers at Arizona Cardinals	Sunday, Dec 25
TB 479
Under: 35
19@16
FINAL	480 ARI
Cover: +5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TB	-8	-380		6-8	3-10-1	4-10-0	23.8	41
ARI	+8	+320	42	4-10	6-8-0	8-5-1	17.2	+6.6
Referee: J HUSSEY ( 6 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TB	T BRADY	14	278.4	20	7	89.1	6.3	9.5
ARI	T MCSORLEY	0	55.3	0	3	29.5	5.7	11.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TB	-6.5	90%	74%	-265	92%	90%	o41	47%	46%
ARI	+6.5	10%	26%	+225	8%	10%	u41	53%	54%
Los Angeles Chargers at Indianapolis Colts	Monday, Dec 26
LAC 481
Cover: +13.5
20@3
FINAL	482 IND
Under: 23
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LAC	-3.5	-185		8-6	8-6-0	5-8-1	24.9	45.2
IND	+3.5	+165	44½	4-9-1	6-8-0	5-9-0	20.3	+4.6
Referee: C MARTIN ( 6 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LAC	J HERBERT	14	287.1	21	9	91.5	6.7	9.9
IND	N FOLES	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LAC	-3.5	70%	76%	-200	79%	80%	o44.5	65%	60%
IND	+3.5	30%	24%	+170	21%	20%	u44.5	35%	40%
Dallas Cowboys at Tennessee Titans	Thursday, Dec 29
DAL 101
Cover: +0.5
27@13
FINAL	102 TEN
Under: 40
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DAL	-13.5	-900		11-4	9-6-0	9-6-0	27.3	40.9
TEN	+13.5	+600	40½	7-8	8-7-0	5-10-0	13.5	+13.8
Referee: S HOCHULI ( 6 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DAL	D PRESCOTT	10	245.0	20	12	97.2	7.8	11.2
TEN	J DOBBS	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DAL	-13.5	58%	53%	-850	85%	80%	o40.5	62%	69%
TEN	+13.5	42%	47%	+600	15%	20%	u40.5	38%	31%
Carolina Panthers at Tampa Bay Buccaneers	Sunday, Jan 1
CAR 103
Over: 54
24@30
FINAL	104 TB
Cover: +2.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CAR	+3.5	+175		6-9	8-7-0	7-8-0	18.3	38.8
TB	-3.5	-200	40½	7-8	3-11-1	4-11-0	20.5	-2.2
Referee: B ROGERS ( 5 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CAR	S DARNOLD	4	189.8	4	0	104.3	8.6	14.1
TB	T BRADY	15	278.5	21	9	87.9	6.2	9.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CAR	+3.5	51%	50%	+170	26%	30%	o40.5	60%	55%
TB	-3.5	49%	50%	-200	74%	70%	u40.5	40%	45%
Cleveland Browns at Washington Commanders	Sunday, Jan 1
CLE 105
Cover: +15.5
24@10
FINAL	106 WAS
Under: 34
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CLE	+1.5	+102		6-9	8-7-0	7-7-1	22.1	43.7
WAS	-1.5	-122	41	7-7-1	7-7-1	5-9-1	21.6	+0.4
Referee: B VINOVICH ( 7 ov | 5 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CLE	D WATSON	4	175.8	2	3	69.3	5.7	9.9
WAS	C WENTZ	6	230.3	11	6	86.3	6.5	10.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CLE	+1.5	48%	44%	+100	49%	47%	o41.5	49%	48%
WAS	-1.5	52%	56%	-120	51%	53%	u41.5	51%	52%
New Orleans Saints at Philadelphia Eagles	Sunday, Jan 1
NO 109
Cover: +15
20@10
FINAL	110 PHI
Under: 30
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NO	+5	+190		6-9	6-9-0	6-9-0	17.5	43
PHI	-5	-220	42	13-2	8-7-0	10-5-0	25.5	-8
Referee: J BOGER ( 5 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NO	A DALTON	12	207.9	17	8	95.7	7.5	11.4
PHI	G MINSHEW	1	97.3	2	2	84.4	8.8	15.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NO	+5	29%	22%	+190	8%	9%	o42	71%	76%
PHI	-5	71%	78%	-225	92%	91%	u42	29%	24%
Arizona Cardinals at Atlanta Falcons	Sunday, Jan 1
ARI 111
Cover: +5.5
19@20
FINAL	112 ATL
Under: 39
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ARI	+6.5	+250		4-11	7-8-0	8-6-1	18.1	40
ATL	-6.5	-300	40	5-10	8-7-0	6-9-0	21.9	-3.8
Referee: A KEMP ( 9 ov | 5 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ARI	D BLOUGH	0	0.0	0	0	0.0	0.0	0.0
ATL	D RIDDER	2	157.5	0	0	73.8	5.3	9.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ARI	+6.5	56%	52%	+245	44%	29%	o40.5	20%	36%
ATL	-6.5	44%	48%	-295	56%	71%	u40.5	80%	64%
Jacksonville Jaguars at Houston Texans	Sunday, Jan 1
JAC 113
Cover: +24.5
31@3
FINAL	114 HOU
Under: 34
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
JAC	-3.5	-190		7-8	7-8-0	8-7-0	23	42.9
HOU	+3.5	+170	43½	2-12-1	8-7-0	6-9-0	19.9	+3.1
Referee: S NOVAK ( 5 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
JAC	T LAWRENCE	15	249.9	24	7	96.0	7.1	10.7
HOU	D MILLS	13	201.4	14	13	79.0	6.5	10.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
JAC	-3.5	60%	77%	-180	89%	87%	o44	66%	62%
HOU	+3.5	40%	23%	+155	11%	13%	u44	34%	38%
Chicago Bears at Detroit Lions	Sunday, Jan 1
CHI 115
Under: 51
10@41
FINAL	116 DET
Cover: +26.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CHI	+4.5	+180		3-12	5-10-0	10-5-0	21.2	48.8
DET	-4.5	-210	52½	7-8	10-4-1	10-5-0	27.7	-6.5
Referee: A HILL ( 7 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CHI	J FIELDS	14	154.8	16	10	88.3	7.3	11.7
DET	J GOFF	15	263.9	26	7	98.3	7.6	11.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CHI	+5	48%	45%	+185	23%	20%	o52.5	69%	57%
DET	-5	52%	55%	-215	77%	80%	u52.5	31%	43%
Miami Dolphins at New England Patriots	Sunday, Jan 1
MIA 117
Cover: +1
21@23
FINAL	118 NE
Over: 44
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIA	+3	+135		8-7	6-8-1	7-8-0	19.6	41.8
NE	-3	-155	41½	7-8	7-7-1	6-9-0	22.2	-2.6
Referee: B ALLEN ( 8 ov | 5 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIA	T BRIDGEWATER	1	130.5	3	3	85.6	8.7	14.1
NE	M JONES	11	212.5	9	8	84.6	6.9	10.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIA	+3	57%	52%	+135	59%	61%	o41.5	31%	47%
NE	-3	43%	48%	-155	41%	39%	u41.5	69%	53%
Denver Broncos at Kansas City Chiefs	Sunday, Jan 1
DEN 119
Cover: +9.5
24@27
FINAL	120 KC
Over: 51
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DEN	+12.5	+600		4-11	6-9-0	4-11-0	15.4	44
KC	-12.5	-900	45½	12-3	5-9-1	7-8-0	28.7	-13.3
Referee: T BLAKE ( 7 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DEN	R WILSON	13	232.2	12	9	82.6	7.2	11.9
KC	P MAHOMES	15	314.7	37	11	105.1	8.1	12.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DEN	+12.5	34%	32%	+540	9%	6%	o46	51%	57%
KC	-12.5	66%	68%	-740	91%	94%	u46	49%	43%
Indianapolis Colts at New York Giants	Sunday, Jan 1
IND 121
Over: 48
10@38
FINAL	122 NYG
Cover: +22.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
IND	+5.5	+200		4-10-1	6-9-0	5-10-0	16.3	40.6
NYG	-5.5	-240	39	8-6-1	11-4-0	6-8-1	24.3	-7.9
Referee: C WROLSTAD ( 5 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
IND	N FOLES	1	143.0	0	3	31.9	4.9	8.4
NYG	D JONES	15	201.9	13	5	90.7	6.8	10.2
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
IND	+5.5	25%	21%	+200	7%	10%	o38.5	25%	54%
NYG	-5.5	75%	79%	-240	93%	90%	u38.5	75%	46%
New York Jets at Seattle Seahawks	Sunday, Jan 1
NYJ 123
Under: 29
6@23
FINAL	124 SEA
Cover: +18
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYJ	-1	-120		7-8	8-7-0	5-10-0	21.8	43.4
SEA	+1	EVEN	43½	7-8	6-9-0	8-7-0	21.7	+0.1
Referee: R TORBERT ( 5 ov | 8 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYJ	M WHITE	3	317.3	3	2	85.8	7.4	11.9
SEA	G SMITH	15	259.1	27	9	102.9	7.6	10.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYJ	-1.5	63%	52%	-125	49%	36%	o43	54%	48%
SEA	+1.5	37%	48%	+105	51%	64%	u43	46%	52%
San Francisco 49ers at Las Vegas Raiders	Sunday, Jan 1
SF 125
Over: 71
37@34
FINAL	126 LV
Cover: +6.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
SF	-9.5	-475		11-4	10-5-0	7-8-0	25.9	44.8
LV	+9.5	+375	41	6-9	7-8-0	8-7-0	18.8	+7.1
Referee: C MARTIN ( 6 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
SF	B PURDY	3	130.3	8	3	103.2	7.9	11.8
LV	J STIDHAM	0	72.0	0	0	76.4	5.5	9.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
SF	-10	75%	80%	-490	90%	94%	o41	58%	65%
LV	+10	25%	20%	+390	10%	6%	u41	42%	35%
Minnesota Vikings at Green Bay Packers	Sunday, Jan 1
MIN 127
Over: 58
17@41
FINAL	128 GB
Cover: +20.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIN	+3.5	+175		12-3	6-8-1	10-5-0	21	45.2
GB	-3.5	-200	48	7-8	7-8-0	7-8-0	24.2	-3.2
Referee: C CHEFFERS ( 6 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIN	K COUSINS	15	274.5	27	11	93.3	7.0	10.6
GB	A RODGERS	15	222.1	24	11	91.3	6.8	10.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIN	+3	45%	63%	+150	57%	60%	o47.5	78%	74%
GB	-3	55%	37%	-175	43%	40%	u47.5	22%	26%
Los Angeles Rams at Los Angeles Chargers	Sunday, Jan 1
LA 129
Cover +2.5
10@31
FINAL	130 LAC
Cover: +14.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LA	+6.5	+230		5-10	5-8-2	6-9-0	17.3	40.9
LAC	-6.5	-270	41	9-6	9-6-0	5-9-1	23.6	-6.3
Referee: C BLAKEMAN ( 8 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LA	B MAYFIELD	9	188.4	10	7	81.5	6.5	10.6
LAC	J HERBERT	15	283.6	21	10	91.2	6.7	9.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LA	+7	36%	40%	+240	16%	15%	o41.5	58%	83%
LAC	-7	64%	60%	-285	84%	85%	u41.5	42%	17%
Pittsburgh Steelers at Baltimore Ravens	Sunday, Jan 1
PIT 107
Cover: +4.5
16@13
FINAL	108 BAL
Under: 29
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
PIT	+1.5	+110		7-8	8-6-1	6-9-0	16.5	38.1
BAL	-1.5	-130	35	10-5	7-8-0	4-11-0	21.7	-5.2
Referee: L CLARK ( 6 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
PIT	K PICKETT	10	185.6	5	9	75.7	6.1	9.4
BAL	T HUNTLEY	3	132.0	1	2	76.6	5.8	8.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
PIT	+1	49%	50%	+100	52%	56%	o35.5	59%	52%
BAL	-1	51%	50%	-120	48%	44%	u35.5	41%	48%
Kansas City Chiefs at Las Vegas Raiders	Saturday, Jan 7
KC 465
Cover: +9.5
31@13
FINAL	466 LV
Under: 44
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
KC	-8.5	-400		13-3	5-10-1	8-8-0	28.7	49.2
LV	+8.5	+330	52	6-10	8-8-0	9-7-0	20.5	+8.2
Referee: S NOVAK ( 5 ov | 10 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
KC	P MAHOMES	16	315.5	40	12	105.2	8.1	12.1
LV	J STIDHAM	1	218.5	3	2	99.3	9.3	14.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
KC	-8.5	49%	49%	-425	81%	84%	o52	62%	68%
LV	+8.5	51%	51%	+340	19%	16%	u52	38%	32%
Tennessee Titans at Jacksonville Jaguars	Saturday, Jan 7
TEN 457
Cover: +2
16@20
FINAL	458 JAC
Under: 36
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TEN	+6	+210		7-9	8-8-0	5-11-0	17.3	39.9
JAC	-6	-250	39	8-8	8-8-0	8-8-0	22.6	-5.3
Referee: B VINOVICH ( 7 ov | 6 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TEN	J DOBBS	1	232.0	1	1	67.5	6.0	11.6
JAC	T LAWRENCE	16	243.8	24	8	95.4	7.1	10.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TEN	+5.5	43%	41%	+225	37%	27%	o39.5	71%	70%
JAC	-5.5	57%	59%	-265	63%	73%	u39.5	29%	30%
New York Jets at Miami Dolphins	Sunday, Jan 8
NYJ 455
Under: 17
6@11
FINAL	456 MIA
Cover: +1.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYJ	+3.5	+190		7-9	8-8-0	5-11-0	19.6	39.2
MIA	-3.5	-220	37	8-8	7-8-1	8-8-0	19.7	-0.1
Referee: J HUSSEY ( 6 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYJ	J FLACCO	3	225.5	5	3	77.0	5.7	9.8
MIA	S THOMPSON	1	63.7	1	3	56.3	5.2	9.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYJ	+4	46%	44%	+170	47%	43%	o37.5	38%	55%
MIA	-4	54%	56%	-200	53%	57%	u37.5	62%	45%
Cleveland Browns at Pittsburgh Steelers	Sunday, Jan 8
CLE 461
Over: 42
14@28
FINAL	462 PIT
Cover: +11.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CLE	+2.5	+130		7-9	9-7-0	7-8-1	20.4	40
PIT	-2.5	-150	39½	8-8	9-6-1	6-10-0	19.6	+0.8
Referee: C BLAKEMAN ( 8 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CLE	D WATSON	5	174.4	5	3	78.1	6.2	10.9
PIT	K PICKETT	11	184.1	6	9	76.5	6.1	9.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CLE	+2.5	37%	38%	+130	34%	38%	o40	24%	29%
PIT	-2.5	63%	62%	-150	66%	62%	u40	76%	71%
Houston Texans at Indianapolis Colts	Sunday, Jan 8
HOU 463
Cover: +4
32@31
FINAL	464 IND
Over: 63
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
HOU	+3	+125		2-13-1	8-8-0	6-10-0	18.2	38.9
IND	-3	-145	37½	4-11-1	6-10-0	6-10-0	20.8	-2.6
Referee: J BOGER ( 5 ov | 10 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
HOU	D MILLS	14	201.4	14	13	78.1	6.4	10.4
IND	S EHLINGER	2	121.3	1	1	75.6	5.5	8.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
HOU	+3	39%	46%	+130	39%	45%	o37.5	46%	41%
IND	-3	61%	54%	-150	61%	55%	u37.5	54%	59%
Tampa Bay Buccaneers at Atlanta Falcons	Sunday, Jan 8
TB 471
Over: 47
17@30
FINAL	472 ATL
Cover: +7.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
TB	+5.5	+200		8-8	4-11-1	5-11-0	16.3	39.8
ATL	-5.5	-240	40½	6-10	8-8-0	6-10-0	23.5	-7.2
Referee: L CLARK ( 6 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
TB	T BRADY	16	288.1	24	9	90.4	6.4	9.7
ATL	D RIDDER	3	161.3	0	0	78.8	5.7	9.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
TB	+6	62%	76%	+205	68%	76%	o40.5	41%	45%
ATL	-6	38%	24%	-245	32%	24%	u40.5	59%	55%
Carolina Panthers at New Orleans Saints	Sunday, Jan 8
CAR 475
Cover: +6.5
10@7
FINAL	476 NO
Under: 17
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
CAR	+3.5	+160		6-10	8-8-0	8-8-0	18.8	41.1
NO	-3.5	-180	42	7-9	7-9-0	6-10-0	22.3	-3.5
Referee: A KEMP ( 9 ov | 6 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
CAR	S DARNOLD	5	220.0	7	1	105.4	8.8	14.3
NO	A DALTON	13	207.6	17	9	95.3	7.7	11.4
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
CAR	+3.5	31%	55%	+160	49%	42%	o41.5	61%	52%
NO	-3.5	69%	45%	-190	51%	58%	u41.5	39%	48%
New England Patriots at Buffalo Bills	Sunday, Jan 8
NE 477
Over: 58
23@35
FINAL	478 BUF
Cover: +3.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NE	+8.5	+340		8-8	7-8-1	7-9-0	16.9	43
BUF	-8.5	-440	44	12-3	7-8-0	5-10-0	26.1	-9.2
Referee: C MARTIN ( 7 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NE	M JONES	12	211.8	11	8	85.8	6.9	10.5
BUF	J ALLEN	15	268.6	32	13	96.1	7.5	11.9
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NE	+8	34%	33%	+320	13%	11%	o44	74%	67%
BUF	-8	66%	67%	-390	87%	89%	u44	26%	33%
Baltimore Ravens at Cincinnati Bengals	Sunday, Jan 8
BAL 479
Cover: +0.5
16@27
FINAL	480 CIN
Over: 43
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
BAL	+11.5	+475		10-6	7-9-0	4-12-0	17.3	40.6
CIN	-11.5	-650	39	11-4	12-3-0	5-9-1	23.3	-6
Referee: R TORBERT ( 5 ov | 9 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
BAL	A BROWN	0	16.0	0	0	65.4	3.2	5.3
CIN	J BURROW	15	284.0	34	12	102.3	7.6	11.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
BAL	+11.5	30%	38%	+470	9%	10%	o39.5	52%	65%
CIN	-11.5	70%	62%	-625	91%	90%	u39.5	48%	35%
Minnesota Vikings at Chicago Bears	Sunday, Jan 8
MIN 481
Cover: +9.5
29@13
FINAL	482 CHI
Under: 42
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
MIN	-6.5	-290		12-4	6-9-1	11-5-0	25.6	46½
CHI	+6.5	+245	42½	3-13	5-11-0	10-6-0	21	+4.6
Referee: B ALLEN ( 9 ov | 5 un | 1 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
MIN	K COUSINS	16	270.1	28	14	91.1	6.9	10.6
CHI	N PETERMAN	0	12.5	0	1	21.5	4.2	8.3
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
MIN	-6.5	83%	80%	-285	90%	90%	o43	48%	55%
CHI	+6.5	17%	20%	+240	10%	10%	u43	52%	45%
Los Angeles Rams at Seattle Seahawks	Sunday, Jan 8
LA 451
Cover: +2
16@19
FINAL	452 SEA
Under: 35
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LA	+5	+200		5-11	5-9-2	6-10-0	16.8	41.1
SEA	-5	-240	42½	8-8	7-9-0	8-8-0	24.2	-7.4
Referee: C WROLSTAD ( 6 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LA	B MAYFIELD	10	183.3	10	7	81.3	6.5	10.7
SEA	G SMITH	16	254.3	29	9	102.9	7.5	10.7
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LA	+4.5	55%	48%	+195	35%	28%	o42.5	75%	62%
SEA	-4.5	45%	52%	-230	65%	72%	u42.5	25%	38%
New York Giants at Philadelphia Eagles	Sunday, Jan 8
NYG 453
Cover: +11
16@22
FINAL	454 PHI
Under: 38
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
NYG	+17	+950		9-6-1	12-4-0	7-8-1	14.1	42.1
PHI	-17	-1800	43	13-3	8-8-0	10-6-0	28	-13.9
Referee: C CHEFFERS ( 7 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
NYG	D WEBB	0	0.0	0	0	0.0	0.0	0.0
PHI	J HURTS	14	248.0	22	5	104.6	8.2	12.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
NYG	+16.5	73%	81%	+900	48%	26%	o42.5	66%	66%
PHI	-16.5	27%	19%	-1500	52%	74%	u42.5	34%	34%
Arizona Cardinals at San Francisco 49ers	Sunday, Jan 8
ARI 467
Over: 51
13@38
FINAL	468 SF
Cover: +11
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
ARI	+14	+750		4-12	8-8-0	8-7-1	14.3	41.2
SF	-14	-1200	40	12-4	10-6-0	8-8-0	26.8	-12.5
Referee: A HILL ( 7 ov | 8 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
ARI	D BLOUGH	1	222.0	1	0	83.5	5.6	9.3
SF	B PURDY	4	149.5	10	4	101.4	8.0	12.1
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
ARI	+14	62%	48%	+700	23%	8%	o40	37%	64%
SF	-14	38%	52%	-1050	77%	92%	u40	63%	36%
Los Angeles Chargers at Denver Broncos	Sunday, Jan 8
LAC 469
Cover: +3.5
28@31
FINAL	470 DEN
Over: 59
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
LAC	+6.5	+240		10-6	10-6-0	5-10-1	21.6	40½
DEN	-6.5	-280	39½	4-12	7-9-0	5-11-0	19	+2.6
Referee: S HOCHULI ( 6 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
LAC	J HERBERT	16	279.1	23	10	92.4	6.8	9.9
DEN	R WILSON	14	231.5	13	10	82.5	7.1	11.6
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
LAC	+6	46%	72%	+220	55%	73%	o39	49%	51%
DEN	-6	54%	28%	-260	45%	27%	u39	51%	49%
Dallas Cowboys at Washington Commanders	Sunday, Jan 8
DAL 473
Under: 32
6@26
FINAL	474 WAS
Cover: +27.5
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DAL	-7.5	-360		12-4	10-6-0	9-7-0	23.5	41.9
WAS	+7.5	+300	41	7-8-1	7-8-1	5-10-1	18.3	+5.2
Referee: T BLAKE ( 8 ov | 7 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DAL	D PRESCOTT	11	248.4	22	14	95.8	7.7	11.1
WAS	S HOWELL	0	0.0	0	0	0.0	0.0	0.0
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DAL	-7	70%	74%	-305	88%	91%	o41	89%	80%
WAS	+7	30%	26%	+255	12%	9%	u41	11%	20%
Detroit Lions at Green Bay Packers	Sunday, Jan 8
DET 459
Cover: +8.5
20@16
FINAL	460 GB
Under: 36
Matchup Analysis
Team Trends
Head-to-Head
Betting Market Insights
News
Team	Line	ML	OU	REC	ATS	OU	EST Score	EST Line
DET	+4.5	+210		8-8	11-4-1	10-6-0	22.2	48.8
GB	-4.5	-250	49	8-8	8-8-0	8-8-0	26.6	-4.4
Referee: B ROGERS ( 6 ov | 9 un | 0 p )
 	STARTING QB	GS	PY	TD	INT	RTG	PYPA	PYPC
DET	J GOFF	16	263.4	29	7	100.1	7.6	11.7
GB	A RODGERS	16	218.1	25	11	91.5	6.8	10.5
	LINE	HANDLE	BETS	ML	HANDLE	BETS	OU	HANDLE	BETS
DET	+5.5	35%	44%	+200	30%	33%	o49	46%	59%
GB	-5.5	65%	56%	-240	70%	67%	u49	54%	41%
"""


# In[51]:


import sys
import sklearn
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential 
from keras import Input
from keras.layers import Dense
from keras import metrics
import numpy as np
import os
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib import rcParams

data = np.matrix([])

#Variables stored from vsin.com data
spreads = []
spread_handles = []
spread_bets = []
mls = []
ml_handles = []
ml_bets = []
ous = []
ou_handles = []
ou_bets = []

#read through doc and save features
c = 1
phrase = ""
for char in data_text:
    if char != "\n":
        phrase += char
    else:
        if c == 20:
            #values
            spread = ""
            spread_handle = ""
            spread_bet = ""
            ml = ""
            ml_handle = ""
            ml_bet = ""
            ou = ""
            ou_handle = ""
            ou_bet = ""
            #values end
            
            last_space = False
            value = ""
            word_num = 0
            for char in phrase:
                if char.isspace():
                    if last_space == False:
                        if word_num == 1:
                            spread = value
                        elif word_num == 2:
                            spread_handle = value
                        elif word_num == 3:
                            spread_bet = value
                        elif word_num == 4:
                            ml = value
                        elif word_num == 5:
                            ml_handle = value
                        elif word_num == 6:
                            ml_bet = value
                        elif word_num == 7:
                            ou = value
                        elif word_num == 8:
                            ou_handle = value
                        last_space = True
                        value = ""
                        word_num += 1
                else:
                    last_space = False
                    value += char
                    
            ou_bet = value
            
            print(phrase)
                
            ml_float = float(0)
            
            if ml[0] == "-":
                ml_float = 1 + 100/(float(ml)*-1)
            else:
                ml_float = 1 + float(ml)/100
                
            spreads.append(float(spread))
            spread_handles.append(float(spread_handle[:-1])/100)
            spread_bets.append(float(spread_bet[:-1])/100)
            mls.append(ml_float)
            ml_handles.append(float(ml_handle[:-1])/100)
            ml_bets.append(float(ml_bet[:-1])/100)
            ous.append(float(ou[1:]))
            ou_handles.append(abs(float(ou_handle[:-1])/100-.5))
            ou_bets.append(abs(float(ou_bet[:-1])/100-.5))

            c=0
        else:
            c+= 1
        phrase = ""
        
#Read through data and store additional features  
c = 0
phrase = ""
for char in data_text:
    if char != "\n":
        phrase += char
    else:
        if c == 20:
            #values
            spread = ""
            spread_handle = ""
            spread_bet = ""
            ml = ""
            ml_handle = ""
            ml_bet = ""
            ou = ""
            ou_handle = ""
            ou_bet = ""
            #values end
            
            last_space = False
            value = ""
            word_num = 0
            for char in phrase:
                if char.isspace():
                    if last_space == False:
                        if word_num == 1:
                            spread = value
                        elif word_num == 2:
                            spread_handle = value
                        elif word_num == 3:
                            spread_bet = value
                        elif word_num == 4:
                            ml = value
                        elif word_num == 5:
                            ml_handle = value
                        elif word_num == 6:
                            ml_bet = value
                        elif word_num == 7:
                            ou = value
                        elif word_num == 8:
                            ou_handle = value
                        last_space = True
                        value = ""
                        word_num += 1
                else:
                    last_space = False
                    value += char
            
            print(phrase)
                
            ou_bet = value
            
            ml_float = float(0)
            
            if ml[0] == "-":
                ml_float = 1 + 100/(float(ml)*-1)
            else:
                ml_float = 1 + float(ml)/100
                
            spreads.append(float(spread))
            spread_handles.append(float(spread_handle[:-1])/100)
            spread_bets.append(float(spread_bet[:-1])/100)
            mls.append(ml_float)
            ml_handles.append(float(ml_handle[:-1])/100)
            ml_bets.append(float(ml_bet[:-1])/100)
            ous.append(float(ou[1:]))
            ou_handles.append(abs(float(ou_handle[:-1])/100-.5))
            ou_bets.append(abs(float(ou_bet[:-1])/100-.5))

            c = 0
        else:
            c += 1
        phrase = ""
        
c = 17
phrase = ""

#Read through again to save weights   
weights = []
for char in data_text:
    if char != "\n":
        phrase += char
    else:
        if c == 20:
            last_space = False
            value = ""
            
            home_score = 0
            away_score = 0
            
            cur = ""
            
            for char in phrase:
                if char == "@":
                    home_score = float(cur)
                    cur = ""
                else:
                    cur += char
            
            away_score = float(cur)
            
            outcome = 0
            
            if home_score > away_score:
                outcome = 1
                
            weights.append(float(outcome))

            c=0
        else:
            c+= 1
        phrase = ""

opposite_weights = []
for weight in weights:
    if weight == float(0):
        opposite_weights.append(float(1))
    else:
        opposite_weights.append(float(0))   
        
for weight in opposite_weights:
    weights.append(weight)

#Define dictionary
data_dict = {'spread': spreads, 'spread_handle': spread_handles, 'ml': mls, 'ml_handle': ml_handles, 'ou_handle': ou_handles, 'weights': weights}

df = pd.DataFrame(data_dict)
df


# In[85]:


from keras.regularizers import L1L2

X = df[['spread', 'spread_handle', 'ml', 'ml_handle', 'ou_handle']]
y = df['weights']

#Obtain test and train data from dictionary
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.1, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


#Logistic Regression
log_reg = Sequential()
log_reg.add(Dense(1,  # output dim is 2, one score per each class
                activation='sigmoid',
                kernel_regularizer=L1L2(l1=0.0, l2=0.01),
                input_dim=5))  # input dimension = number of features your data has
log_reg.compile(optimizer='sgd',
              loss='binary_crossentropy',
              metrics=['binary_accuracy'])

log_reg_history = log_reg.fit(X_train, y_train, shuffle=True, epochs=3)

eval = log_reg.evaluate(x=X_test, y=y_test)
eval


# In[155]:


tf.random.set_seed(42)


neuralnetwork = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

neuralnetwork.compile(
    loss=tf.keras.losses.binary_crossentropy,
    optimizer=tf.keras.optimizers.Adam(lr=0.03),
    metrics=[
        tf.keras.metrics.BinaryAccuracy(name='accuracy'),
        tf.keras.metrics.Precision(name='precision'),
        tf.keras.metrics.Recall(name='recall')
    ]
)

neuralnetwork_history = neuralnetwork.fit(X_train_scaled, y_train, epochs=100)


# In[153]:


#Test set of games to predict, in this case the NFL wild card games

game_to_predict = np.array([[9.5, .27, 5, .15, 0], #seahawks 
                            [-9.5, .73, 100/500+1, .85, 0], #49ers 
                            
                            [-2.5, .59, 100/140+1, .38, .02], #chargers 
                            [2.5, .41, 2.2, .62, .02], #jags 

                            [13.5, .12, 7.25, .14, .11], #dolphins 
                            [-13.5, .88, 100/900+1, .86, .11], #bills
                            
                            [3, .53, 2.35, .52, .01], #giants 
                            [-3, .47, 100/155+1, .48, .01], #vikings 
                            
                            [8.5, .36, 4.5, .1, .14], #ravens 
                            [-8.5, .74, 100/435+1, .9, .14], #bengals 
                            
                            [-2.5, .46, 100/140+1, .34, .05], #cowboys 
                            [2.5, .54, 2.2, .66, .05]]) #buccaneers 


#Scale games with standard scaler
games_to_predict_scaled = scaler.transform(game_to_predict)


# In[156]:


#Form predictions for neural network
neuralnetwork_predictions = neuralnetwork.predict(games_to_predict_scaled)

neuralnetwork_prediction_classes = [
    1 if prob > 0.5 else 0 for prob in np.ravel(neuralnetwork_predictions)
]

print(neuralnetwork_prediction_classes)

rcParams['figure.figsize'] = (18, 8)
rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False

plt.plot(
    np.arange(1, 101), 
    neuralnetwork_history.history['loss'], label='Loss'
)
plt.plot(
    np.arange(1, 101), 
    neuralnetwork_history.history['accuracy'], label='Accuracy'
)

plt.plot(
    np.arange(1, 101), 
    neuralnetwork_history.history['precision'], label='Precision'
)
plt.plot(
    np.arange(1, 101), 
    neuralnetwork_history.history['recall'], label='Recall'
)
plt.title('Evaluation metrics', size=20)
plt.xlabel('Epoch', size=14)
plt.legend();


#Evaluating mean accuracy for test and train data
neuralnetwork_predictions_train = neuralnetwork.predict(X_train_scaled)

neuralnetwork_predictions_test = neuralnetwork.predict(X_test_scaled)

neuralnetwork_prediction_classes_train = [
    1 if prob > 0.5 else 0 for prob in np.ravel(neuralnetwork_predictions_train)
]

neuralnetwork_prediction_classes_test = [
    1 if prob > 0.5 else 0 for prob in np.ravel(neuralnetwork_predictions_test)
]

print(1-sklearn.metrics.accuracy_score(y_test,neuralnetwork_prediction_classes_test))
print (1-sklearn.metrics.accuracy_score(y_train,neuralnetwork_prediction_classes_train))


# In[86]:


#Form predictions for log reg
log_reg_game_predictions = log_reg.predict(games_to_predict_scaled)

log_reg_prediction_classes = [
    1 if prob > 0.5 else 0 for prob in np.ravel(log_reg_game_predictions)
]

#print predictions
print(log_reg_prediction_classes)

#plot loss vs accuracy
rcParams['figure.figsize'] = (18, 8)
rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False

plt.plot(
    np.arange(1, 4), 
    log_reg_history.history['loss'], label='Loss'
)
plt.plot(
    np.arange(1,4), 
    log_reg_history.history['binary_accuracy'], label='Accuracy'
)


plt.title('Evaluation metrics', size=20)
plt.xlabel('Epoch', size=14)
plt.legend();


# In[ ]:





# In[ ]:




