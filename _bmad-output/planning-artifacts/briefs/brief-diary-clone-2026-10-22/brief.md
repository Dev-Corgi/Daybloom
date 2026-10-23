---
title: "Product Brief: DiaryClone"
status: ready_for_review
created: 2026-10-22
updated: 2026-10-23
---

# Product Brief: DiaryClone

## 목적

DiaryClone은 장차 AI 기능을 갖춘 일기 앱을 만들기 위한 첫 단계다. 화면과 기본 경험을 처음부터 설계하는 대신, Stoic의 **선택한** 일기 흐름을 Android와 iOS에서 충실히 재현해 작동하는 기반을 마련한다. 이번 단계는 내부 개발용 클론이며 새로운 AI 기능이나 독자적인 제품 경험을 추가하지 않는다. 후속 제품의 대상 사용자와 AI 가치 제안은 아직 정하지 않았다.

## 사용자 경험

사용자는 온보딩을 거쳐 Today에서 아침·저녁 성찰을 작성하고, Tomorrow를 확인하며, Journey에서 저장한 일기와 기분의 흐름을 돌아본다. 기록은 기기에 저장되어 앱을 다시 열어도 남는다. 포함된 조회·수정·정렬·통계 화면은 예시 데이터가 아닌 실제 기록을 반영한다. Profile에서는 포함된 알림 설정과 Privacy policy 화면에 접근한다. 화면 문구는 영어로 제공한다.

## 이번 단계의 범위

| 영역 | 포함할 흐름 | 경계 |
| --- | --- | --- |
| 시작 | Onboarding | 캡처된 마지막 화면은 제외 |
| 오늘 | Today, Morning reflection, Evening reflection, Tomorrow | `on glowing reviews`와 `Get Inspired` 컴포넌트·기능은 제외 |
| 문구 | Today의 Quote 표시 | Quote journal, Favorite, Share는 제외 |
| 기록 | Journey, Entry detail, Daily entries | 포함된 화면의 기록 조회·수정 동작을 실제 데이터로 연결 |
| 돌아보기 | Trends & insights, Mood calendar, Sorting by months | 저장된 기록과 기분 데이터로 표시. Sorting by months는 Trends의 기간 전환(Flow 49)이며 Journey의 월별 기록 탐색은 제외 |
| 설정 | Profile, Turning on notifications, Privacy policy | 선택한 화면과 알림 권한·설정 흐름을 구현 |

원본 화면에 범위 밖 기능의 버튼·카드·진입점이 있으면 제거한다. **예외:** 온보딩에 남는 `AI Mentors` 카드와 문구는 원본 디자인을 유지하기 위해 그대로 표시한다. 이번 단계에 AI 기능은 없으며, 이 클론은 내부 개발용이다. 해당 문구와 실제 기능의 정합성은 후속 제품 개발에서 다룬다.

계정, 클라우드 동기화, 다국어 지원은 후속 단계로 미룬다.

## 디자인 원칙

기준 자료는 `docs/Stoic/flows`의 캡처와 흐름 문서다. 범위에 남는 화면에서 요소의 크기, 색상, 배치와 시각적 계층을 캡처에 맞춘다. 남는 일러스트와 아이콘은 SVG로 재현한다. Android에서도 같은 앱 화면 디자인을 사용하고, 상태 표시줄·권한 대화상자 등 시스템 UI만 플랫폼에 맞춘다. iOS 캡처의 393 × 852 화면을 우선 비교 기준으로 삼되, 실제 Android·iOS 기기 화면에서도 콘텐츠가 잘리거나 조작을 막지 않아야 한다.

### `bmad-ux`에 넘길 디자인 참고 범위

위 표에서 지정한 플로우만 이번 **구현 대상**이다. `docs/Stoic/flows`의 나머지 플로우와 화면은 **디자인 참고 자료**로 사용한다. `bmad-ux`가 `DESIGN.md`의 토큰·컴포넌트 기준과 `EXPERIENCE.md`의 동작 패턴을 정할 때, 전체 캡처에서 반복되는 타이포그래피, 색상, 간격, 형태, 아이콘, 화면 상태와 상호작용을 살펴 일관된 규칙으로 정리한다. 이후 새로운 화면이나 컴포넌트가 필요해지면 그 규칙에 맞춰 설계한다. 참고 자료에 있다는 이유만으로 해당 화면이나 기능을 이번 구현 범위에 추가하지 않는다. 선택한 화면의 클론은 해당 화면의 캡처를 우선 기준으로 삼는다.

## 완료 기준

- 선택한 모든 흐름이 Android와 iOS에서 처음부터 끝까지 실행된다. 포함된 조작은 빈 화면이나 동작하지 않는 버튼으로 끝나지 않는다.
- 작성한 성찰과 일기가 기기에 저장되고 앱 재실행 뒤에도 조회·수정할 수 있다. Journey, Daily entries, Entry detail, Trends & insights의 주·월 보기, Mood calendar가 해당 데이터를 일관되게 보여 준다.
- 알림 설정 흐름은 각 운영체제의 권한 상태와 연결된다.
- 포함된 화면을 기준 캡처와 나란히 비교해 레이아웃, 크기, 색상, 배치, SVG 일러스트·아이콘을 맞춘다. 범위 밖 컴포넌트는 화면에 남지 않는다.
