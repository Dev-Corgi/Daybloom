# Tomorrow

- 상태: **verified**
- Mobbin 상세 페이지: [https://mobbin.com/flows/ee3b14c9-237b-4c21-b67a-c6850e0ac077](https://mobbin.com/flows/ee3b14c9-237b-4c21-b67a-c6850e0ac077)
- 앱: stoic.
- 기기: iOS (393x852)
- 화면 수: 2
- 저장한 이미지 수: 2
- 검증: 상세 페이지 제목·URL, 이미지 출처, 화면 수/파일 수, Mermaid 순서를 확인함. 

## Mermaid flow

```mermaid
flowchart LR
    S1["Screen 1: Tomorrow — 진입 UI"]
    S2["Screen 2: Tomorrow — 결과 UI"]
    S1 -->|사용자 행동/상태 변화| S2
```

## 화면별 관찰

### 1. 화면 1

진입 상태: Tomorrow 플로우의 첫 iOS 화면. 화면에 보이는 시작 UI와 현재 선택 상태는 첨부 이미지에서 확인된다.

![Screen 1](screenshots/screen-01.webp)
### 2. 화면 2

결과 상태: Tomorrow에 해당하는 마지막 iOS 화면. 사용자가 Tomorrow을 수행한 뒤 보이는 결과 UI가 첨부 이미지에 표시된다.

![Screen 2](screenshots/screen-02.webp)

## BMad handoff notes

- 진입 상태: Tomorrow from Today의 Mobbin 상세 페이지에서 iOS Screens 뷰를 열고 첫 화면부터 확인한다.
- 주요 행동: `Tomorrow`과 관련된 선택·입력·탭·재생·필터·정렬·설정 변경은 각 첨부 화면에 보이는 UI 기준으로 해석한다. 화면에서 확인할 수 없는 전제조건과 내부 처리 결과는 추정하지 않는다.
- 기대 결과: 마지막 화면에서 `Tomorrow` 이후의 UI 상태가 표시된다. 정확한 서버 저장 여부나 계정 상태는 화면에서 확인 불가하다.
- 파괴적/되돌릴 수 없는 동작: 이 플로우의 스크린샷에서 삭제·계정 탈퇴·결제 확정 등 파괴적 동작은 확인 불가하다. 해당 동작이 실제 제품에서 존재하는지는 추정하지 않는다.
