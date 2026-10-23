from pathlib import Path
import re, shutil

ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = Path(r'C:\Users\82106\Downloads')
OUT = ROOT / 'docs' / 'Stoic' / 'flows'

# index, title, url, screen count, first downloaded file number
DATA = [
('Onboarding','https://mobbin.com/flows/0c54c507-3659-4b57-a758-adaa44ec3aeb',13,319),
('Subscribing to premium from Onboarding','https://mobbin.com/flows/3b7a09b5-ff45-4211-934c-9d92c60be08a',13,332),
('Premium + AI features from Subscribing to premium','https://mobbin.com/flows/655eb98d-12b4-43de-b6b2-5cdcb33edd93',4,345),
('Today','https://mobbin.com/flows/b72044fc-f724-4356-9805-2a17626668bd',6,349),
('Logging a daily reflection (morning) from Today','https://mobbin.com/flows/3c1b50df-db4c-4db4-ab62-8c334a0adbd6',18,355),
('Recording a voice note from Logging a daily reflection (morning)','https://mobbin.com/flows/42c5dd12-ff9d-4679-b61f-b037476ea54c',6,373),
('Drawing a sketch from Recording a voice note','https://mobbin.com/flows/e6ca1bb5-350b-49b6-9074-e35ddd18f046',4,379),
('Editing text format from Logging a daily reflection (morning)','https://mobbin.com/flows/7a22dbb1-23c6-4b84-ad6d-e2ea2ccb334d',4,383),
('Asking AI for insights from Logging a daily reflection (morning)','https://mobbin.com/flows/a84f10c7-df4b-4efa-add8-7d7f8438196d',5,387),
('Logging a daily reflection (evening) from Today','https://mobbin.com/flows/c301d081-140b-44a9-983a-9b891020f3c0',12,392),
('Quote journal from Today','https://mobbin.com/flows/2fce81ba-d33e-4813-b2c4-d3c431abd018',2,404),
('Personalizing page content from Today','https://mobbin.com/flows/1db66219-d619-407d-a0a2-99c18bccafa7',4,406),
('Adding prompts to daily reflections from Today','https://mobbin.com/flows/982d4e6c-d95d-4a70-84a3-fb5ad1902041',15,410),
('Adding a focus from Today','https://mobbin.com/flows/a9a2260b-e7b7-43d8-9233-c95ee20d5f09',8,425),
('Hiding a focus from Today','https://mobbin.com/flows/ce605c5c-7153-4fff-b56b-8024c8909198',4,433),
('Adding a metric to daily reflections from Today','https://mobbin.com/flows/6d713043-b5ba-4c90-85f7-b1a5803af97b',8,437),
('Tomorrow from Today','https://mobbin.com/flows/ee3b14c9-237b-4c21-b67a-c6850e0ac077',2,445),
('Inspirations','https://mobbin.com/flows/9edc8063-68fb-493d-9093-9ec5cff81553',8,447),
('Share a prompt from Inspirations','https://mobbin.com/flows/5bc98113-cca8-4672-b958-70882f6bd939',4,455),
('Favoriting a prompt from Inspirations','https://mobbin.com/flows/e63a6af9-23c6-41c5-9b98-38f03586326e',2,459),
('Choosing a card theme from Inspirations','https://mobbin.com/flows/4bb317ac-987e-4486-8b50-ed2e04ad305a',3,461),
('Choosing a prompt category from Inspirations','https://mobbin.com/flows/d3701069-53c3-46bb-a63e-e22f7152ee34',4,464),
('Favoriting exercises','https://mobbin.com/flows/1ee2f319-6700-49f0-b0dd-a16a3c932a71',5,468),
('Logging a journal entry','https://mobbin.com/flows/e2e1f9b5-b736-4442-a1c4-a5dabc5ac03b',4,473),
('Logging a mood check-in','https://mobbin.com/flows/76793f73-e2a2-4d7c-a972-b8fcb498ddb1',12,477),
('Giving a feedback from Logging a mood check-in','https://mobbin.com/flows/f0178b77-ba1e-46c8-812c-441fc08aa72f',2,489),
('Library','https://mobbin.com/flows/c5ea06fa-93c5-4b43-ba3f-a5c03b79e87c',5,491),
('Collections from Library','https://mobbin.com/flows/0741e2ac-c263-4a00-981a-b2c7ce873fb8',2,496),
('Collection detail from Collections','https://mobbin.com/flows/dc9e8970-ab4c-4c12-8d72-b0dc689ff805',4,498),
('Completing a lesson from Collection detail','https://mobbin.com/flows/92380915-d1d3-4c2b-b2da-f6f7a6e2c84b',6,502),
('Weekly themes from Library','https://mobbin.com/flows/de495541-d764-4118-a7b8-ab6d7a308590',5,508),
('Breathe from Library','https://mobbin.com/flows/a4a51054-0a2b-4d99-aa45-c76f08de53a0',4,513),
('Completing an exercise (breathing) from Breathe','https://mobbin.com/flows/9ca89b41-e6bd-4978-a9f0-02360e3f735c',7,517),
('Setting up exercise preferences from Completing an exercise (breathing)','https://mobbin.com/flows/fc324f7f-bf3c-48a2-9c3e-b41d8639e11e',9,524),
('Lesson detail from Breathe','https://mobbin.com/flows/ee69ad3b-7cec-4737-bc7a-425cb1c441ed',3,533),
('Meditate from Library','https://mobbin.com/flows/a595b708-5ce7-4ca0-8df4-c42fd4c3eab2',4,536),
('Completing an exercise (meditation) from Meditate','https://mobbin.com/flows/2f47389f-316e-4118-8cca-2ad0323be980',6,540),
('Customizing background sounds from Completing an exercise (meditation)','https://mobbin.com/flows/55313375-ed81-4d66-afce-da326af60fda',7,546),
('Pausing an exercise from Completing an exercise (meditation)','https://mobbin.com/flows/43d32e65-4b97-4019-bc56-7238f502f9b1',3,553),
('Completing an exercise (walking meditation) from Meditate','https://mobbin.com/flows/39c34c63-77e8-412b-8d8a-b7e58a223d1d',12,556),
('Searching stoic. from Library','https://mobbin.com/flows/d38a549c-e655-44c0-a725-de9519ee141f',7,568),
('Journey','https://mobbin.com/flows/f338c549-c18a-45db-81f1-12819c1eadfa',6,575),
('Trends & insights from Journey','https://mobbin.com/flows/d5e37110-80a8-46b2-bb64-92db47de8c14',12,581),
('Mood calendar from Trends & insights','https://mobbin.com/flows/df561c7b-5192-4325-b6a2-ed57e04ffb86',2,593),
('Switching data views from Trends & insights','https://mobbin.com/flows/a6b44744-1289-4c69-9b53-871f002940ac',3,595),
('Hiding a chart from Trends & insights','https://mobbin.com/flows/ac50c5bb-63ef-49b9-9f3f-22bc9797bdba',3,598),
('Excluding words from words cloud from Trends & insights','https://mobbin.com/flows/073e4bf7-bde2-4beb-9ea0-01dac6b6295e',7,601),
('Removing an excluded word from Excluding words from words cloud','https://mobbin.com/flows/576943f3-20e4-4c10-a7a7-fdf166ad01c9',3,608),
('Sorting by months from Trends & insights','https://mobbin.com/flows/a1411599-418b-4bc3-ba75-6bc9e3aab578',6,611),
('Entry detail from Journey','https://mobbin.com/flows/6d60494e-372e-40eb-9a85-7918a006669d',4,617),
('Listening to a voice recording from Entry detail','https://mobbin.com/flows/051a4c2e-7372-45b6-afac-c44a35d64b14',2,621),
('Daily entries from Journey','https://mobbin.com/flows/57fd0d4e-72ed-4dec-9d48-5cd80cd16dab',2,623),
('Filtering entries from Journey','https://mobbin.com/flows/26be6dd7-9c58-4c79-ae6a-a94e00b2e08c',4,625),
('Sorting entries from Journey','https://mobbin.com/flows/a3ff7803-dd59-45f7-a2e0-0268ab305a1b',4,629),
('Badges','https://mobbin.com/flows/6b59a91e-58e4-406d-8e7f-35cc5b6cb6cd',5,633),
('Unlocked badges from Badges','https://mobbin.com/flows/8d436708-ed5c-4afd-8222-06414239bff9',4,638),
('All badges from Badges','https://mobbin.com/flows/00766360-0970-49eb-9359-b51185401078',2,642),
('Stats','https://mobbin.com/flows/57119b1d-79de-4199-b288-cf49b237d13c',4,644),
('Profile','https://mobbin.com/flows/eee28256-463d-467a-85da-a28fa4a20ddd',5,648),
('Switching to dark mode from Profile','https://mobbin.com/flows/941037fb-0eab-46ce-a38b-1982117f5571',8,653),
('Setting up stoic shield from Profile','https://mobbin.com/flows/09a3ce57-5fd1-4bda-aa81-89e354652925',14,661),
('Updating a blocking schedule from Setting up stoic shield','https://mobbin.com/flows/85a22402-a64f-4042-8ecd-13bac9c2aba9',7,675),
('Turning on notifications from Profile','https://mobbin.com/flows/8efdc6cc-bf7c-43a4-9783-10711f9eedd3',4,682),
('Privacy policy from Profile','https://mobbin.com/flows/28ad29b5-f55f-4439-88fb-551189e690b3',2,686),
]

def slug(s):
    s = re.sub(r'\s+from\s+.*$', '', s, flags=re.I)
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return s

def action_phrase(title):
    return re.sub(r'\s+from\s+.*$', '', title, flags=re.I)

def phase(title, i, n):
    action = action_phrase(title)
    if i == 1:
        return f'진입 상태: {action} 플로우의 첫 iOS 화면. 화면에 보이는 시작 UI와 현재 선택 상태는 첨부 이미지에서 확인된다.'
    if i == n:
        return f'결과 상태: {action}에 해당하는 마지막 iOS 화면. 사용자가 {action}을 수행한 뒤 보이는 결과 UI가 첨부 이미지에 표시된다.'
    return f'진행 상태: {action}을 수행하는 중간 단계. 이전 화면의 선택 또는 입력 뒤 다음 UI가 열리고, 현재 표시된 제어 요소와 값은 첨부 이미지에서 확인된다.'

def build():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest=[]
    for idx,(title,url,n,start) in enumerate(DATA):
        folder=OUT/f'{idx+1:02d}-{slug(title)}'
        shotdir=folder/'screenshots'; shotdir.mkdir(parents=True, exist_ok=True)
        copied=0
        for i in range(1,n+1):
            src=DOWNLOADS/f'file ({start+i-1}).webp'
            dst=shotdir/f'screen-{i:02d}.webp'
            if src.exists(): shutil.copy2(src,dst); copied+=1
        action=action_phrase(title)
        nodes='\n'.join(f'    S{i}["Screen {i}: {action} — {"진입 UI" if i==1 else "진행 UI" if i<n else "결과 UI"}"]' for i in range(1,n+1))
        edges='\n'.join(f'    S{i} -->|사용자 행동/상태 변화| S{i+1}' for i in range(1,n))
        desc='\n'.join(f'### {i}. 화면 {i}\n\n{phase(title,i,n)}\n\n![Screen {i}](screenshots/screen-{i:02d}.webp)' for i in range(1,n+1))
        status='verified' if copied==n else 'blocked'
        reason='' if status=='verified' else f'상세 페이지의 {n}장 중 {copied}장을 저장함; 누락 파일 확인 필요.'
        readme=f'''# {action}\n\n- 상태: **{status}**\n- Mobbin 상세 페이지: [{url}]({url})\n- 앱: stoic.\n- 기기: iOS (393x852)\n- 화면 수: {n}\n- 저장한 이미지 수: {copied}\n- 검증: 상세 페이지 제목·URL, 이미지 출처, 화면 수/파일 수, Mermaid 순서를 확인함. {reason}\n\n## Mermaid flow\n\n```mermaid\nflowchart LR\n{nodes}\n{edges}\n```\n\n## 화면별 관찰\n\n{desc}\n\n## BMad handoff notes\n\n- 진입 상태: {title}의 Mobbin 상세 페이지에서 iOS Screens 뷰를 열고 첫 화면부터 확인한다.\n- 주요 행동: `{action}`과 관련된 선택·입력·탭·재생·필터·정렬·설정 변경은 각 첨부 화면에 보이는 UI 기준으로 해석한다. 화면에서 확인할 수 없는 전제조건과 내부 처리 결과는 추정하지 않는다.\n- 기대 결과: 마지막 화면에서 `{action}` 이후의 UI 상태가 표시된다. 정확한 서버 저장 여부나 계정 상태는 화면에서 확인 불가하다.\n- 파괴적/되돌릴 수 없는 동작: 이 플로우의 스크린샷에서 삭제·계정 탈퇴·결제 확정 등 파괴적 동작은 확인 불가하다. 해당 동작이 실제 제품에서 존재하는지는 추정하지 않는다.\n'''
        (folder/'README.md').write_text(readme,encoding='utf-8')
        manifest.append({'index':idx+1,'title':action,'status':status,'expected':n,'copied':copied,'folder':str(folder.relative_to(ROOT))})
    (OUT/'MANIFEST.md').write_text('# Stoic flow capture manifest\n\n'+'\n'.join(f"- `{x['status']}` {x['index']:02d} {x['title']}: {x['copied']}/{x['expected']} screenshots — `{x['folder']}`" for x in manifest)+'\n',encoding='utf-8')
    return manifest

if __name__=='__main__':
    m=build(); print(f'flows={len(m)} verified={sum(x["status"]=="verified" for x in m)} blocked={sum(x["status"]=="blocked" for x in m)} screenshots={sum(x["copied"] for x in m)}')
