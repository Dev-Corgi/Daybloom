# Capture audit 01–21 (visual inspection)

검사 기준: `docs/Stoic/flows/<flow>/screenshots/screen-NN.webp`. 각 이미지 145장을 흐름별 contact sheet로 모두 시각 확인했다. 화면 번호는 각 폴더의 `screen-NN.webp`를 가리킨다. 원본 iOS viewport는 393×852이고 하단 검정 Mobbin 띠/워터마크는 앱 UI가 아니다. 이 문서의 `선택`은 브리프의 이번 구현 범위, `참고`는 디자인 시스템 증거만 뜻한다. 아래 수치 토큰은 캡처에서 측정하지 않았으므로 확정하지 않는다.

## 검사 인벤토리

| 흐름 | 장수 | 범위 | 화면 상태/특징 |
|---|---:|---|---|
| 01 Onboarding | 13 | 선택 01–12; 13 제외 | intro, 다중 선택, 나이 단일 선택, 알림 토글·시간 선택·OS 권한, 준비 완료·AI 카드; 13은 구독 |
| 02 Subscribing to premium | 13 | 참고 | paywall, 요금 선택·처리·확인, 구독 뒤 Today |
| 03 Premium AI features | 4 | 참고 | 기능 설명의 행·섹션 분할 |
| 04 Today | 6 | 선택; 범위 밖 카드/행동 제외 | 시간대·날짜·작성 전후 카드, Quote, 영감 카드 |
| 05 Morning reflection | 18 | 선택 01–10·16–18; AI 11–15 제외 | intro, 슬라이더, 초점 선택, 글쓰기, 완료·streak |
| 06 Recording voice note | 6 | 참고 | 첨부 메뉴, 녹음 패널과 전사 토글 |
| 07 Drawing a sketch | 4 | 참고 | 편집기 첨부 메뉴, 전체 캔버스, 그림 썸네일 |
| 08 Editing text format | 4 | 참고 | 글 서식 패널과 본문 변형 |
| 09 Asking AI for insights | 5 | 참고 | 멘토 sheet, 생성 중/완료 상태 |
| 10 Evening reflection | 12 | 선택 | 휴식 척도, 감정 다중 선택/확장, 요약·사진·완료 |
| 11 Quote journal | 2 | 참고 | Today Quote에서 별도 작성 sheet |
| 12 Personalizing page content | 4 | 참고 | Today 표시 항목 토글·편집 |
| 13 Adding prompts to daily reflections | 15 | 참고 | 편집 카드 carousel, 카탈로그, 새 prompt, 저장 경고 |
| 14 Adding a focus | 8 | 참고 | Focus 원형 격자, 새 Focus의 이름·아이콘 |
| 15 Hiding a focus | 4 | 참고 | 더보기→Hide→Hidden 구역 |
| 16 Adding a metric to daily reflections | 8 | 참고 | Metrics 카탈로그, Scale/Yes-No segmented 선택, 저장 경고 |
| 17 Tomorrow | 2 | 선택 | Today에서 다음 날로 이동, 새의 countdown empty state |
| 18 Inspirations | 8 | 참고 | 큰 몰입형 카드, swipe/테마/기능 탐색 |
| 19 Share a prompt | 4 | 참고 | 공유 이미지 carousel·워터마크 toggle |
| 20 Favoriting a prompt | 2 | 참고 | 별 윤곽→채움 |
| 21 Choosing a card theme | 3 | 참고 | 테마 chooser·사진형 카드 |
| **합계** | **145** | | 모든 `screen-*.webp` 확인 |

## 반복 규칙과 근거

`확신 높음` = 여러 장에서 반복/상태 전이 확인. `중간` = 동일한 제한된 맥락에서 반복. `낮음` = 단일 캡처 또는 크기/색상 정량값 미측정.

**픽셀 표본으로 확인한 두 표면 계열:** 원본 WebP의 빈 배경·카드 중심색을 RGB 빈도로 비교했다. 01/01·05/02–03은 canvas `#F3F3F5`; 01/03·04/01·05/06·18/02는 이 canvas와 card `#FFFDFE`가 함께 나타난다. 반면 04/02–04·10/02–03·13/02–09는 canvas `#F1F3F4`와 card `#FFFFFF` 계열이다. 즉 **04 Today 한 흐름에서도 화면 01과 02–04의 색 계열이 다르다.** 선택 화면 재현에는 해당 캡처의 색을 우선하고, 새 컴포넌트는 그 컴포넌트가 놓이는 화면의 표면 계열을 따른다. 원본이 서로 다른 시기/테마인지는 캡처만으로 확정할 수 없다. 검정 Mobbin footer의 `#2F2F2F` 빈도는 앱 색으로 세지 않았다.

| 패턴 | 정확한 근거 화면 | 시각/동작 규칙 | 변형·예외 | 확신 |
|---|---|---|---|---|
| 밝은 앱 바탕과 검은 강조 | 04/01–06, 05/01–18, 10/01–12, 17/01–02 | 거의 흰 회색 바탕, 검정 텍스트·활성 버튼, 흰 콘텐츠 표면이 기본. 비어 있는 큰 여백도 구성 요소. | 04/01 진입 카드는 어두운 검정, 21/03 사진형 테마도 검정, 02/01·18/04는 유료/테마 이미지·그라데이션. 모든 카드를 흰색으로 일반화하면 안 됨. | 높음(색값 낮음) |
| 굵은 제목/단정한 보조 문구 | 01/01–12, 05/02–08, 10/02–03, 13/02–04, 16/02–04 | 제목은 굵고 둥근 산세리프 느낌; 설명과 메타는 작고 회색. 짧은 소문자+마침표 대형 제목(`today.`, `morning preparation.`, `add items.`)과 sentence case 질문을 구분. | 긴 작성 본문 05/09–10·10/07–10은 표준 본문 크기, 08/03에서 의도적으로 큰 heading 서식; 19/03·21/03 사진 테마에서 serif 스타일. | 높음(폰트명/치수 낮음) |
| primary capsule과 보조 outline | 01/02–12, 05/02·11–12·18, 10/11, 18/02·07 | 검은 채움+흰 글자의 둥근 capsule이 최상위 CTA. 하얀 채움/얇은 회색 선과 검은 글자가 보조. 선택·비활성 시 회색/검정 전환. | 04/01 어두운 카드에서는 흰 채움 `Begin`; 05/03–10·10/02–10은 하단 우측 검은 **원형** 화살표로 전진; 13/08 카탈로그의 Add 작은 capsule. | 높음 |
| 선택 컴포넌트는 맥락별 형태 | 01/02–05, 05/06–08, 10/03–06, 16/02–04 | 미선택 흰 배경, 선택 검은 배경+흰 글자/아이콘. 질문의 제약에 맞춰 단일/복수 선택, 펼침과 추가 항목을 표현. | 온보딩 답은 가로 capsule; Focus는 **원형 아이콘 격자**+아래 라벨; 감정은 **2열 둥근 직사각형**; metric 응답형은 **segmented control**. `choice-chip` 하나의 pill 형태로 묶을 수 없음. | 높음 |
| 스위치와 시간 설정 | 01/06–10, 12/02–03, 19/02–04 | 리스트 행 오른쪽에 toggle; off는 회색 track, on은 색이 맥락별로 다름. 시간 탭은 iOS picker overlay, OS 권한은 native alert. | 01/06–09 알림 토글은 푸른색, 12/02–03 개인화·19/04 watermark 토글은 검정; black on을 모든 switch에 적용하지 말 것. | 높음 |
| 홈 상단 date strip/상태 | 04/01–03, 10/12, 17/01–02 | 인사말·streak chip·프로필 아이콘 아래 일주일 날짜 strip; 선택 날짜가 얇은 테두리의 세로 pill로 강조. 완료 요일 체크와 흐린 미래 날짜. | Tomorrow 17/02에서 헤더 `tomorrow.`와 다음 날짜 강조, 본문은 countdown. 타임존/실제 시각에 따른 텍스트는 별도 구현 결정. | 높음 |
| Today 반영 카드의 생명주기 | 04/01–03, 10/12, 12/04 | 시작 전 어두운 Morning 단일 카드 혹은 밝은 Morning/Evening 2열 카드, 완료 후 흐린 배경+선택 요약 pill로 교체. | 시간대·기존 작성 상태에 따라 카드 레이아웃 자체가 바뀜. `content-card = white + radius16`로 표현 불가. 04/04–06 하단 Quote/영감 영역은 범위 제한을 따름. | 높음 |
| reflection chrome/진행 표시 | 05/02–18, 06/01–06, 08/01–04, 10/02–10 | 좌 Back/설정, 중앙 얇은 짧은 segment progress, 우 Close; 질문 본문 아래는 넓은 공간; 하단 action은 키보드/패널 위로 이동. | Intro(05/02)와 완료(05/16–18,10/11)는 같은 작성 단계 chrome이 아님. 05/11–15 AI 단계 제외 시 segment 수를 재산정해야 함. | 높음 |
| reflection 수치 입력 | 05/03–04, 10/02, 13/02, 16/01 | 서술값은 슬라이더 위치에 따라 `moderate`→`quite well` 등 변화. 흰 track 위 검은 진행 바와 원형 손잡이, 극점 양쪽 small caption. | 16/06 새 metric의 Yes/No는 작은 outline pills. 같은 질문 카드 안에서도 실제 입력형별 모양이 다름. | 높음 |
| 글쓰기 canvas와 accessory | 05/09–10, 06/01–06, 07/01·04, 08/01–04, 10/07–10 | 질문 아래 placeholder `Start writing...`, 풀 폭 무테두리 본문. 하단 `+`, `Aa`, AI sparkle, 원형 forward 순서; 키보드가 나오면 bar가 위로 상승. | 10/07–10은 사진 permission/thumbnail strip가 본문 앞; 05/09는 툴팁과 키보드. `+`, `Aa`, AI/음성/그림은 원본에 있지만 브리프의 범위 확인 없이 새 구현 기능으로 추가하면 안 됨. | 높음 |
| 카드/셀 그룹의 표면 | 02/01–07, 04/01–06, 12/02–03, 13/04–07, 18/02–08 | 흰 카드와 둥근 모서리, 잔잔한 경계/그림자; 카드 내부의 정보·CTA를 가운데 또는 리스트로 정렬. | 원본에는 홈 약 2열 긴 카드(04/03), 전체 높이 영감 카드(18/02–08), 세로 carousel 카드(13/02–07), 설정 행(12/02) 등 여러 anatomy가 있음. 고정 card token 하나는 불충분. | 높음 |
| 스크롤/가로 carousel/하단 고정 | 02/01–07, 04/04–06, 13/02–07, 18/02–08, 19/02–04 | 콘텐츠는 세로 스크롤되고 일부 카드는 좌우 이웃 카드 peek로 가로 스와이프를 암시. 중요 CTA/탭은 하단 safe area 위에 남음. | 13/02–07 페이지 점은 carousel 위치; 18/02–08은 영감 카드 자체 전환. 원본 하단 5탭+중앙 create는 이번 브리프에서 축소 대상. | 높음 |
| sheet와 modal stack | 11/02, 12/02–03, 13/01–15, 14/01–08, 16/01–08, 19/02–04, 21/02 | 어두워진 배경 위 상단 둥근 sheet, X/Cancel/Save 계층. sheet 안에서 또 편집 sheet가 열릴 수 있음. | 09/03 mentor는 흰 하단 반높이 sheet, 19/02는 공유 full-height sheet, 13/14는 iOS 시스템 confirmation alert. 모든 sheet가 동일한 높이나 제목 구성을 쓰지 않음. | 높음 |
| empty/completion의 큰 중심 요소 | 05/16–18, 10/11, 17/02, 18/08 | 아이콘/새/꽃 같은 흑백 상징과 굵은 문구를 중앙에 놓고 넓은 여백 확보; 다음 행동은 하단 CTA. | 17/02 countdown은 Today nav가 살아있고 05/18 완료는 별도 `Keep exploring stoic.`. streak는 데이터 의존; 18/08은 안내 카드(참고). | 높음 |
| 편집 전후의 확인/비활성 상태 | 02/07–09, 13/09–14, 16/02–07 | 미입력 action은 흐린 회색. 편집 저장은 명시적인 Save/Add; 이미 존재하는 오늘 답이 변경될 때 영향 설명 alert로 재확인. | 구독 확인 alert 02/09는 Apple 결제 맥락; 13/14·16/07 reflection 변경 경고는 참고 흐름이며 이번 범위의 새 기능을 뜻하지 않음. | 높음 |
| 도상 언어 | 01/01·11–12, 05/02–05·16–18, 10/02·11, 17/02, 21/03 | 검은 새 실루엣/태양·달/단순 선화가 반복. Focus icon은 단색 채움 glyph+원형 흰 표면. | 18/04·19/03·21/03 사진 테마는 비단색이고 범위 밖; 남는 일러스트를 SVG로 재현한다는 브리프 준수. | 높음 |

## 재사용 컴포넌트 anatomy와 상태

- **선택 항목:** hit target/아이콘·문구/선택 배경을 각각 정의. `answer pill`(01/02–05), `emotion tile`(10/03–06), `focus icon circle`(05/06–08), `segmented selector`(16/02–04)는 동작 primitive(선택)는 공유하되 형태는 별도 variant. 감정은 여러 개 동시 선택(10/04); Focus는 최대 3(05/06). 나이는 단일(01/04–05).
- **Today reflection card:** 상태는 Morning 미시작(04/01 dark), 양쪽 미시작(04/03), Morning 완료(04/02), Evening 완료(10/12), 시각에 따라 대형 단일/2열. 각 카드의 label, 중심 메시지, bottom Begin/요약 pill 순으로 읽힘. 참고용 Quote/영감 블록은 독립 형상(04/04–06).
- **reflection step:** 상단 Back + segments + Close, 본문 질문/설명·입력, 하단 원형 Next. 감정 확장(10/03→05–06)은 같은 step 내부 스크롤/상태, 다음 progress step이 아님. 키보드·media overlay(05/09,06/03–06,10/07–10)는 하단 accessory와 함께 올라감.
- **notification row:** 좌 label+굵은 시간+chevron, 우 switch(01/06–09). 편집 중 native time picker가 sheet처럼 겹침; OS 권한 prompt는 native(01/10). 단색 블랙 switch로 바꾸지 말 것.
- **sheet:** dim backdrop, 상단 close/cancel/save, 큰 중앙 제목 또는 섹션 label, 내용 리스트/카드, safe-area bottom. `Save`는 미입력 비활성(13/02,14/01), 입력 뒤 활성(13/13,14/07). Nested dismissal는 스택 순서(13/09–15).
- **완료/empty:** 큰 symbol, 짧은 headline, 보조 copy, 데이터 요약/streak, 다음 CTA의 순서(05/16–18,10/11). Tomorrow의 countdown은 별도 read-only empty(17/02).

## 구현 범위를 넓히지 말아야 할 원본 기능

02 구독/paywall·후속 결제, 03 유료 기능, 05/11–15·09 AI mentor/AI insight, 06 음성 녹음/전사, 07 sketch, 08 rich text formatting, 11 quote journal, 12 Today 사용자 편집기, 13 prompt 관리/새 prompt, 14–15 custom/hidden Focus 관리, 16 custom metric 생성, 18 Inspirations 탭/카드, 19 공유, 20 즐겨찾기, 21 카드 테마 선택은 **참고 증거**만이다. 04/01–06의 `on glowing reviews`와 `Get Inspired`, 하단 Inspirations/Library/중앙 `+`, 10/07–10의 사진 접근·첨부와 10/11의 별도 night readiness 선택도 선택된 캡처에 나타나지만 브리프의 명시 범위 및 화면별 선정표와 대조해야 한다. 특히 원본에 보인다는 이유만으로 기능 구현하지 않는다. 예외는 01/11–12의 `AI Mentors` 표시 카드(기능 없음).

## 현재 spines와의 구체적 차이/보완 제안

1. `DESIGN.md`의 `choice-chip`은 모두 pill로 정의됐지만 05/06–08 Focus는 원형, 10/03–06 감정은 2열 둥근 직사각형이다. 공통 선택 state와 형태 variant를 분리해야 한다.
2. `DESIGN.md`의 `content-card = surface + radius16`은 04/01 어두운 hero, 04/03 2열 tall cards, 04/02·10/12 완료된 outlined/gray 카드, 18/02 몰입형 카드의 근거를 담지 못한다. 선택된 Today 카드 상태 variant를 우선 정의할 것.
3. `DESIGN.md`의 스위치/토큰에서 01/06–09의 파란 notification on과 12/02–03의 검은 setting on을 구분해야 한다. `#...` 색값과 8/16/24px radius·spacing은 현재 시각적 추정이지 145장 대조에서 측정 확정된 수치가 아니다.
4. `EXPERIENCE.md`의 `Pill action` 설명은 reflection의 우측 하단 **원형** 진행 버튼(05/03–10,10/02–10)을 별도 primitive로 정의해야 한다. 05/02 intro의 `Continue`는 capsule이다.
5. `EXPERIENCE.md`의 `Today` 상태·컴포넌트에는 04/01 dark Morning card, 04/03 2열 카드, 04/02·10/12 완료된 gray/outlined 카드의 구조 전환이 명시돼야 한다.
6. 10/03→06 감정은 multi-select와 Show more/less를 사용하고 한 step에서 스크롤한다. `EXPERIENCE.md`의 focus/emotion 공통 설명보다 상태 전이를 구체화할 것.
7. 01/11의 회색 Continue는 체크리스트 마지막 항목 완료 후 01/12 검은 Continue로 바뀐다. 이를 generic 온보딩 CTA 상태로 기록할 것.
8. `DESIGN.md`/`EXPERIENCE.md`에 위처럼 근거 화면 번호를 직접 붙이면 나중에 새 컴포넌트를 설계할 때 전체 캡처를 재조사하지 않아도 rule→source→exception을 추적할 수 있다.

## 한계

Contact sheet로 145장의 구성/상태를 전부 확인했고 일부 원본의 배경/표면 RGB 빈도를 계측했다. 다만 모든 색·좌표·타입 페이스를 계측하지는 않았으며, radius·spacing·font size 토큰은 별도 원본 pixel sample/side-by-side 검증 없이는 `추정`으로 표시해야 한다. 이 감사는 01–21번만 담당하며 나머지 corpus를 대표한다고 주장하지 않는다.
