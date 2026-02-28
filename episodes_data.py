# ── 小猪佩奇外挂攻略 · 第1季全52集 内容数据 ──────────────────────────────


def _ep(num, title_en, title_zh, color, synopsis, vocab, patterns, goals,
        phase1, phase2, phase3, phase4, phase5, phase6, checklist, ammo):
    return dict(num=num, title_en=title_en, title_zh=title_zh, color=color,
                synopsis=synopsis, vocab=vocab, patterns=patterns, goals=goals,
                phase1=phase1, phase2=phase2, phase3=phase3,
                phase4=phase4, phase5=phase5, phase6=phase6,
                checklist=checklist, ammo=ammo)


# ═══════════════════════════════════════════════════════════════════════════════
# EP 10 · Gardening 种花园
# ═══════════════════════════════════════════════════════════════════════════════
EP10 = _ep(
    num=10, title_en="Gardening", title_zh="种花园", color="green",
    synopsis="Peppa 和 George 去爷爷奶奶家，爷爷正在种种子。Peppa 亲手种了一颗草莓种子，耐心等了很多天，终于长出了甜蜜的草莓。George 表示他想种一棵恐龙树。",

    vocab=[
        {"word":"seed","phonetic":"/siːd/","pos":"n.","zh":"种子","action":"用拇指和食指捏出一个几乎不存在的小点，放进想象的洞里，\"So tiny!\""},
        {"word":"plant","phonetic":"/plɑːnt/","pos":"v.","zh":"种植","action":"蹲下，手指戳地，假装埋种子，再拍拍土盖好"},
        {"word":"grow","phonetic":"/ɡrəʊ/","pos":"v.","zh":"生长","action":"从蹲着缓缓站起，双臂向上展开，越变越高"},
        {"word":"earth","phonetic":"/ɜːθ/","pos":"n.","zh":"泥土","action":"捧起手心，假装抓一把土，手指搓一搓，闻一闻"},
        {"word":"patient","phonetic":"/ˈpeɪʃnt/","pos":"adj.","zh":"耐心的","action":"双手合十放胸前，闭眼，深呼吸，\"Wait... wait...\""},
        {"word":"strawberry","phonetic":"/ˈstrɔːbri/","pos":"n.","zh":"草莓","action":"做出摘果实放进嘴里的动作，闭眼满足地 \"Mmm！\""},
        {"word":"water","phonetic":"/ˈwɔːtə/","pos":"v.","zh":"浇水","action":"手握想象的水壶，一上一下倾斜，发出 \"Glug glug glug...\""},
        {"word":"tiny","phonetic":"/ˈtaɪni/","pos":"adj.","zh":"微小的","action":"大拇指和食指几乎相触，眯眼去看，\"So tiny I can barely see it！\""},
    ],

    patterns=[
        {"pattern":"Seeds grow into plants.","zh":"种子会长成植物","example":"This tiny seed will grow into a lovely strawberry plant."},
        {"pattern":"You'll have to be patient.","zh":"你得耐心等","example":"It will take a long time to grow. You'll have to be patient, Peppa."},
        {"pattern":"Everything grows from tiny seeds.","zh":"万物都从小种子长来","example":"Everything in my garden grows from tiny seeds like these."},
        {"pattern":"Inside this... are more seeds.","zh":"里面还有更多种子","example":"Inside this apple are more seeds — to make more apple trees."},
    ],

    goals={
        "min":"孩子能说出 3 个词（seed / grow / strawberry）",
        "mid":"孩子能用英文说一句：I planted a strawberry seed!",
        "ideal":"孩子主动用 <strong>\"You'll have to be patient\"</strong> 教家长",
    },

    phase1={
        "review_intro":"上集（第9集《Daddy Loses His Glasses》）孩子学过 <code>glasses</code>。用故意说错触发纠正：",
        "review_script":"\"上次 Daddy Pig 找不到眼镜，结果眼镜在哪里？在他的<u>口袋</u>里！\"（故意说错）",
        "review_response":"孩子一定会喊：\"不对！在他<strong>头上</strong>！（On his head！）\"家长：\"对！On his head all along！\"",
        "preview_intro":"家长蹲下来，假装在地上戳一个小洞，问孩子：",
        "preview_script":"\"Today — Grandpa Pig has a BIG secret in his garden. Something VERY. VERY. TINY... will turn into something you can EAT.\"（停顿，用手从地上慢慢站高，越变越大）",
        "preview_mission":"\"Your mission while watching: count how many things Grandpa Pig grows in his garden. Use your fingers. Ready? Go.\"",
    },

    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":"🌱","bg":"green","trigger":"Grandpa 解释种子怎么生长","action":"家长做出种种子的动作，手指插地，盖土，浇水，然后慢慢站起来"},
            {"emoji":"⏳","bg":"yellow","trigger":"Peppa 等待种子发芽","action":"家长夸张地做出等待的样子，看表，叹气，\"Still not growing...\""},
            {"emoji":"🍓","bg":"red","trigger":"草莓长出来了","action":"家长做出惊喜的样子，瞪大眼睛，捂嘴"},
        ],
    },

    phase3={
        "intro":"全程聊天，不是考试。家长读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":"\"So... did Peppa's strawberry seed actually grow? Yes or no?\"",
            "note":"家长做出等待的手势",
            "rows":[
                {"child":"\"Yes！\" / 点头","parent":"\"YES！ It grew！ From THIS tiny—\"（捏紧手指）\"—into a whole strawberry plant！ Amazing！\""},
                {"child":"\"No！\" / 摇头","parent":"（假装震惊）\"It didn't grow？！ Then what were those RED things Peppa ate？！\" 等孩子喊\"草莓！\""},
                {"child":"不说话","parent":"家长自己做出种种子 → 等待 → 惊喜发现草莓的全套动作，再问 \"Did it grow? YES or NO?\""},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":"\"Was Peppa patient... or did she want the strawberry RIGHT NOW？\"",
            "note":"\"patient\" 时做合十等待状；\"right now\" 时做急不可耐跺脚状",
            "rows":[
                {"child":"\"Right now！\"","parent":"\"Yes！ She wanted it immediately！ But plants can't grow IMMEDIATELY. You have to be...\" 等孩子补 \"patient\""},
                {"child":"\"Patient！\"","parent":"（夸张点头）\"She tried to be patient！ But it was SO hard！ Have YOU ever had to wait for something you really wanted？\""},
                {"child":"说中文","parent":"\"YES！ NOT patient！ She wanted strawberries for tea — TODAY！ <em>（Recast）</em> She wasn't very patient！\""},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":"\"If YOU could plant ONE thing in a garden... what would YOU grow？\"",
            "note":"指着孩子，等待",
            "rows":[
                {"child":"说水果/蔬菜","parent":"\"Ooh！ [水果]！ Do you know what the seed looks like？ THIS tiny？ And it becomes THAT big？！\""},
                {"child":"说零食/糖果","parent":"（假装惊喜）\"A candy tree！ I wish！ But we can only grow REAL things. What REAL thing？\""},
                {"child":"说恐龙树","parent":"（笑）\"Like George！ A dinosaur tree！ Hmm... but where would you find a dinosaur seed？ Grrr~\""},
                {"child":"不说话","parent":"\"OK. I would grow a CHOCOLATE tree. Can you grow chocolate？\" 等孩子笑着否定，再说 \"So what's your choice？\""},
            ],
        },
        "personal":{
            "intro":"把等待和耐心跟孩子的生活挂钩。",
            "script_lines":[
                "\"Have YOU ever waited for something REALLY REALLY long...\"",
                "（夸张叹气，来回踱步）",
                "\"...and it felt like it would NEVER come？\"",
            ],
            "rows":[
                {"child":"说等生日/圣诞","parent":"\"YES！ Waiting for your birthday feels like FOREVER！ That's exactly how Peppa felt about her strawberry！\""},
                {"child":"指家长","parent":"\"Me？ I wait for... （假装想）...for you to fall asleep so I can have peace and quiet.\" 自嘲耸肩"},
                {"child":"说等外卖/食物","parent":"\"Waiting for food is the HARDEST！ 'Are we there yet? Is it ready yet?' <strong>You'll have to be patient！</strong>\""},
                {"child":"不说话","parent":"\"No？ You've never waited for anything？ You're more patient than Daddy Pig！ Wow！\""},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演 Grandpa Pig，用第一人称说出本集词汇。",
            "script_lines":[
                "\"Excuse me！ Are you Grandpa Pig？\"",
                "\"I'm a reporter. Can I ask — what's growing in your garden today？\"",
            ],
            "rows":[
                {"child":"指植物 / 说 garden","parent":"\"Your garden！ What's growing in it？ Can you show me a seed？\""},
                {"child":"说 strawberry","parent":"\"A strawberry plant！ And how long did it take to grow？ Was it quick？\""},
                {"child":"说中文","parent":"家长自己扮演 Grandpa：\"I am Grandpa Pig. Everything in my garden grows from tiny seeds. Now YOU try！\""},
            ],
        },
        "recast":[
            {"child":"the seed <u>growed</u>","correct":"the seed <strong>grew</strong>！ It grew so well！","note":"不规则过去式 grew"},
            {"child":"I <u>putted</u> the seed","correct":"You <strong>put</strong> the seed！ Well done！","note":"put 过去式不变"},
            {"child":"it's <u>very tiny</u> seed","correct":"it's a <strong>very tiny</strong> seed！","note":"补充冠词 a"},
            {"child":"Grandpa <u>plant</u> flowers","correct":"Grandpa <strong>plants</strong> flowers！","note":"第三人称单数加 s"},
            {"child":"the strawberry <u>is</u> grow","correct":"the strawberry <strong>grew</strong>！ / is <strong>growing</strong>！","note":"时态统一"},
            {"child":"I <u>seed</u> it grow","correct":"I <strong>saw</strong> it grow！","note":"不规则过去式 saw"},
        ],
    },

    phase4={
        "tpr":[
            {"command":"\"Plant the seed!\"","action":"蹲下，手指戳地，假装埋种子，拍土盖住"},
            {"command":"\"Water the plant!\"","action":"手握想象的水壶，倾斜浇水，嘴里 \"Glug glug...\""},
            {"command":"\"Be patient! Wait for it to grow!\"","action":"双臂交叉，脚踩节拍，夸张地等，偷看，再等"},
            {"command":"\"Watch it grow！\"","action":"从蹲着慢慢站起，双臂逐渐展开，越变越高"},
            {"command":"\"Pick the strawberry!\"","action":"做出摘草莓的动作，放嘴里，\"Mmm！ Delicious！\""},
            {"command":"\"George wants a dinosaur tree!\"","action":"做出 T-Rex 的爪子，晃晃，困惑地四处张望，\"Where's my dinosaur seed？\""},
        ],
        "dubbing":[
            {"num":1,"time":"约第1分30秒","scene":"Grandpa Pig 把苹果切开，里面露出种子，解释种子→树的循环。",
             "l1":"Wow！","l1_note":"配上瞪眼惊喜表情","l2":"Seeds！ Inside！","l3":"\"Inside this apple are more seeds！ To make more apple trees！\""},
            {"num":2,"time":"约第2分钟","scene":"Peppa 亲手把草莓种子放进小洞，盖土，浇水。",
             "l1":"Grow！ Grow！","l1_note":"边说边做祈祷手势","l2":"I planted it！ Water it！","l3":"\"I made a little hole, put the seed in, and watered it！ Now we wait！\""},
            {"num":3,"time":"约第3分钟","scene":"Peppa 盯着地面，种子完全没动静，很失望。",
             "l1":"Hmph！","l1_note":"噘嘴，双手叉腰","l2":"Not growing！ Too slow！","l3":"\"It's not doing anything！ I want my strawberries for tea TODAY！\""},
            {"num":4,"time":"约第4分30秒","scene":"Peppa 再次来访，发现满满一串草莓！George 要求种恐龙。",
             "l1":"Strawberries！！","l1_note":"尖叫，蹦起来","l2":"They grew！ Wow！","l3":"\"They grew！ My strawberry plant grew！ — George, dinosaurs don't grow on trees！\""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"I just make a little hole and put the seed in... then I eat it.","answer":"COVER IT WITH EARTH！",
             "correct_line":"I just make a little hole, put the seed in, then I <strong>cover it with earth</strong> and water it."},
            {"num":2,"is_trap":False,
             "bug_line":"This tiny seed will grow into a lovely PIZZA plant.","answer":"STRAWBERRY！",
             "correct_line":"This tiny seed will grow into a lovely <strong>strawberry</strong> plant."},
            {"num":3,"is_trap":True,
             "bug_line":"You'll have to be patient, Peppa.","answer":"","correct_line":""},
            {"num":4,"is_trap":False,
             "bug_line":"Inside this apple are more SOCKS.","answer":"SEEDS！",
             "correct_line":"Inside this apple are more <strong>seeds</strong> — to make more apple trees."},
            {"num":5,"is_trap":False,
             "bug_line":"George wants to grow a BANANA tree.","answer":"DINOSAUR！",
             "correct_line":"George wants to grow a <strong>dinosaur</strong> tree."},
        ],
    },

    phase5={
        "l1":"Peppa 去 Grandpa 家. Grandpa plant strawberry seed. 然后 grow big！ Delicious！",
        "l1_response":"\"YES！ It grew！ And what did Peppa say — was she patient？ Or did she want it NOW？\"",
        "l2":"Peppa went to Grandpa Pig's house. Grandpa teach her plant a seed. She water it and wait. The strawberry grew！",
        "l2_response":"\"Great！ <em>（Recast）</em> Grandpa <strong>taught</strong> her. She watered it and waited — <strong>patiently</strong>！\"",
        "l3":"Peppa and George visited Grandpa Pig's garden. Grandpa showed Peppa how to plant a strawberry seed. She had to be patient — and when she came back, delicious strawberries had grown！",
        "l3_response":"\"PERFECT！ 'She had to be patient' — that's the key phrase！ You sound just like a little gardener！\"",
        "scaffold":[
            {"stuck":"第1句说不出来","rescue":"\"OK, first — where did they go？ Grand... pa... Pig's... <strong>gar-den</strong>...\" （做种植动作）"},
            {"stuck":"第2句说不出来","rescue":"\"Then Grandpa showed Peppa how to... <em>（做戳地洞的动作）</em>... plant a <strong>seed</strong>！\""},
            {"stuck":"第3句说不出来","rescue":"\"And they had to wait... and wait... and be <strong>pa-tient</strong>... until...\" （慢慢站起，展开双臂）"},
            {"stuck":"完全不开口","rescue":"家长先说 L1 版本，然后 \"Now YOU say it！ Copy me！ Just three words: seed, grow, strawberry！\""},
        ],
        "roleplay_child":"Peppa（种草莓的那个）",
        "roleplay_parent":"Grandpa Pig（教种植的那个）",
        "roleplay_situations":[
            {"label":"孩子假装戳洞","T_line":"\"You made a little hole！ Now what？ Put the... <strong>seed</strong> in！\""},
            {"label":"孩子做浇水动作","T_line":"\"Watering it！ Now what？ We have to be... <strong>patient</strong>！ Say it！\""},
            {"label":"孩子等了2秒就不耐烦","T_line":"\"Peppa！ <strong>You'll have to be patient！</strong> Say it with me！\""},
            {"label":"孩子假装发现草莓","T_line":"\"Strawberries！ Now say the whole thing — 'My strawberry grew！'\""},
        ],
    },

    phase6={
        "phonics_title":"规则：-ti- 让 /t/ 变成 /ʃ/",
        "phonics_word":"patient /ˈpeɪʃnt/",
        "phonics_mnemonic":"\"ti 遇到元音，t 变懒，说 /ʃ/——patient, nation, station, action！\"",
        "phonics_table":[
            {"word":"patient","wrong":"pa-TI-ent","right":"/ˈpeɪʃnt/","rule":"-tient → /ʃnt/"},
            {"word":"station","wrong":"sta-TI-on","right":"/ˈsteɪʃn/","rule":"-tion → /ʃn/"},
            {"word":"nation","wrong":"na-TI-on","right":"/ˈneɪʃn/","rule":"-tion → /ʃn/"},
            {"word":"action","wrong":"ac-TI-on","right":"/ˈækʃn/","rule":"-tion → /ʃn/"},
        ],
        "next_script":"\"Next time — George drinks his juice a little bit too fast... and something very funny happens to his body. Do you know what it is？\"",
        "next_a":"打嗝（Hiccups！）",
        "next_b":"打喷嚏",
    },

    checklist=[
        "Phase 1：孩子喊出了上集的词 glasses / on his head",
        "Phase 2：孩子自发做了种种子或浇水的动作",
        "Phase 3：孩子回答了至少1个问题（哪怕只说 strawberry）",
        "Phase 4：TPR 当过考官 + 配音每个画面说过至少 Level 1 + Bugs 少于 2 次扣分",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],

    ammo=[
        {"sentence":"You'll have to be patient！","zh":"你得耐心等","usage":"孩子等零食/等玩具/等去游乐场时"},
        {"sentence":"Everything grows from tiny seeds.","zh":"万物起于微小","usage":"孩子嫌弃自己学得慢时，鼓励他"},
        {"sentence":"Watch it grow！","zh":"看它慢慢长大","usage":"家里种了植物，每天观察时用"},
        {"sentence":"Inside this... are more seeds.","zh":"里面还有更多种子","usage":"切苹果、切西瓜时，引出循环的概念"},
    ],
)


# ═══════════════════════════════════════════════════════════════════════════════
# EP 11 · Hiccups 打嗝
# ═══════════════════════════════════════════════════════════════════════════════
EP11 = _ep(
    num=11, title_en="Hiccups", title_zh="打嗝", color="sky",
    synopsis="George 早餐喝果汁喝太快，打起了嗝。Peppa 先后用 三种偏方 试图治嗝：揉头+揉肚子、单脚跳+挥手+伸舌头、吓一跳——统统失败。Mummy 训Peppa玩太粗，打嗝反而神奇地停了。",

    vocab=[
        {"word":"hiccup","phonetic":"/ˈhɪkʌp/","pos":"n./v.","zh":"打嗝","action":"猛地把一口气憋回去，做出打嗝的动作和声音"},
        {"word":"cure","phonetic":"/kjʊə/","pos":"v./n.","zh":"治疗/疗法","action":"做出\"医生开药方\"的手势，神气地点头 \"I know the cure！\""},
        {"word":"quickly","phonetic":"/ˈkwɪkli/","pos":"adv.","zh":"很快地","action":"假装快速喝东西，然后立刻打嗝"},
        {"word":"shock","phonetic":"/ʃɒk/","pos":"n./v.","zh":"惊吓","action":"突然跳出来大喊 \"BOO！\" 吓对方"},
        {"word":"wriggle","phonetic":"/ˈrɪɡl/","pos":"v.","zh":"扭动","action":"全身扭来扭去，像虫子一样"},
        {"word":"roughly","phonetic":"/ˈrʌfli/","pos":"adv.","zh":"粗鲁地/粗野地","action":"故意夸张地做出捶打动作，然后摇头 \"Too rough！\""},
        {"word":"pretend","phonetic":"/prɪˈtend/","pos":"v.","zh":"假装","action":"双手做出引号姿势，眨眼 \"Just pretend！\""},
        {"word":"spoil","phonetic":"/spɔɪl/","pos":"v.","zh":"破坏","action":"做出一个很开心的游戏动作，然后突然 \"Hic！\"，摊手表示被毁了"},
    ],

    patterns=[
        {"pattern":"Don't drink too quickly.","zh":"别喝太快","example":"If you drink too quickly, you will get hiccups again."},
        {"pattern":"I know how to cure hiccups.","zh":"我知道怎么治打嗝","example":"George, I know how to cure hiccups. You have to do what I say."},
        {"pattern":"Remember, this is just pretend scaring.","zh":"记住，这只是假装在吓你","example":"I'm going to scare you. But you must remember, it's only a game."},
        {"pattern":"You mustn't play so roughly with George.","zh":"你不能跟George玩这么粗野","example":"He's only little."},
    ],

    goals={
        "min":"孩子能做出打嗝的动作并说 \"Hiccup！\"",
        "mid":"孩子能说一句治打嗝的方法（哪怕是搞笑的）",
        "ideal":"孩子主动用 <strong>\"Don't... too quickly\"</strong> 或 <strong>\"I know how to cure...\"</strong> 造句",
    },

    phase1={
        "review_intro":"上集（第10集《Gardening》）孩子学过 <code>patient</code> 和 <code>seed</code>。用故意说错触发纠正：",
        "review_script":"\"上次 Peppa 种了一颗种子，然后她非常<u>着急</u>，马上就等到草莓长出来了！\"（故意两处说错）",
        "review_response":"孩子会喊：\"不对！她很<strong>耐心</strong>（patient）！而且要等<strong>很多天</strong>！\"",
        "preview_intro":"家长假装快速大口喝东西，然后夸张地——",
        "preview_script":"\"Hic！ Hic！ Hic！\"（表情痛苦地打嗝）\"Today someone in the Pig family gets... THESE. And Peppa tries THREE different ways to make them stop. Which one do YOU think will work？\"",
        "preview_mission":"\"Your mission: count how many times Peppa tries to cure George's hiccups. Use your fingers！ Ready？ Go！\"",
    },

    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":"🥤","bg":"yellow","trigger":"George 喝果汁喝太快开始打嗝","action":"家长做出快速喝东西然后打嗝的动作，表情痛苦"},
            {"emoji":"🤸","bg":"purple","trigger":"Peppa 让 George 单脚跳+挥手+伸舌头","action":"家长真的单脚跳+挥手，越来越夸张，失去平衡"},
            {"emoji":"😱","bg":"orange","trigger":"Peppa 吓 George","action":"家长做出跳起来吓人的准备动作，然后假装被训，缩回去"},
        ],
    },

    phase3={
        "intro":"全程聊天，不是考试。家长读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":"\"So... did ANY of Peppa's cures actually work？ Yes or no？\"",
            "note":"",
            "rows":[
                {"child":"\"No！\"","parent":"\"NONE of them worked！ Zero！ The best cure was...\" （等孩子反应）\"...Mummy yelling at Peppa！ Ha！\""},
                {"child":"\"Yes！\"","parent":"（假装困惑）\"Which one worked？ The head-rubbing？ The jumping？ The SCARING？ Hmm...\"（等孩子说）"},
                {"child":"不说话","parent":"家长做出三种治法全套动作，最后说 \"Did ANY of them work？ YES or NO？\""},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":"\"Was Peppa trying to HELP George... or was she just having fun scaring him？\"",
            "note":"",
            "rows":[
                {"child":"\"帮他！\"","parent":"\"She was trying to help！ But her methods were a bit... CREATIVE. Like what？\""},
                {"child":"\"Scare him！\"","parent":"（笑）\"Well... she said it was just a GAME. 'This is just pretend scaring.' Do you believe her？\""},
                {"child":"两个都说","parent":"\"Exactly！ She was helping AND having fun — that's very Peppa of her！\""},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":"\"What would YOU do to cure someone's hiccups？\"",
            "note":"指着孩子",
            "rows":[
                {"child":"说喝水","parent":"\"Drink water！ Very sensible！ Does that always work？ Let's try...\"（假装喝，然后 \"Hic！\"）\"Hmm...\""},
                {"child":"说吓他","parent":"\"BOO！ Like Peppa！ But you have to say it's just pretend, right？ 'This is just <strong>pretend</strong> scaring！'\""},
                {"child":"说奇怪方法","parent":"（惊喜）\"Wow！ That's even more creative than Peppa！ I want to try this！\""},
                {"child":"不说话","parent":"\"OK, let me guess YOUR method...\" （然后做出超搞笑的假动作），\"You? Same or different？\""},
            ],
        },
        "personal":{
            "intro":"把打嗝和孩子的生活经验挂钩。",
            "script_lines":[
                "\"Have YOU ever had hiccups before？\"",
                "（做出打嗝动作，等孩子反应）",
                "\"And what did YOU do to make them stop？\"",
            ],
            "rows":[
                {"child":"说喝水/憋气","parent":"\"That's the classic！ Did it work？ Or did you go Hic！ Hic！ even after？\""},
                {"child":"说什么都没用","parent":"\"ME TOO！ Hiccups stop whenever they WANT to. Like George's！ Mummy just yelled and POOF — gone！\""},
                {"child":"说没有过","parent":"\"Lucky you！ But today, after watching George... you might catch them just from watching！ Hic！\" 假装打嗝"},
                {"child":"指家长打嗝","parent":"\"Me？ I hiccup in meetings. Very embarrassing. <strong>Don't drink too quickly</strong> — I need to remember that！\""},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演 George（打嗝者），家长扮演 Peppa（治疗者）。",
            "script_lines":[
                "\"Okay, YOU are George. YOU have hiccups.\"",
                "\"I am Peppa. I know EXACTLY how to cure hiccups. Ready？\"",
            ],
            "rows":[
                {"child":"配合打嗝","T_line":"\"Hic！ Perfect！ Now say 'Hic hic！' Try to make it sound really painful！\""},
                {"child":"做动作不说话","T_line":"\"Great acting！ Now add a sound！ 'Hic！' Go！\""},
                {"child":"笑场","T_line":"\"You laughed！ George would NOT laugh — he's very SAD about his hiccups！ Try again, but sadder！\""},
            ],
        },
        "recast":[
            {"child":"George <u>drink</u> too fast","correct":"George <strong>drank</strong> too fast！","note":"不规则过去式 drank"},
            {"child":"the hiccup <u>don't</u> stop","correct":"the hiccups <strong>didn't</strong> stop！","note":"助动词否定 didn't"},
            {"child":"Peppa <u>try</u> to cure","correct":"Peppa <strong>tried</strong> to cure！","note":"规则过去式 tried"},
            {"child":"it <u>is</u> work","correct":"it <strong>worked</strong>！ / it <strong>does</strong> work！","note":"时态"},
            {"child":"he <u>haved</u> hiccups","correct":"he <strong>had</strong> hiccups！","note":"不规则过去式 had"},
            {"child":"Mummy <u>shout</u> at Peppa","correct":"Mummy <strong>shouted</strong> at Peppa！","note":"规则过去式 shouted"},
        ],
    },

    phase4={
        "tpr":[
            {"command":"\"Drink your juice too quickly！\"","action":"仰头，假装快速大口喝，然后立刻 \"Hic！\"，表情痛苦"},
            {"command":"\"Rub the top of your head AND rub your tummy！\"","action":"一手头顶转圈，一手揉肚子，脸因为要协调两个动作而痛苦扭曲"},
            {"command":"\"Jump up and down three times on one leg！\"","action":"单脚夸张跳三次，边跳边数 \"One！ Two！ Three！\""},
            {"command":"\"Wave your arms and stick your tongue out！\"","action":"双臂疯狂挥舞，舌头伸出来，尽可能夸张"},
            {"command":"\"Close your eyes and turn around quickly three times！\"","action":"闭眼原地转三圈，睁眼后假装头晕"},
            {"command":"\"Give someone a SHOCK！ BOO！\"","action":"蹲下躲好，然后突然跳出来大喊 \"BOO！\""},
            {"command":"\"Hiccups are gone！ Yay！\"","action":"摊开双手，表情写着\"我也不知道为什么好了\"，然后欢呼"},
        ],
        "dubbing":[
            {"num":1,"time":"约第1分钟","scene":"Daddy Pig 警告 George 别喝太快，但 George 喝完立刻 \"Hic！\"",
             "l1":"Hic！","l1_note":"越夸张越好，配上痛苦表情","l2":"Too fast！ Hiccups！","l3":"\"Don't drink too quickly, George！ Now look — hiccups！\""},
            {"num":2,"time":"约第2分钟","scene":"Peppa 让 George 揉头揉肚子同时进行，George 完全乱了手脚。",
             "l1":"Huh？！","l1_note":"一脸懵逼","l2":"Too hard！ Confusing！","l3":"\"Rub your head AND your tummy at the same time？ That's impossible！\""},
            {"num":3,"time":"约第3分钟","scene":"Peppa 单脚跳+挥手+伸舌头，自己先做示范，越来越乱。",
             "l1":"Whoa！","l1_note":"做出将要跌倒的动作","l2":"Jump！ Wave！ Tongue！","l3":"\"Jump on one leg, wave your arms, AND stick your tongue out？ Easy！ Watch me！\""},
            {"num":4,"time":"约第4分30秒","scene":"Mummy 训了 Peppa 一顿，George 的打嗝神奇地消失了。",
             "l1":"Oh！","l1_note":"捂嘴，惊讶","l2":"Gone！ They stopped！","l3":"\"George's hiccups stopped！ But... how？ Maybe Mummy is the real cure！\""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"Daddy Pig: George！ Don't drink your SOUP too quickly.","answer":"JUICE！",
             "correct_line":"Don't drink your <strong>juice</strong> too quickly."},
            {"num":2,"is_trap":False,
             "bug_line":"Peppa: I know how to cure hiccups. You have to do... nothing.","answer":"WHAT I SAY！",
             "correct_line":"You have to do <strong>what I say</strong>."},
            {"num":3,"is_trap":True,
             "bug_line":"Remember, this is just pretend scaring.","answer":"","correct_line":""},
            {"num":4,"is_trap":False,
             "bug_line":"Peppa: I was just trying to stop George's SINGING.","answer":"HICCUPS！",
             "correct_line":"I was just trying to stop George's <strong>hiccups</strong>."},
            {"num":5,"is_trap":False,
             "bug_line":"Mummy Pig: If you drink too quickly, you will get SPOTS.","answer":"HICCUPS！",
             "correct_line":"If you drink too quickly, you will get <strong>hiccups</strong>."},
        ],
    },

    phase5={
        "l1":"George drink juice too fast. He get hiccups. Peppa try cure. Not work！ Then... gone！",
        "l1_response":"\"YES！ Gone！ Just like that！ And WHO cured them？ Was it Peppa？ Or was it...？\"",
        "l2":"George drank his juice too quickly and got hiccups. Peppa tried three cures but nothing worked. Then Mummy told Peppa off and the hiccups stopped！",
        "l2_response":"\"Great story！ <em>（Recast）</em> George <strong>drank</strong> his juice — and Peppa <strong>tried</strong> to cure them！ Funny ending！\"",
        "l3":"George had the hiccups after drinking juice too quickly. Peppa tried rubbing his head, jumping on one leg, and even scaring him — but nothing worked. Then Mummy scolded Peppa for being too rough, and George's hiccups magically disappeared！",
        "l3_response":"\"PERFECT！ 'Magically disappeared' — fantastic word！ You sound just like the Narrator！\"",
        "scaffold":[
            {"stuck":"第1句说不出来","rescue":"\"OK, so first... George drank his... <strong>jui-ce</strong>...\" （做喝东西动作，然后 \"Hic！\"）"},
            {"stuck":"第2句说不出来","rescue":"\"Then Peppa said 'I know how to... <strong>cure</strong>... hiccups！' Can you say cure？\""},
            {"stuck":"第3句说不出来","rescue":"\"And then Mummy... <em>（做出生气指责动作）</em>...and the hiccups just... <em>（做消失手势）</em>...\""},
            {"stuck":"完全不开口","rescue":"家长先说 L1 版本，\"Now YOU say it！ Just say: juice, hiccups, gone！\""},
        ],
        "roleplay_child":"George（有打嗝的那个）",
        "roleplay_parent":"Peppa（努力治疗的那个，说话不停）",
        "roleplay_situations":[
            {"label":"孩子假装打嗝","T_line":"\"Hic！ Poor George！ I know exactly what to do！ First, rub your head AND your tummy！\""},
            {"label":"孩子照做但很混乱","T_line":"\"Now jump on one leg！ Three times！ Wave your arms！ Stick your tongue out！\""},
            {"label":"孩子摔倒/乱了","T_line":"\"Are your hiccups gone？ No？ Don't worry, I have one more cure！ I'll SCARE you！\""},
            {"label":"孩子假装吓到","T_line":"\"BOO！ ... Are they gone？ Say 'Yes, they're gone！' or 'Hic！ Still here！'\""},
        ],
    },

    phase6={
        "phonics_title":"规则：-ck 组合，一个发音，加倍的力量",
        "phonics_word":"hiccup /ˈhɪkʌp/",
        "phonics_mnemonic":"\"c+k 合体 = 一个很强的 /k/ 音。hiccup 里的 cc 也发 /k/——两个字母，一个声音，很有力！\"",
        "phonics_table":[
            {"word":"hiccup","wrong":"hi-c-cup","right":"/ˈhɪkʌp/","rule":"cc → /k/"},
            {"word":"duck","wrong":"du-c-k","right":"/dʌk/","rule":"ck → /k/"},
            {"word":"quick","wrong":"qu-i-c-k","right":"/kwɪk/","rule":"ck → /k/"},
            {"word":"thick","wrong":"th-i-c-k","right":"/θɪk/","rule":"ck → /k/"},
        ],
        "next_script":"\"Next time — Peppa and George are going to RACE their bicycles. But wait — Peppa has training wheels and her friends don't. What do you think Peppa will do？\"",
        "next_a":"继续用辅助轮",
        "next_b":"拆掉辅助轮，学自己骑！",
    },

    checklist=[
        "Phase 1：孩子模仿了打嗝的动作或声音",
        "Phase 2：孩子跟着做了至少一种治打嗝的动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 当过考官 + 配音每个画面说过至少 Level 1 + Bugs 少于 2 次扣分",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],

    ammo=[
        {"sentence":"Don't drink too quickly！","zh":"别喝太快","usage":"孩子狂喝饮料时"},
        {"sentence":"I know how to cure...！","zh":"我知道怎么治……","usage":"孩子生病或不舒服时，让他用这句自信地说出\"解决方案\""},
        {"sentence":"This is just pretend scaring.","zh":"这只是假装在吓你","usage":"和孩子玩 BOO 游戏前，用来说明规则"},
        {"sentence":"You mustn't play so roughly.","zh":"你不能玩这么粗野","usage":"孩子玩耍太激烈，在他听懂之前先用英文说"},
    ],
)


# ═══════════════════════════════════════════════════════════════════════════════
# EP 12 · Bicycles 骑自行车
# ═══════════════════════════════════════════════════════════════════════════════
EP12 = _ep(
    num=12, title_en="Bicycles", title_zh="骑自行车", color="blue",
    synopsis="Peppa 的朋友们都不用辅助轮骑车了，只有她还装着。她鼓起勇气让爸爸拆掉辅助轮，摔了又摔，终于学会——然后一不注意压扁了爸爸精心培育的大南瓜。",

    vocab=[
        {"word":"stabilizer","phonetic":"/ˈsteɪbɪlaɪzə/","pos":"n.","zh":"辅助轮","action":"双手放在两侧，假装是自行车的小辅助轮，左右摇摆"},
        {"word":"pedal","phonetic":"/ˈpedl/","pos":"v.","zh":"踩踏板","action":"坐下，双脚交替做蹬自行车踏板的动作，越来越快"},
        {"word":"race","phonetic":"/reɪs/","pos":"n./v.","zh":"比赛","action":"做出起跑线弓步准备的姿势，大喊 \"Ready, steady, GO！\""},
        {"word":"squash","phonetic":"/skwɒʃ/","pos":"v.","zh":"压扁","action":"双手从高处往下猛地按，同时发出 \"SQUISH！\" 的声音"},
        {"word":"pumpkin","phonetic":"/ˈpʌmpkɪn/","pos":"n.","zh":"南瓜","action":"双手圈出一个又大又圆的形状，骄傲地说 \"My beautiful pumpkin！\""},
        {"word":"properly","phonetic":"/ˈprɒpəli/","pos":"adv.","zh":"正确地/像样地","action":"挺胸，整理仪态，用最正式的姿势做某件事"},
        {"word":"promise","phonetic":"/ˈprɒmɪs/","pos":"v./n.","zh":"承诺","action":"握拳放在胸口，郑重地点头 \"I promise.\""},
        {"word":"wobble","phonetic":"/ˈwɒbl/","pos":"v.","zh":"摇晃","action":"假装骑车时身体左右大幅度摇摆，表情惊恐"},
    ],

    patterns=[
        {"pattern":"I don't need my stabilizers anymore.","zh":"我不再需要辅助轮了","example":"Peppa: Look at me. I can ride my bike properly！"},
        {"pattern":"Don't let go, Daddy！","zh":"爸爸别松手！","example":"Peppa: Hold on, Daddy. Don't let go！"},
        {"pattern":"You've been cycling on your own for ages.","zh":"你已经自己骑了好一阵子了","example":"Daddy Pig: You've been cycling on your own for ages."},
        {"pattern":"You really must look where you're going.","zh":"你真的必须看你要去的地方","example":"Daddy Pig: In future, you really must look where you're going."},
    ],

    goals={
        "min":"孩子能模仿骑车动作并说 stabilizers 或 pedal",
        "mid":"孩子能用一句话说出故事的转折：Peppa squashed the pumpkin！",
        "ideal":"孩子主动用 <strong>\"Don't let go！\"</strong> 或 <strong>\"I can do it！\"</strong> 在角色扮演中大喊",
    },

    phase1={
        "review_intro":"上集（第11集《Hiccups》）孩子学过 <code>hiccup</code> 和 <code>cure</code>。用故意说错触发：",
        "review_script":"\"上次 George 打嗝，Peppa 的三种治法全部成功了！\"（两处故意说错）",
        "review_response":"孩子会喊：\"不对！全部<strong>失败</strong>了！是Mummy训了Peppa才停的！\"",
        "preview_intro":"家长假装骑车，然后夸张地摇摇晃晃，差点摔倒——",
        "preview_script":"\"Today Peppa's friends can all ride their bikes like THIS—\" （流畅地骑）\"But Peppa still rides like... THIS！\" （摇晃，辅助轮拖地）\"She has to make a BIG decision. What do you think she does？\"",
        "preview_mission":"\"Your mission: watch how many times Peppa wobbles or falls！ Count on your fingers！\"",
    },

    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":"🚲","bg":"blue","trigger":"Peppa 看到朋友们不用辅助轮骑车","action":"家长做出羡慕的表情，偷偷看别人的车，再看自己的"},
            {"emoji":"😱","bg":"red","trigger":"Peppa 摔倒","action":"家长夸张地捂脸，做出 \"Oh no！\" 的表情，但不说话"},
            {"emoji":"🎉","bg":"green","trigger":"Peppa 成功自己骑车了","action":"家长悄悄做出鼓掌的动作，偷偷瞄孩子的反应"},
        ],
    },

    phase3={
        "intro":"全程聊天，不是考试。家长读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":"\"So... did Peppa learn to ride without stabilizers？ YES or NO？\"",
            "note":"",
            "rows":[
                {"child":"\"Yes！\"","parent":"\"YES！ She did it！ But it wasn't easy！ She fell how many times？ Count with me...\""},
                {"child":"\"No！\"","parent":"（假装震惊）\"She didn't learn？ Then how did she ride to the pumpkin... and SQUASH it？！\""},
                {"child":"不说话","parent":"家长做全套：装辅助轮 → 摔 → 爬起 → 最终骑走，问 \"Did she learn？ YES or NO？\""},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":"\"Was Daddy Pig helpful... or was he a bit too confident？\"",
            "note":"\"helpful\" 时做大拇指；\"too confident\" 时做出 Daddy Pig 挺胸的自夸动作",
            "rows":[
                {"child":"\"Helpful！\"","parent":"\"He was helpful！ He held the bike and let go at the right moment！ Smart！\""},
                {"child":"\"Too confident！\"","parent":"（笑）\"Well... he also said 'I know what I'm doing' right before getting stuck in a tree... wait, that's next episode！ Ha！\""},
                {"child":"两个都","parent":"\"Both！ Exactly！ He helped AND he was overconfident. That's VERY Daddy Pig！\""},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":"\"Have YOU ever tried to learn something really hard？ And what happened？\"",
            "note":"",
            "rows":[
                {"child":"说骑车/滑板/游泳","parent":"\"Just like Peppa！ Did you fall？ And did you want to give up？ But you didn't！ Right？！\""},
                {"child":"说学习某个技能","parent":"\"YES！ It's hard at first！ But then one day... click！ You've got it！ Like Peppa！\""},
                {"child":"说什么都不会","parent":"（假装震惊）\"Nothing is hard for you？ You never fell？ You are better than Peppa at everything！ Wow！\""},
                {"child":"说骑车还在学","parent":"\"YOU are learning too！ Just like Peppa！ 'Don't let go, Daddy!' — remember that feeling？\""},
            ],
        },
        "personal":{
            "intro":"把学骑车的经历和坚持不放弃的主题挂钩。",
            "script_lines":[
                "\"When Daddy Pig said 'I've got you' and then LET GO...\"",
                "（做出放手后孩子突然自己骑走的惊喜动作）",
                "\"...how do you think Peppa FELT？\"",
            ],
            "rows":[
                {"child":"说害怕","parent":"\"Scared！ But she kept pedalling！ And then she realized — 'I'M DOING IT！'\""},
                {"child":"说惊喜/开心","parent":"\"SURPRISED！ And proud！ 'Look at me！ I can ride properly！' — she was SO proud！\""},
                {"child":"说被骗了","parent":"\"Ha！ She felt a bit tricked！ But Daddy was smart — if he told her, she might have stopped！\""},
                {"child":"不说话","parent":"\"Let me show you what I THINK she felt...\" （做出先恐慌后惊喜转变的两段表情）\"Which one？\""},
            ],
        },
        "role_play":{
            "intro":"孩子扮演 Peppa 学骑车，家长扮演 Daddy Pig。",
            "script_lines":[
                "\"YOU are Peppa. YOU are learning to ride.",
                "\"I am Daddy Pig. I am VERY good at this. Ready, steady, GO！\"",
            ],
            "rows":[
                {"child":"假装骑车","T_line":"\"Keep pedalling！ Don't stop！ And say 'Don't let go, Daddy！'\""},
                {"child":"假装摔倒","T_line":"\"You fell！ But that's OK！ Say 'I'm OK！ Let's try again！'\""},
                {"child":"成功骑了","T_line":"\"You did it！ Say 'I can do it！ Look at me！' Really loud！\""},
            ],
        },
        "recast":[
            {"child":"Peppa <u>falled</u> off","correct":"Peppa <strong>fell</strong> off！","note":"不规则过去式 fell"},
            {"child":"she <u>taked</u> off the stabilizers","correct":"she <strong>took</strong> off the stabilizers！","note":"不规则过去式 took"},
            {"child":"Daddy <u>holded</u> the bike","correct":"Daddy <strong>held</strong> the bike！","note":"不规则过去式 held"},
            {"child":"she <u>squash</u> the pumpkin","correct":"she <strong>squashed</strong> the pumpkin！","note":"规则过去式 squashed"},
            {"child":"I can <u>ride</u> bike","correct":"I can ride <strong>a</strong> bike！","note":"补充冠词 a"},
            {"child":"Peppa <u>learn</u> quickly","correct":"Peppa <strong>learned</strong> quickly！","note":"规则过去式 learned"},
        ],
    },

    phase4={
        "tpr":[
            {"command":"\"Ride your bike with stabilizers！\"","action":"假装骑车，双手左右大幅摇摆，辅助轮刮地，\"Clang clang！\""},
            {"command":"\"Take the stabilizers OFF！\"","action":"蹲下，假装拧螺丝，把想象中的辅助轮拆下来，扔一边"},
            {"command":"\"Ready, steady, GO！\"","action":"弓腿做起跑姿势，大声喊 \"Ready, steady, GO！\" 然后原地快速蹬腿"},
            {"command":"\"Wobble！ Don't fall！\"","action":"大幅摇晃，差点倒，用力保持平衡，表情惊恐"},
            {"command":"\"Keep pedalling！ Don't stop！\"","action":"加速蹬腿动作，越来越快，同时大喊 \"Don't stop！ Don't stop！\""},
            {"command":"\"Watch out for the pumpkin！\"","action":"做出 Daddy Pig 惊慌的表情，大喊 \"PEPPA！ MY PUMPKIN！\""},
            {"command":"\"SQUASH！ Oh no！\"","action":"双手重重往下按，同时喊 \"SQUISH！\"，然后双手捂脸，悲痛"},
        ],
        "dubbing":[
            {"num":1,"time":"约第1分30秒","scene":"Danny、Suzy、Rebecca 都不用辅助轮，Peppa 看着自己的车，小声嫌弃辅助轮。",
             "l1":"Hmph！","l1_note":"噘嘴，低头看自己的车","l2":"Baby wheels！ So embarrassing！","l3":"\"I don't want stabilizers anymore！ They make me look like a baby！\""},
            {"num":2,"time":"约第3分钟","scene":"Daddy Pig 帮 Peppa 推车，Peppa 死死拽着 Daddy 的手，生怕他放开。",
             "l1":"Don't let go！","l1_note":"表情极度紧张","l2":"Hold on！ I'll fall！","l3":"\"Don't you DARE let go, Daddy Pig！ I am NOT ready！\""},
            {"num":3,"time":"约第4分钟","scene":"Peppa 突然意识到自己已经独立骑了好一会儿了，惊讶。",
             "l1":"Wait...！","l1_note":"停下来，四处张望","l2":"I'm doing it！ Alone！","l3":"\"Daddy let go！ And I'm... I'm RIDING！ By myself！ I CAN DO IT！\""},
            {"num":4,"time":"约第5分钟","scene":"Peppa 得意忘形，眼睛不看路，直接压进爸爸的南瓜。",
             "l1":"Oops！","l1_note":"捂嘴，做破坏后的无辜表情","l2":"I squashed it！ Sorry Daddy！","l3":"\"I'm so sorry Daddy！ I forgot to look where I was going！ At least the pumpkin makes good pie？\""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"Peppa: I don't want TRAINING WHEELS anymore. （stabilizers 说成了 training wheels）","answer":"STABILIZERS！",
             "correct_line":"I don't want <strong>stabilizers</strong> anymore."},
            {"num":2,"is_trap":False,
             "bug_line":"Daddy Pig: All right. Let's take them off. Are you SURE sure SURE？","answer":"（只是三个 sure！原文只有一个 sure）... 实际题目：",
             "correct_line":""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"Daddy Pig: Pumpkins are the only thing I can grow. Probably because I love pumpkin SOUP.","answer":"PIE！",
             "correct_line":"Probably because I love pumpkin <strong>pie</strong>."},
            {"num":2,"is_trap":False,
             "bug_line":"Peppa: George is riding a baby SCOOTER.","answer":"BIKE / TRICYCLE！",
             "correct_line":"George is still riding a baby <strong>tricycle</strong>."},
            {"num":3,"is_trap":True,
             "bug_line":"You really must look where you're going.","answer":"","correct_line":""},
            {"num":4,"is_trap":False,
             "bug_line":"Daddy Pig: You've been cycling on your own for HOURS.","answer":"AGES！",
             "correct_line":"You've been cycling on your own for <strong>ages</strong>."},
            {"num":5,"is_trap":False,
             "bug_line":"Peppa: I'm going to WIN. Wheeee! （然后 squash 了爸爸的...） I squashed the MELON！","answer":"PUMPKIN！",
             "correct_line":"Oh no, I squashed Daddy's <strong>pumpkin</strong>！"},
        ],
    },

    phase5={
        "l1":"Peppa take off stabilizers. She wobble and fall. Then she ride！ But she squash the pumpkin！",
        "l1_response":"\"YES！ She squashed it！ Was Daddy Pig sad？ Or did he make...？\" 等孩子补 \"pumpkin pie！\"",
        "l2":"Peppa's friends could ride without stabilizers. Peppa took hers off too. She fell a few times but then she did it！ But she squashed Daddy's pumpkin by accident.",
        "l2_response":"\"Great！ <em>（Recast）</em> She <strong>fell</strong> a few times — past tense！ And she <strong>squashed</strong> it by accident！\"",
        "l3":"All of Peppa's friends could ride their bikes without stabilizers. Peppa asked Daddy to take hers off too. After many falls, she finally did it — she could ride on her own！ But in her excitement, she wasn't looking and squashed Daddy Pig's prized pumpkin.",
        "l3_response":"\"PERFECT！ 'Prized pumpkin' — great adjective！ Daddy Pig's most beloved, precious pumpkin... squashed！ Poor Daddy！\"",
        "scaffold":[
            {"stuck":"第1句说不出来","rescue":"\"OK, what did Peppa ask Daddy to take off？ Sta... bi... li... <strong>zers</strong>！ Her stabilizers！\""},
            {"stuck":"第2句说不出来","rescue":"\"Then Daddy held the bike and let go... and Peppa was... <em>（做骑车动作）</em>... riding！ On her <strong>own</strong>！\""},
            {"stuck":"第3句说不出来","rescue":"\"But she wasn't looking, and she... <em>（做压扁手势，SQUISH！）</em>... the pumpkin！\""},
            {"stuck":"完全不开口","rescue":"家长先说 L1，\"Now YOU say it！ Three words: stabilizers, ride, squash！\""},
        ],
        "roleplay_child":"Peppa（学骑车的那个）",
        "roleplay_parent":"Daddy Pig（帮忙推车的那个）",
        "roleplay_situations":[
            {"label":"孩子假装骑车很稳","T_line":"\"Wow！ You're doing it！ Say 'I can do it！ I'm riding！'\""},
            {"label":"孩子假装摇晃","T_line":"\"Wobbling！ Don't fall！ Say 'Don't let go, Daddy！'\""},
            {"label":"孩子假装撞到东西","T_line":"\"You squashed... my... PUMPKIN！ Say 'Sorry Daddy！ I'll make it into pie！'\""},
        ],
    },

    phase6={
        "phonics_title":"规则：magic-e 让元音变长",
        "phonics_word":"ride /raɪd/ vs rid /rɪd/",
        "phonics_mnemonic":"\"最后加个 e，前面的元音变长，说自己的字母名。ride 里的 'i' 说 /aɪ/，不加 e 就是 rid /ɪ/——完全不一样！\"",
        "phonics_table":[
            {"word":"ride","wrong":"rid（无e）","right":"/raɪd/","rule":"i+e → /aɪ/"},
            {"word":"bike","wrong":"bik（无e）","right":"/baɪk/","rule":"i+e → /aɪ/"},
            {"word":"race","wrong":"rac（无e）","right":"/reɪs/","rule":"a+e → /eɪ/"},
            {"word":"wobble","wrong":"有2个b","right":"/ˈwɒbl/","rule":"双写辅音保持短元音"},
        ],
        "next_script":"\"Next time — Mummy Pig makes a very special box for Peppa. And only Peppa knows what's inside. What do you think she puts in it？\"",
        "next_a":"玩具",
        "next_b":"秘密的东西（Secret things！）",
    },

    checklist=[
        "Phase 1：孩子喊出了上集的词 hiccup / cure",
        "Phase 2：孩子自发做了骑车的动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 当过考官 + 配音每个画面说过至少 Level 1 + Bugs 少于 2 次扣分",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],

    ammo=[
        {"sentence":"Don't let go！","zh":"别松手！","usage":"孩子学任何新技能时，紧张地抓着大人"},
        {"sentence":"You've been doing it on your own for ages！","zh":"你已经自己做了好一阵子了","usage":"孩子以为大人在帮他，其实已经独立完成了某件事"},
        {"sentence":"You really must look where you're going.","zh":"你真的要看路","usage":"孩子低头玩手机/游戏走路撞到东西时"},
        {"sentence":"Never mind. The important thing is you're okay.","zh":"没关系，重要的是你没事","usage":"孩子磕到/摔到时，先这么说"},
    ],
)


# ═══════════════════════════════════════════════════════════════════════════════
# EP 13 · Secrets 秘密
# ═══════════════════════════════════════════════════════════════════════════════
EP13 = _ep(
    num=13, title_en="Secrets", title_zh="秘密", color="purple",
    synopsis="Mummy 给 Peppa 做了一个秘密盒子，让她装自己的秘密。Peppa 让 George 和 Daddy 来猜里面有什么，两个人都没猜中。Mummy 也给 George 做了一个——只有 George 自己知道里面有什么。",

    vocab=[
        {"word":"secret","phonetic":"/ˈsiːkrɪt/","pos":"n./adj.","zh":"秘密","action":"食指放嘴唇上 \"Shhhh！\" 同时左右张望，确认没人"},
        {"word":"empty","phonetic":"/ˈempti/","pos":"adj.","zh":"空的","action":"把手张开，翻转朝下，表示什么都没有，\"Nothing inside！\""},
        {"word":"guess","phonetic":"/ɡes/","pos":"v.","zh":"猜","action":"皱眉，手托下巴，做思考状，\"Hmm... let me guess...\""},
        {"word":"decide","phonetic":"/dɪˈsaɪd/","pos":"v.","zh":"决定","action":"先做两难选择的犹豫动作，然后猛地拍大腿，\"I've decided！\""},
        {"word":"proper","phonetic":"/ˈprɒpə/","pos":"adj.","zh":"正经的/像样的","action":"挺直腰，摆出正经的姿势，用严肃的声音说 \"A proper guess！\""},
        {"word":"fill","phonetic":"/fɪl/","pos":"v.","zh":"装满","action":"假装往一个盒子里放东西，越装越多，满了！"},
        {"word":"detective","phonetic":"/dɪˈtektɪv/","pos":"n.","zh":"侦探","action":"戴上想象的侦探帽，放大镜举起来，用夸张的声音 \"Elementary！\""},
        {"word":"discover","phonetic":"/dɪˈskʌvə/","pos":"v.","zh":"发现","action":"慢慢揭开想象的布，大喊 \"I discovered it！\""},
    ],

    patterns=[
        {"pattern":"Only you can decide that.","zh":"只有你能决定这件事","example":"It's your secret box. Only you can decide what goes inside."},
        {"pattern":"It's a secret！","zh":"这是秘密！","example":"Don't tell me. Don't tell George or Daddy. It's a secret."},
        {"pattern":"That's all your guesses. Used up！","zh":"你的猜测机会用完了","example":"Peppa: Nope. And that's all your guesses. Used up！"},
        {"pattern":"Can I have a try？","zh":"我可以试试吗？","example":"Daddy Pig: Can I have a try？ Hmm, have you put my glasses inside？"},
    ],

    goals={
        "min":"孩子能说 \"It's a secret！\" 并做出 Shhhh 的动作",
        "mid":"孩子能用英文说一句猜测：I think it's a...！",
        "ideal":"孩子主动用 <strong>\"Only you can decide\"</strong> 或 <strong>\"That's all your guesses. Used up！\"</strong>",
    },

    phase1={
        "review_intro":"上集（第12集《Bicycles》）孩子学过 <code>stabilizer</code>。用故意说错触发：",
        "review_script":"\"上次 Peppa 学骑车，她拆掉了辅助轮，最后骑得非常好，什么都没破坏！\"（最后一句故意说错）",
        "review_response":"孩子会喊：\"不对！她压扁了爸爸的<strong>南瓜</strong>（pumpkin）！\"",
        "preview_intro":"家长神神秘秘地拿出一个盒子（或假装有一个盒子），做出 Shhhh 的动作——",
        "preview_script":"\"Today — Peppa has a VERY special box. She fills it with secret things. And... absolutely nobody is allowed to know what's inside. <em>（把盒子藏到身后，摆出 Shhhh 手势）</em>\"",
        "preview_mission":"\"Your mission while watching: guess what Peppa puts in the secret box. And see if YOU are right！\"",
    },

    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":"📦","bg":"purple","trigger":"Mummy 把神秘的盒子拿给 Peppa","action":"家长做出接过礼物时慎重又好奇的表情，假装小心翼翼地打开"},
            {"emoji":"🤔","bg":"yellow","trigger":"George 和 Daddy 猜不出盒子里有什么","action":"家长做出认真思考的样子，皱眉，手托下巴，然后耸肩 \"I give up！\""},
            {"emoji":"🤫","bg":"pink","trigger":"George 的秘密盒子出现","action":"家长做出惊讶的表情，指向 George，\"He has one too？！\""},
        ],
    },

    phase3={
        "intro":"全程聊天，不是考试。家长读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":"\"So... did Daddy Pig guess what was inside Peppa's box？ YES or NO？\"",
            "note":"",
            "rows":[
                {"child":"\"No！\"","parent":"\"NO！ He guessed his glasses... which were ON HIS HEAD！ Silly Daddy！ And then what did Peppa say？ 'That's all your guesses... ' — what？\""},
                {"child":"\"Yes！\"","parent":"（震惊）\"He guessed right？！ How？ What did he guess？ Was it...？\" （等孩子说）"},
                {"child":"不说话","parent":"家长做出 Daddy Pig 猜测两次都猜错的动作，表情越来越懊恼，然后 \"Did he guess right？ YES or NO？\""},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":"\"Was Peppa good at keeping secrets... or did she tell EVERYONE？\"",
            "note":"",
            "rows":[
                {"child":"\"Good！\"","parent":"\"She kept the secret！ She didn't even tell George！ Do YOU have any secrets？\""},
                {"child":"\"Tell everyone！\"","parent":"（假装思考）\"Hmm... she did tell George it was 'empty'... and she told Daddy there was 'something inside'... Is that a hint？\""},
                {"child":"说中文","parent":"\"She kept the secret pretty well！ <em>（Recast）</em> She was <strong>good at keeping</strong> her secret！\""},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":"\"If YOU had a secret box, what would YOU put inside it？\"",
            "note":"指着孩子",
            "rows":[
                {"child":"说小玩具/贴纸","parent":"\"Stickers！ Or toys！ Good idea！ And would you let ME see？ <em>（做出乞求的眼神）</em> Please？\""},
                {"child":"说大东西","parent":"（假装很认真）\"But... would a car/dinosaur/pizza FIT inside the box？ Hmm...\""},
                {"child":"说秘密/隐私","parent":"\"Oh！ Your REAL secrets！ Like diary things？ <strong>Only you can decide</strong> what goes inside！\""},
                {"child":"说不知道","parent":"\"OK, I'll tell you MY secret box... （故作神秘停顿）...it's full of CHOCOLATE. But that's a secret. Don't tell Mummy.\""},
            ],
        },
        "personal":{
            "intro":"把秘密和孩子自己的生活挂钩。",
            "script_lines":[
                "\"Have you ever had a SECRET？\"",
                "（做出 Shhhh 手势，压低声音）",
                "\"And did you manage to keep it？ Or did it... slip out？\"",
            ],
            "rows":[
                {"child":"说有秘密","parent":"\"Oh！ What kind？ Something GOOD... or something a bit naughty？ <em>（眨眼）</em>\""},
                {"child":"说没有","parent":"\"No secrets？ Never？ You've never hidden anything from anyone？ You're the most honest person I know！\""},
                {"child":"笑着不说","parent":"\"You're keeping a secret right NOW！ I can see it on your face！ <strong>It's a secret</strong>！ I get it！\""},
                {"child":"说告诉了别人","parent":"\"Aha！ You spilled the secret！ That's so hard to keep in！ Was the other person surprised？\""},
            ],
        },
        "role_play":{
            "intro":"孩子扮演 Peppa（有秘密盒子），家长扮演 Daddy Pig（想猜出来）。",
            "script_lines":[
                "\"Peppa！ I hear you have a SECRET box！\"",
                "\"Can I have a try？ I'm very good at guessing！\"",
            ],
            "rows":[
                {"child":"说 \"It's a secret！\"","T_line":"\"A secret！ But can I have just ONE guess？ Please？ I think it's... your shoes！\""},
                {"child":"说 \"No！ Wrong！\"","T_line":"\"Oh dear！ One more！ Is it... Mummy's hat？\""},
                {"child":"说 \"That's all your guesses！ Used up！\"","T_line":"\"Used up？ Already？ Oh. That is very Peppa. Very correct. Well done！\""},
            ],
        },
        "recast":[
            {"child":"she <u>putted</u> things inside","correct":"she <strong>put</strong> things inside！","note":"put 过去式不变"},
            {"child":"Daddy <u>can't</u> guess it","correct":"Daddy <strong>couldn't</strong> guess it！","note":"过去式 couldn't"},
            {"child":"it's a <u>secret thing</u>","correct":"it's a <strong>secret</strong>！","note":"secret 本身就是名词，不需要 thing"},
            {"child":"Mummy <u>make</u> a box","correct":"Mummy <strong>made</strong> a box！","note":"不规则过去式 made"},
            {"child":"George <u>don't</u> know","correct":"George <strong>doesn't</strong> know！","note":"第三人称单数"},
        ],
    },

    phase4={
        "tpr":[
            {"command":"\"Shhh！ It's a secret！\"","action":"食指贴嘴唇，左右张望，蹑手蹑脚，压低声音"},
            {"command":"\"Fill the box with secret things！\"","action":"假装往盒子里放东西，越来越多，最后关上，\"All full！\""},
            {"command":"\"Make a proper guess！\"","action":"挺直腰，用夸张的侦探语气，\"My guess is... THE GLASSES WERE ON YOUR HEAD ALL ALONG！\""},
            {"command":"\"That's all your guesses！ Used up！\"","action":"两只手做出\"时间到\"的动作，摊开双手，\"No more guesses for you！\""},
            {"command":"\"Don't tell me！ It's a secret！\"","action":"用双手捂住自己的耳朵，\"La la la, I can't hear you！ I don't want to know！\""},
            {"command":"\"George has a secret too！\"","action":"做出惊讶的表情，蹲下来看想象中的 George 的盒子，\"What's inside, George？\""},
        ],
        "dubbing":[
            {"num":1,"time":"约第1分钟","scene":"Mummy 把神秘盒子交给 Peppa，说这是她的秘密盒子，让她自己决定装什么。",
             "l1":"Ooh！","l1_note":"小心翼翼接过盒子，双眼发光","l2":"My box！ Secret box！","l3":"\"My secret box！ Only I can decide what goes inside！ And nobody is allowed to look！\""},
            {"num":2,"time":"约第2分30秒","scene":"Daddy Pig 猜测盒子里是他的眼镜，Peppa 指出眼镜就在他头上。",
             "l1":"（做指头顶的动作）","l1_note":"指着 Daddy 的头，一脸无奈","l2":"Glasses on head！ Silly！","l3":"\"Daddy！ Your glasses are on your head！ That's not a proper guess！\""},
            {"num":3,"time":"约第3分钟","scene":"Daddy 用完了猜测机会，Peppa 郑重宣告。",
             "l1":"Used up！","l1_note":"做出手势像关门","l2":"No more guesses！ Done！","l3":"\"That's ALL your guesses！ Used up！ You'll never know what's inside！ Ha！\""},
            {"num":4,"time":"约第4分30秒","scene":"Mummy 拿出 George 的秘密盒子——George 也有一个！里面只有 George 知道。",
             "l1":"Wow！","l1_note":"惊讶，因为连 Peppa 也不知道","l2":"George has one！ What's inside？","l3":"\"George has a secret box too！ And only GEORGE knows what's inside！ What is it, George？ Grrr！\""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"Mummy Pig: It's a secret box for you to keep secret FOOD in.","answer":"THINGS！",
             "correct_line":"It's a secret box for you to keep secret <strong>things</strong> in."},
            {"num":2,"is_trap":False,
             "bug_line":"Daddy Pig: Have you put Mummy's RING inside？","answer":"SHOES！",
             "correct_line":"Have you put Mummy's <strong>shoes</strong> inside？"},
            {"num":3,"is_trap":True,
             "bug_line":"Only you can decide that, Peppa.","answer":"","correct_line":""},
            {"num":4,"is_trap":False,
             "bug_line":"Peppa: Nope. And that's all your guesses. WASTED！","answer":"USED UP！",
             "correct_line":"That's all your guesses. <strong>Used up</strong>！"},
            {"num":5,"is_trap":False,
             "bug_line":"Peppa: George, this is my secret box. It's FULL. I have to find some things to put inside.","answer":"EMPTY！",
             "correct_line":"It's <strong>empty</strong>. I have to find some things to put inside."},
        ],
    },

    phase5={
        "l1":"Mummy give Peppa a box. It's for secrets. Daddy try guess. He can't！ George have secret box too！",
        "l1_response":"\"YES！ Even George！ And do you know what's inside George's box？ Nobody knows！ Except...？\"",
        "l2":"Mummy Pig made a special secret box for Peppa. Peppa filled it with secret things. Daddy tried to guess but he used up all his guesses. Then Mummy made one for George too！",
        "l2_response":"\"Great！ <em>（Recast）</em> Peppa <strong>filled</strong> it — past tense！ And Daddy <strong>used up</strong> all his guesses！\"",
        "l3":"Mummy Pig made Peppa a secret box and told her only she could decide what to put inside. Peppa let George and Daddy guess, but neither one got it right. Then Mummy surprised everyone — she'd made George his own secret box too, and only George knows what's inside！",
        "l3_response":"\"PERFECT！ 'Only she could decide' — beautiful！ And 'neither one got it right' — brilliant！\"",
        "scaffold":[
            {"stuck":"第1句说不出来","rescue":"\"OK, what did Mummy give Peppa？ A... secret... <strong>box</strong>！ Say it！\""},
            {"stuck":"第2句说不出来","rescue":"\"Then Daddy tried to... <strong>guess</strong>... what was inside！ Did he get it right？\""},
            {"stuck":"第3句说不出来","rescue":"\"And at the end... George had a secret box TOO！ Only <strong>George</strong> knows！\""},
            {"stuck":"完全不开口","rescue":"家长先说 L1，\"Now YOU say it！ Just three words: box, secret, guess！\""},
        ],
        "roleplay_child":"Peppa（有秘密盒子的那个）",
        "roleplay_parent":"Daddy Pig（想猜出来的那个）",
        "roleplay_situations":[
            {"label":"孩子抱着想象的盒子","T_line":"\"Is that your SECRET box？ Can I see inside？ Please？ I'll be very careful！\""},
            {"label":"孩子摇头说不行","T_line":"\"Please！ Just ONE peek？ I guess it's... my glasses？ No？ Mummy's shoes？\""},
            {"label":"孩子说 Used up","T_line":"\"All used up？ Already？ That is very Peppa of you. Well done！ Can you say the whole thing：'That's all your guesses. Used up！'\""},
        ],
    },

    phase6={
        "phonics_title":"规则：'ea' 的两种读法",
        "phonics_word":"secret /ˈsiːkrɪt/ → 'e' 发长音",
        "phonics_mnemonic":"\"'ea' 最常见读 /iː/（speak, clean, read），但有时候很任性读 /e/（head, bread, dead）——英语就是这么调皮！\"",
        "phonics_table":[
            {"word":"clean","wrong":"clen","right":"/kliːn/","rule":"ea → /iː/"},
            {"word":"speak","wrong":"spek","right":"/spiːk/","rule":"ea → /iː/"},
            {"word":"head","wrong":"heed","right":"/hed/","rule":"ea → /e/（任性版）"},
            {"word":"bread","wrong":"breed","right":"/bred/","rule":"ea → /e/（任性版）"},
        ],
        "next_script":"\"Next time — Peppa and George go to the park with Daddy, and they try to fly something in the sky. But it won't go up！ What do you think is missing？\"",
        "next_a":"翅膀",
        "next_b":"Wind！ 风！",
    },

    checklist=[
        "Phase 1：孩子喊出了上集的词 stabilizer / squash / pumpkin",
        "Phase 2：孩子做出了 Shhhh 的保密动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 当过考官 + 配音每个画面说过至少 Level 1 + Bugs 少于 2 次扣分",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],

    ammo=[
        {"sentence":"It's a secret！","zh":"这是秘密！","usage":"和孩子玩惊喜游戏时"},
        {"sentence":"Only you can decide that.","zh":"只有你能决定这件事","usage":"孩子纠结选择时，给他自主权"},
        {"sentence":"That's all your guesses. Used up！","zh":"你的猜测机会用完了","usage":"家里玩猜谜游戏，机会用完时宣布"},
        {"sentence":"Can I have a try？","zh":"我可以试试吗？","usage":"请求机会的礼貌表达"},
    ],
)


# ═══════════════════════════════════════════════════════════════════════════════
# EP 14 · Flying a Kite 放风筝
# ═══════════════════════════════════════════════════════════════════════════════
EP14 = _ep(
    num=14, title_en="Flying a Kite", title_zh="放风筝", color="sky",
    synopsis="一家人带着风筝去公园。没有风，风筝飞不起来。终于有了风，Daddy Pig 得意地放风筝——结果挂在树上了。他爬树去救风筝，树枝承受不了他的重量，他摔进了泥坑，连带全家都沾上了泥。大家决定就这样跳泥坑吧！",

    vocab=[
        {"word":"kite","phonetic":"/kaɪt/","pos":"n.","zh":"风筝","action":"双手举起，假装放线，仰头看天，风筝在空中飞"},
        {"word":"windy","phonetic":"/ˈwɪndi/","pos":"adj.","zh":"有风的","action":"双臂向两侧伸开，身体随风左右摇摆，头发乱飞"},
        {"word":"expert","phonetic":"/ˈekspɜːt/","pos":"n.","zh":"专家/行家","action":"挺胸，双手叉腰，用傲娇语气说 \"I am a bit of an expert！\""},
        {"word":"branch","phonetic":"/brɑːntʃ/","pos":"n.","zh":"树枝","action":"双臂伸开，假装是树枝，一脸担心别人来爬"},
        {"word":"stuck","phonetic":"/stʌk/","pos":"adj.","zh":"卡住了","action":"假装用力拉一个卡住的东西，越来越用力，就是动不了"},
        {"word":"rescue","phonetic":"/ˈreskjuː/","pos":"v.","zh":"救出","action":"做出英雄拯救的姿势，\"Fear not！ I will RESCUE the kite！\""},
        {"word":"nonsense","phonetic":"/ˈnɒnsns/","pos":"n.","zh":"胡说","action":"摆摆手，做出 Daddy Pig 不屑一顾的动作，\"Nonsense！ I know what I'm doing！\""},
        {"word":"muddy","phonetic":"/ˈmʌdi/","pos":"adj.","zh":"满是泥的","action":"低头看自己的衣服，假装全是泥，\"Oh. It's only mud....\""},
    ],

    patterns=[
        {"pattern":"The kite won't fly if there isn't any wind.","zh":"没有风，风筝就飞不起来","example":"No matter how fast you run. You need wind！"},
        {"pattern":"I know what I'm doing.","zh":"我知道我在做什么","example":"Daddy Pig: Don't worry. I know what I'm doing.（结果撞树）"},
        {"pattern":"You might get the kite stuck in a tree.","zh":"风筝可能会挂树上","example":"Mummy Pig: Watch out for the trees."},
        {"pattern":"It's only mud.","zh":"不过是泥嘛","example":"Daddy Pig: Luckily, I haven't hurt myself. It's only mud."},
    ],

    goals={
        "min":"孩子能说 \"No wind！ Kite won't fly！\"",
        "mid":"孩子能说 Daddy Pig 的经典台词：I know what I'm doing！",
        "ideal":"孩子主动用 <strong>\"It's only mud！\"</strong> 在生活中实际场景里使用",
    },

    phase1={
        "review_intro":"上集（第13集《Secrets》）孩子学过 <code>secret</code>。用故意说错触发：",
        "review_script":"\"上次 Peppa 有一个秘密盒子，Daddy Pig 猜了两次，猜出来了！\"（最后一句说错）",
        "review_response":"孩子会喊：\"不对！Daddy 猜的机会<strong>用完了</strong>（used up）！没猜出来！\"",
        "preview_intro":"家长双手举起，假装放风筝，然后突然风筝线松了，双手做出一切完蛋的手势——",
        "preview_script":"\"Today — Daddy Pig says he's a bit of an EXPERT at flying kites. But something goes VERY wrong. He says—\" （挺胸，傲娇地）\"'I know what I'm doing.' Watch what happens NEXT.！\"",
        "preview_mission":"\"Your mission while watching: count how many times Daddy Pig says 'I know what I'm doing'！\"",
    },

    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":"🪁","bg":"sky","trigger":"全家等待风来","action":"家长做出无聊等待的动作，望天，叹气，\"Still no wind...\""},
            {"emoji":"💨","bg":"blue","trigger":"风来了，风筝飞起来了","action":"家长仰头做出看高空的动作，眼神跟着风筝移动"},
            {"emoji":"🌳","bg":"green","trigger":"Daddy 爬树去救风筝","action":"家长做出紧张担心的样子，捂心口，\"That branch is too thin！\""},
        ],
    },

    phase3={
        "intro":"全程聊天，不是考试。家长读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":"\"So... was Daddy Pig really an expert at flying kites？ YES or NO？\"",
            "note":"",
            "rows":[
                {"child":"\"No！\"","parent":"\"NO！ He got the kite stuck in a TREE！ Experts don't do that！ Do they？\""},
                {"child":"\"Yes！\"","parent":"（假装认真）\"Well... he DID fly it very high at first. But experts don't usually FALL into muddy puddles. Do they？\""},
                {"child":"不说话","parent":"家长做出放风筝得意 → 风筝挂树 → 爬树 → 摔进泥坑的全套动作，\"Was he an expert？ YES or NO？\""},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":"\"Who was right — Mummy who said 'watch out for the trees'... or Daddy who said 'I know what I'm doing'？\"",
            "note":"",
            "rows":[
                {"child":"选 Mummy","parent":"\"MUMMY was right！ She said 'Watch out！' and what happened？ Exactly what she warned about！\""},
                {"child":"选 Daddy","parent":"（假装困惑）\"He was right？ But he got stuck... and fell in a puddle... and said 'I know what I'm doing' THREE times...\""},
                {"child":"两个都","parent":"\"Daddy was right that he COULD rescue the kite. Mummy was right about the branch being too thin！ Both！\""},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":"\"Have YOU ever said 'I know what I'm doing'... and then it went WRONG？\"",
            "note":"",
            "rows":[
                {"child":"笑着说有","parent":"\"Tell me！ What happened？ Was it as bad as falling into a muddy puddle？\""},
                {"child":"说没有","parent":"\"Never？ You always know what you're doing？ You're smarter than Daddy Pig！ Wait — we ALL are.（自嘲）\""},
                {"child":"指家长","parent":"\"ME？ Oh... （假装回忆）...yes. Every time I cook something new. 'I know what I'm doing！' （然后摊手）\""},
                {"child":"不说话","parent":"\"OK, I'll confess — I ALWAYS say 'I know what I'm doing' when I put furniture together. And it never ends well.\""},
            ],
        },
        "personal":{
            "intro":"把自信过头和犯错挂钩，让孩子体验 Daddy Pig 的感受。",
            "script_lines":[
                "\"When Daddy fell in the muddy puddle...\"",
                "（做出掉进泥坑的动作）",
                "\"...he said 'It's only mud.' Would YOU say that？\"",
            ],
            "rows":[
                {"child":"说当然不会","parent":"\"No？ You'd be UPSET？ But Daddy Pig doesn't care！ He just says...\" 等孩子接 \"It's only mud！\""},
                {"child":"说也会说","parent":"\"YES！ 'It's only mud！' — brilliant attitude！ Let's practice saying it like a TRUE Daddy Pig！\""},
                {"child":"说很脏","parent":"\"It IS very muddy！ But Mummy said something clever: 'You can't get any muddier!' So might as well jump in！\""},
                {"child":"不说话","parent":"家长自己先做出掉进泥坑的动作，摊手，\"IT'S ONLY MUD！\" 然后等孩子跟着说"},
            ],
        },
        "role_play":{
            "intro":"孩子扮演 Mummy Pig（担心派），家长扮演 Daddy Pig（自信派）。",
            "script_lines":[
                "\"YOU are Mummy Pig. You are VERY worried about that tree.",
                "\"I am Daddy Pig. I am an expert. Watch！\"",
            ],
            "rows":[
                {"child":"说 Watch out！","T_line":"\"Watch out？ Nonsense！ I know what I'm doing！ —— Now say 'The branch is too thin！'\""},
                {"child":"说 Be careful！","T_line":"\"Be careful？ I AM being careful！ I'm an expert！ —— Say 'You're too heavy！'\""},
                {"child":"做出 Daddy 摔倒","T_line":"\"WHOOPS！ （做掉进泥坑动作） ...It's only mud. Heh heh. Say 'I TOLD you so, Daddy！'\""},
            ],
        },
        "recast":[
            {"child":"the kite <u>flied</u> up","correct":"the kite <strong>flew</strong> up！","note":"不规则过去式 flew"},
            {"child":"Daddy <u>climbed</u> the tree","correct":"Daddy <strong>climbed</strong> the tree！","note":"规则过去式，已正确，继续鼓励"},
            {"child":"he <u>falled</u> down","correct":"he <strong>fell</strong> down！","note":"不规则过去式 fell"},
            {"child":"there <u>is</u> no wind","correct":"there <strong>was</strong> no wind！","note":"过去时 was"},
            {"child":"it <u>stuck</u> in tree","correct":"it got <strong>stuck</strong> in the tree！","note":"固定搭配 get stuck"},
            {"child":"Daddy is <u>expert</u>","correct":"Daddy is <strong>an</strong> expert！","note":"expert 以元音开头，用 an"},
        ],
    },

    phase4={
        "tpr":[
            {"command":"\"Fly the kite！ Higher！ Higher！\"","action":"双手高举，假装放线，仰头越来越高，越来越兴奋"},
            {"command":"\"No wind！ The kite won't fly！\"","action":"垂头丧气，风筝线耷拉下来，叹气，\"There's no wind...\""},
            {"command":"\"It's windy now！ VERY windy！\"","action":"做出被风吹的动作，头发乱了，站不稳，但开心"},
            {"command":"\"Watch out for the tree！\"","action":"Mummy Pig 的担心脸，用手指着想象的树，\"Danger！ Danger！\""},
            {"command":"\"I know what I'm doing！\"","action":"Daddy Pig 的自信动作：双手叉腰，挺胸，不屑地摆摆手，\"Nonsense！\""},
            {"command":"\"WHOOPS！ Falling！\"","action":"做出从高处猛地掉下来、摔进泥坑的夸张动作，\"SPLASH！\""},
            {"command":"\"It's only mud！\"","action":"低头看自己，耸肩，无所谓地说 \"It's only mud. Ho ho ho.\""},
        ],
        "dubbing":[
            {"num":1,"time":"约第1分30秒","scene":"Peppa 和 George 使劲跑，风筝怎么都不起飞，因为没有风。",
             "l1":"Come on！","l1_note":"抱怨地喊，气喘吁吁","l2":"No wind！ Won't fly！","l3":"\"The kite won't fly！ There's NO wind！ We need WIND！ Where is the wind？！\""},
            {"num":2,"time":"约第3分钟","scene":"Daddy Pig 得意洋洋地放风筝，声称自己是行家里手。",
             "l1":"Ta-da！","l1_note":"手势表演，仰头得意","l2":"Expert！ Watch me！","l3":"\"Yes, I am a bit of an expert at these things. Just watch and learn！\""},
            {"num":3,"time":"约第4分钟","scene":"风筝挂在树上了，Daddy Pig 开始爬树，Mummy 让他小心。",
             "l1":"I've got it！","l1_note":"假装爬树，咬牙切齿","l2":"Too heavy！ Careful！","l3":"\"Daddy Pig！ You are much too heavy for that branch！ Come down！\""},
            {"num":4,"time":"约第5分钟","scene":"Daddy 摔进泥坑，全家都溅到泥，然后大家都去跳泥坑。",
             "l1":"SPLASH！ Hehe...","l1_note":"先尴尬，再释然","l2":"It's only mud！ Jump！","l3":"\"It's only mud！ And I did rescue the kite！ Now — can we all jump in the puddle？\""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"Daddy Pig: The kite won't fly if there isn't any RAIN.","answer":"WIND！",
             "correct_line":"The kite won't fly if there isn't any <strong>wind</strong>."},
            {"num":2,"is_trap":False,
             "bug_line":"Daddy Pig: Yes, I am a bit of an expert at COOKING these things.","answer":"（去掉 COOKING）FLYING！",
             "correct_line":"I am a bit of an expert at <strong>flying</strong> these things."},
            {"num":3,"is_trap":True,
             "bug_line":"I know what I'm doing.","answer":"","correct_line":""},
            {"num":4,"is_trap":False,
             "bug_line":"Mummy Pig: Daddy Pig, you are much too TALL for that branch.","answer":"HEAVY！",
             "correct_line":"You are much too <strong>heavy</strong> for that branch."},
            {"num":5,"is_trap":False,
             "bug_line":"Peppa: Now that we're all muddy, can we jump in the BATH？","answer":"PUDDLE！",
             "correct_line":"Can we jump in the <strong>puddle</strong>？"},
        ],
    },

    phase5={
        "l1":"Family go park. Fly kite. No wind！ Then Daddy Pig get kite stuck in tree. He fall in mud！",
        "l1_response":"\"YES！ Splash！ And then what？ Did everyone go home？ Or did they...？\" 等孩子说\"跳泥坑！\"",
        "l2":"Peppa's family went to fly a kite. There was no wind at first, but then it got very windy. Daddy Pig flew the kite but it got stuck in a tree. He tried to rescue it and fell into a muddy puddle！",
        "l2_response":"\"Great！ <em>（Recast）</em> It <strong>got stuck</strong> in the tree！ And Daddy <strong>fell</strong> into the puddle！\"",
        "l3":"The Pig family went to the park to fly their kite. At first there was no wind, so the kite wouldn't fly. When the wind came, Daddy Pig flew it brilliantly — until it got stuck in a tree. He climbed up to rescue it, but the branch was too thin and he fell into a muddy puddle. Of course, everyone ended up jumping in puddles together！",
        "l3_response":"\"PERFECT！ 'The branch was too thin' — brilliant detail！ You really remember the story！\"",
        "scaffold":[
            {"stuck":"第1句说不出来","rescue":"\"OK, where did they go？ The... <strong>park</strong>！ And what did they bring？ A... <strong>kite</strong>！\""},
            {"stuck":"第2句说不出来","rescue":"\"Then the kite got... <em>（做挂树动作）</em>... <strong>stuck</strong>！ In the tree！\""},
            {"stuck":"第3句说不出来","rescue":"\"And Daddy fell in the... <em>（做SPLASH动作）</em>... muddy <strong>puddle</strong>！ Splash！\""},
            {"stuck":"完全不开口","rescue":"家长先说 L1，\"Now YOU say it！ Three words: kite, stuck, mud！\""},
        ],
        "roleplay_child":"Mummy Pig（担心者）",
        "roleplay_parent":"Daddy Pig（自信者）",
        "roleplay_situations":[
            {"label":"家长炫耀放风筝","T_line":"\"Say: 'Watch out for the trees, Daddy Pig！'\""},
            {"label":"家长假装挂树了","T_line":"\"Oh no！ Say: 'I TOLD you！ Be careful！'\""},
            {"label":"家长假装从树上摔下来","T_line":"\"SPLASH！ Now say: 'Are you okay, Daddy Pig？ Is it... only mud？'\""},
        ],
    },

    phase6={
        "phonics_title":"规则：'qu' 总是一起出现，发 /kw/",
        "phonics_word":"quick /kwɪk/",
        "phonics_mnemonic":"\"q 太孤独，总是拉着 u 一起出现，合体发 /kw/！queen, quick, quiet, question——qu 是永远的好朋友！\"",
        "phonics_table":[
            {"word":"quick","wrong":"kwik（不用qu）","right":"/kwɪk/","rule":"qu → /kw/"},
            {"word":"queen","wrong":"kween","right":"/kwiːn/","rule":"qu → /kw/"},
            {"word":"quiet","wrong":"kwait","right":"/ˈkwaɪət/","rule":"qu → /kw/"},
            {"word":"question","wrong":"kestion","right":"/ˈkwestʃən/","rule":"qu → /kw/"},
        ],
        "next_script":"\"Next time — the Pig family are going to have a picnic！ And someone says they're going to exercise — but falls asleep instead. And then a VERY tiny creature chases someone around...！ Ready？\"",
        "next_a":"Daddy Pig 被黄蜂追",
        "next_b":"George 被鸭子追",
    },

    checklist=[
        "Phase 1：孩子喊出了上集的词 secret / used up",
        "Phase 2：孩子做出了放风筝或被风吹的动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 当过考官 + 配音每个画面说过至少 Level 1 + Bugs 少于 2 次扣分",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],

    ammo=[
        {"sentence":"I know what I'm doing！","zh":"我知道我在做什么","usage":"孩子说这句时，微笑着等他做错，然后说 \"Do you, though？\""},
        {"sentence":"It's only mud.","zh":"不过是泥嘛","example":"用法：孩子磕到或弄脏时，换个角度看问题"},
        {"sentence":"Watch out for the trees！","zh":"小心那些树！","usage":"比喻：提醒孩子注意可能的障碍"},
        {"sentence":"You might get... stuck.","zh":"你可能会被卡住","usage":"做事前提醒孩子考虑风险"},
    ],
)


# ═══════════════════════════════════════════════════════════════════════════════
# EP 15 · Picnic 野餐
# ═══════════════════════════════════════════════════════════════════════════════
EP15 = _ep(
    num=15, title_en="Picnic", title_zh="野餐", color="pink",
    synopsis="一家人出门野餐，Daddy Pig 嚷嚷要运动，结果饭没吃完就睡着了。然后一只黄蜂追着他满草地狂奔——运动达成。Peppa 和 George 喂鸭子，草莓蛋糕差点被鸭子蹭走。",

    vocab=[
        {"word":"wasp","phonetic":"/wɒsp/","pos":"n.","zh":"黄蜂","action":"伸出一根手指飞来飞去，嘴里 \"Bzzzz~\""},
        {"word":"exercise","phonetic":"/ˈeksəsaɪz/","pos":"n./v.","zh":"锻炼","action":"夸张地原地跑步，越来越慢，最后瘫倒"},
        {"word":"delicious","phonetic":"/dɪˈlɪʃəs/","pos":"adj.","zh":"美味的","action":"闭眼揉肚子，发出 \"Mmm~\" 的满足声"},
        {"word":"sleepy","phonetic":"/ˈsliːpi/","pos":"adj.","zh":"困的","action":"慢慢闭眼，头歪向一侧"},
        {"word":"feed","phonetic":"/fiːd/","pos":"v.","zh":"喂食","action":"手心朝上，一小撮一小撮向前抛"},
        {"word":"waddle","phonetic":"/ˈwɒdl/","pos":"v.","zh":"摇摆走路","action":"双脚并拢左右大幅摇摆，嘴里 \"Quack！\""},
        {"word":"blanket","phonetic":"/ˈblæŋkɪt/","pos":"n.","zh":"毯子","action":"双臂大开，猛地向两侧展开，\"Swoosh！\""},
        {"word":"homemade","phonetic":"/ˌhəʊmˈmeɪd/","pos":"adj.","zh":"自制的","action":"指着厨房，做出揉面团的动作"},
    ],

    patterns=[
        {"pattern":"So much for...！","zh":"就这？说好的呢","example":"So much for Daddy Pig and his exercise."},
        {"pattern":"What a fuss！","zh":"大惊小怪！","example":"What a fuss！ It's only a little wasp."},
        {"pattern":"It's only a little...","zh":"不就是一点小...嘛","example":"It's only a little wasp."},
        {"pattern":"I managed to...","zh":"我设法做到了","example":"I managed to hang on to my cake."},
    ],

    goals={
        "min":"孩子能用 <strong>3 个词</strong>说出剧情（wasp / run / cake）",
        "mid":"孩子能用 <strong>3 句话</strong>讲故事（哪怕中英混杂）",
        "ideal":"孩子主动用 <strong>\"So much for...\"</strong> 或 <strong>\"It's only a...\"</strong> 造一句新句子",
    },

    phase1={
        "review_intro":"上集（第14集《Flying a Kite》）孩子学过 <code>kite</code> 和 <code>muddy</code>。用故意说错触发：",
        "review_script":"\"上次 Daddy Pig 放风筝，他非常厉害，风筝一直飞得很高，什么事情都没发生！\"（说错）",
        "review_response":"孩子会喊：\"不对！风筝<strong>挂树上</strong>了！Daddy 还<strong>摔进泥坑</strong>了！\"",
        "preview_intro":"家长站起来，手指做出飞的姿势，嘴里 Bzzzz~，突然往孩子方向冲过去——",
        "preview_script":"\"Today！ Someone in the Pig family... is going to be CHASED by something VERY. VERY. TINY.\" （停顿，做出抱头狂跑的样子）",
        "preview_mission":"\"Your mission while watching: count how many times Daddy Pig RUNS AWAY. Use your fingers. Ready？ Go.\"",
    },

    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":"😴","bg":"blue","trigger":"Daddy Pig 说完要运动就睡着","action":"家长慢慢闭眼，夸张地靠向沙发"},
            {"emoji":"🐝","bg":"yellow","trigger":"黄蜂出现","action":"家长夸张地缩起来，发出小声的 \"Eeek...\""},
            {"emoji":"🏃","bg":"green","trigger":"Daddy Pig 狂跑","action":"家长忍着笑，偷偷瞄孩子脸上的反应"},
        ],
    },

    phase3={
        "intro":"这一整个 Phase 都是\"聊天\"，不是考试。家长全程用英文说，孩子用中文或英文回答都算。核心任务：<strong>读孩子的脸</strong>。眼神亮 → 继续；眼神空 → 立刻降级。",
        "q1":{
            "type_label":"Yes/No 兜底，绝对能回答",
            "script":"\"So... did Daddy Pig actually exercise？ Yes or no？\"",
            "note":"家长做出疑惑脸，双手一摊",
            "rows":[
                {"child":"\"No！\" / 摇头","parent":"\"NO！ Zero exercise！ He just... <em>（做出呼呼大睡的样子）</em> ...Zzzzz！ So much for Daddy Pig！\""},
                {"child":"\"Yes！\" / 点头","parent":"<em>（假装震惊）</em>\"He exercised?！ Wait — the WASP made him run. Does that count？！\""},
                {"child":"不说话","parent":"家长做出举拳头然后立刻睡着的动作，再问 \"Did he? YES or NO？\""},
            ],
        },
        "q2":{
            "type_label":"二选一，孩子永远有话说",
            "script":"\"Was Daddy Pig scared of the wasp... or was he BRAVE？\"",
            "note":"\"scared\" 时做出缩起来发抖的动作；\"brave\" 时做出超级英雄的 pose",
            "rows":[
                {"child":"\"Scared！\"","parent":"\"VERY scared！ <em>（模仿 Daddy Pig 的大肚子狂跑）</em> His personal trainer was a tiny insect！ Ha！\""},
                {"child":"\"Brave！\"","parent":"<em>（假装认真思考）</em>\"Hmmm... he RAN AWAY from the wasp. Is that... brave？ Or is that...？\" <em>（等孩子改口）</em>"},
                {"child":"说中文\"害怕\"","parent":"\"Yes！ SCARED！ Super scared！ <em>（Recast）</em> He was so scared！\""},
            ],
        },
        "q3":{
            "type_label":"开放式，孩子怎么答都行",
            "script":"\"If YOU were there, and a wasp landed on YOUR cake... what would YOU do？\"",
            "note":"指着孩子，然后做出黄蜂飞来的手势",
            "rows":[
                {"child":"比划打虫子","parent":"\"You'd FIGHT it！ <em>（做出打拳的动作）</em> Brave！ What would you say？ Shoo？ Get away？\""},
                {"child":"说跑","parent":"\"Run away！ Just like Daddy Pig！ SAME！ Ha！\""},
                {"child":"说吃掉蛋糕","parent":"\"EAT IT FIRST！ <em>（假装惊喜）</em> Smart！ Very smart！ Before the wasp gets it！\""},
                {"child":"说不知道","parent":"家长先自己疯狂假装跑，然后问 \"You？ Same？ Or different？\""},
            ],
        },
        "personal":{
            "intro":"把剧情和孩子自己的生活挂钩，这是语言迁移的触发点。",
            "script_lines":[
                "\"Have YOU ever said... 'I'm going to exercise！'...\"",
                "（举拳头，慷慨激昂）",
                "\"...and then just... fell asleep？\"",
            ],
            "rows":[
                {"child":"笑着指家长","parent":"\"That's me every Sunday. <strong>So much for exercising！</strong> <em>（自嘲地耸肩）</em>\""},
                {"child":"点头承认","parent":"\"YES！ Me too！ We are BOTH Daddy Pig！\""},
                {"child":"说中文具体的事","parent":"Recast: \"Oh！ <strong>So much for practicing piano！</strong>\""},
                {"child":"不说话","parent":"\"You always exercise？ You are better than Daddy Pig！\" <em>（夸张崇拜）</em>"},
            ],
        },
        "role_play":{
            "intro":"让孩子站进角色立场，用第一人称说出本集词汇。",
            "script_lines":[
                "\"Excuse me！ Are you Daddy Pig？\"",
                "\"I'm a reporter. Can I ask — after the wasp incident... how do you FEEL？\"",
            ],
            "rows":[
                {"child":"做出跑的动作","parent":"\"You RAN AWAY！ And did you keep your cake？ Did you？\""},
                {"child":"说 \"tired\"","parent":"\"Tired！ But — did you keep your cake？\""},
                {"child":"说 \"scared\"","parent":"\"The wasp was so tiny and Daddy Pig was so—\" <em>（等孩子接 big/fat）</em>"},
                {"child":"说中文","parent":"家长先扮演 Daddy Pig 示范，\"Now YOU try！\""},
            ],
        },
        "recast":[
            {"child":"Daddy Pig <u>runned</u> away","correct":"Daddy Pig <strong>RAN</strong> away！ So fast！","note":"不规则动词过去式 ran"},
            {"child":"the <u>bee</u> chased him","correct":"A <strong>wasp</strong> chased him！ A wasp, not a bee — bzzzz~","note":"词汇纠错"},
            {"child":"he <u>is</u> scared","correct":"He <strong>was</strong> scared！ Super scared！","note":"过去时 was"},
            {"child":"a wasp <u>chase</u> him","correct":"The wasp <strong>chased</strong> him！ Chased him everywhere！","note":"过去时 chased"},
            {"child":"Daddy Pig <u>fall</u> asleep","correct":"He <strong>fell</strong> asleep！ Boom！","note":"不规则动词 fell"},
            {"child":"he <u>hold</u> the cake","correct":"He <strong>held</strong> on to his cake！","note":"不规则动词 held"},
        ],
    },

    phase4={
        "tpr":[
            {"command":"\"Spread the picnic blanket！\"","action":"双臂大开向两侧猛地展开，喊一声 \"Swoosh！\""},
            {"command":"\"I'm really hungry！ Let's eat！\"","action":"揉肚子，然后夸张地大口咬东西，\"Mmm！Mmm！\""},
            {"command":"\"I feel quite sleepy.\"","action":"抱臂靠向沙发/墙壁，慢慢闭眼，发出呼噜声 \"Zzzzzzz...\""},
            {"command":"\"Feed the ducks！\"","action":"蹲低，一只手不停向前抛，嘴里喊 \"Here you go！Quack quack！\""},
            {"command":"\"Waddle like a duck！\"","action":"双脚并拢，左右大幅摇摆走路，嘴里不停 \"Quack quack！\""},
            {"command":"\"Eeek！ A wasp！ Run away！\"","action":"先尖叫一声 \"EEEK！\"，然后疯狂原地跑，双手在头顶乱挥"},
            {"command":"\"Stay still！ Don't move！\"","action":"全身瞬间僵住，屏住呼吸，连眼睛都不能眨"},
            {"command":"\"Run around and get some exercise！\"","action":"原地跑步，越跑越慢，最后夸张地瘫倒"},
        ],
        "dubbing":[
            {"num":1,"time":"约第2分30秒","scene":"Daddy Pig 刚说完\"我要去运动！\"，下一秒就在野餐毯上睡着了。",
             "l1":"Zzzzz...","l1_note":"边说边倒向一侧","l2":"Sleepy！ So lazy！","l3":"\"I thought you wanted to exercise, Daddy Pig！\""},
            {"num":2,"time":"约第3分50秒","scene":"Mummy Pig 发现一只黄蜂飞到蛋糕上，猛地跳起来尖叫。",
             "l1":"EEEK！","l1_note":"声音越尖越好","l2":"Wasp！ Help！","l3":"\"Eeek！ A wasp！ I hate wasps！ Shoo！\""},
            {"num":3,"time":"约第4分20秒","scene":"Daddy Pig 被黄蜂追着满草地乱跑，双手乱挥。",
             "l1":"Shoo！","l1_note":"边喊边疯狂挥手","l2":"Run！ Get away！","l3":"\"Shoo！ Get it off me！ You little pest！\""},
            {"num":4,"time":"约第5分10秒","scene":"满头大汗的 Daddy Pig 跑回来，得意地举起草莓蛋糕。",
             "l1":"My cake！","l1_note":"高举想象中的蛋糕","l2":"I kept it！ The cake is safe！","l3":"\"Luckily, I managed to hang on to my slice of strawberry cake！\""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"Mummy's homemade strawberry POOP is there, too.","answer":"CAKE！",
             "correct_line":"Mummy's homemade strawberry <strong>cake</strong> is there, too."},
            {"num":2,"is_trap":False,
             "bug_line":"My BUTT is not big.","answer":"TUMMY！",
             "correct_line":"My <strong>tummy</strong> is not big."},
            {"num":3,"is_trap":True,
             "bug_line":"So much for Daddy Pig and his exercise.","answer":"","correct_line":""},
            {"num":4,"is_trap":False,
             "bug_line":"It's only a little T-REX.","answer":"WASP！",
             "correct_line":"It's only a little <strong>wasp</strong>."},
            {"num":5,"is_trap":False,
             "bug_line":"You are very lucky ZOMBIES.","answer":"DUCKS！",
             "correct_line":"You are very lucky <strong>ducks</strong>."},
        ],
    },

    phase5={
        "l1":"Peppa 家去 picnic. Daddy Pig 说要 exercise 然后睡着了. Wasp 追他，他 run away！",
        "l1_response":"\"YES！ That's the story！ And did he keep his...？\" （等孩子补 cake）",
        "l2":"The family went to picnic. Daddy Pig said exercise but he sleep. A wasp chase Daddy Pig and he run very fast.",
        "l2_response":"\"Great！ <em>（Recast）</em> The wasp <strong>chased</strong> him and he <strong>ran</strong> very fast！ And he kept his cake！\"",
        "l3":"The Pig family had a picnic. Daddy Pig said he'd exercise, but he fell asleep. Then a wasp chased him everywhere — so much for Daddy Pig！",
        "l3_response":"\"PERFECT！ 'So much for Daddy Pig！' — That's EXACTLY what Peppa said！\"",
        "scaffold":[
            {"stuck":"第1句说不出来","rescue":"\"OK, so first... the family went to a... <strong>pic-nic</strong>...\" （停顿）"},
            {"stuck":"第2句说不出来","rescue":"\"Then Daddy Pig said he wanted to... <strong>ex-er-</strong>...\" （做出跑步动作）"},
            {"stuck":"第3句说不出来","rescue":"\"But then a tiny thing flew in... <em>Bzzzz~...</em>\" （手指做飞的姿势）"},
            {"stuck":"完全不开口","rescue":"家长自己先说 Level 1，\"Now YOU say it！ Copy me！\""},
        ],
        "roleplay_child":"Daddy Pig（被追的那个）",
        "roleplay_parent":"黄蜂（追人的那个）",
        "roleplay_situations":[
            {"label":"孩子疯狂跑起来","T_line":"\"That was great！ You RAN AWAY！ Now say it — 'Run away！'\""},
            {"label":"孩子喊 Shoo！","T_line":"\"SHOO！ Yes！ Now say the whole thing — 'Shoo！ Shoo, wasp！'\""},
            {"label":"孩子站着不动","T_line":"\"Stay still！ Don't move！ Say it — 'Stay still！'\""},
            {"label":"孩子喊 Get away！","T_line":"\"Louder！ The wasp can't hear you！ Say it again！\""},
        ],
    },

    phase6={
        "phonics_title":"规则：wa- 魔法变音",
        "phonics_word":"wasp /wɒsp/",
        "phonics_mnemonic":"\"w 后面跟 a，a 变懒，不说 /æ/，说 /ɒ/。\"",
        "phonics_table":[
            {"word":"wasp","wrong":"WA-sp（/æ/）","right":"/wɒsp/","rule":"wa → /wɒ/"},
            {"word":"wash","wrong":"WA-sh（/æ/）","right":"/wɒʃ/","rule":"wa → /wɒ/"},
            {"word":"want","wrong":"WA-nt（/æ/）","right":"/wɒnt/","rule":"wa → /wɒ/"},
            {"word":"watch","wrong":"WA-tch（/æ/）","right":"/wɒtʃ/","rule":"wa → /wɒ/"},
        ],
        "next_script":"\"Next time — the Pig family find a box of old instruments in the attic！ And someone who's never played before... manages to do something everyone else couldn't！\"",
        "next_a":"George 吹响了号角",
        "next_b":"Daddy Pig 拉小提琴拉得很好听",
    },

    checklist=[
        "Phase 1：孩子喊出了上集的词 kite / stuck / muddy",
        "Phase 2：孩子用手指数了 Daddy Pig 跑的次数",
        "Phase 3：孩子回答了至少 1 个问题（哪怕只是 Yes/No）",
        "Phase 4：TPR 当过考官 + 配音每个画面说过至少 Level 1 + Find the Bugs 少于 2 次扣分",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],

    ammo=[
        {"sentence":"So much for...！","zh":"就这？说好的呢","usage":"孩子说今天一定练琴结果没练：'So much for practicing piano！'"},
        {"sentence":"What a fuss！","zh":"大惊小怪！","usage":"孩子因碗里有一根葱哭天抹泪：'What a fuss！ It's only a little onion.'"},
        {"sentence":"It's only a little...","zh":"不就是一点小...嘛","usage":"孩子摔了点皮：'It's only a little scratch. You're fine！'"},
        {"sentence":"I managed to...","zh":"我设法做到了","usage":"孩子终于把难题做出来：'You managed to solve it！ Great job！'"},
    ],
)


# ═══════════════════════════════════════════════════════════════════════════════
# EP 16 · Musical Instruments 乐器
# ═══════════════════════════════════════════════════════════════════════════════
EP16 = _ep(
    num=16, title_en="Musical Instruments", title_zh="乐器", color="amber",
    synopsis="爸妈从阁楼翻出一箱旧乐器。Mummy 拉小提琴很优雅，Peppa 一拉像猫叫。全家轮流吹一个破号，无论谁吹都难听到爆——最后 George 把号吹响了，完美反转收尾。",

    vocab=[
        {"word":"instrument","phonetic":"/ˈɪnstrəmənt/","pos":"n.","zh":"乐器","action":"假装依次演奏小提琴、鼓、手风琴，随便换"},
        {"word":"dusty","phonetic":"/ˈdʌsti/","pos":"adj.","zh":"布满灰尘的","action":"拍打想象中的旧东西，假装灰尘扑脸，大打喷嚏 \"Achoo！\""},
        {"word":"blow","phonetic":"/bləʊ/","pos":"v.","zh":"吹","action":"深吸一口气，憋住，用力往外吹，脸憋得通红"},
        {"word":"impossible","phonetic":"/ɪmˈpɒsɪbl/","pos":"adj.","zh":"不可能的","action":"双手向两侧摊开，耸肩摇头，深叹气，\"Phhhh...\""},
        {"word":"bravo","phonetic":"/ˈbrɑːvəʊ/","pos":"excl.","zh":"好极了","action":"使劲鼓掌，竖大拇指，大喊 \"BRAVO！\""},
        {"word":"attic","phonetic":"/ˈætɪk/","pos":"n.","zh":"阁楼","action":"踮脚尖，双手向上伸，做用力从阁楼搬东西的样子"},
        {"word":"violin","phonetic":"/ˌvaɪəˈlɪn/","pos":"n.","zh":"小提琴","action":"夹起想象的小提琴，拉弓，发出世界上最难听的猫叫声"},
        {"word":"horn","phonetic":"/hɔːn/","pos":"n.","zh":"号角","action":"双手握拳靠嘴，憋住气，用全身力气吹，发出任何奇怪的声音"},
    ],

    patterns=[
        {"pattern":"I haven't played it for a long time.","zh":"我好久没玩了/练了","example":"Daddy Pig: I haven't played the accordion for a long time."},
        {"pattern":"Even if I say so myself.","zh":"虽然是我自夸（但我确实不错）","example":"Daddy Pig: I play quite nicely, even if I say so myself."},
        {"pattern":"You have to blow it very hard.","zh":"你得用很大的力气吹","example":"You have to blow the horn very hard."},
        {"pattern":"It's impossible！","zh":"这不可能！","example":"It's impossible to play the horn！ Nobody can do it！"},
    ],

    goals={
        "min":"孩子能模仿乐器动作并说至少一个乐器名称",
        "mid":"孩子能用一句话说出故事反转：George blew the horn！",
        "ideal":"孩子主动用 <strong>\"Even if I say so myself\"</strong> 或 <strong>\"It's impossible！\"</strong>",
    },

    phase1={
        "review_intro":"上集（第15集《Picnic》）孩子学过 <code>wasp</code> 和 <code>So much for...</code>。用故意说错触发：",
        "review_script":"\"上次 Daddy Pig 说要运动，然后他跑得非常快，把那只黄蜂追跑了！\"（说错主语）",
        "review_response":"孩子会喊：\"不对！是黄蜂<strong>追</strong>了 Daddy Pig！Daddy 跑的！\"",
        "preview_intro":"家长做出从阁楼搬东西的动作，灰尘满天飞，打喷嚏——",
        "preview_script":"\"Today — the Pig family find a box of old, dusty musical instruments! Everyone tries to play the same instrument. The problem？ Nobody can！ Except... one very surprising someone.\"",
        "preview_mission":"\"Your mission while watching: which instrument CAN George play？ Listen carefully！\"",
    },

    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":"🎻","bg":"amber","trigger":"Mummy 优雅地拉小提琴","action":"家长做出优雅的拉琴动作，点头，闭眼陶醉"},
            {"emoji":"😖","bg":"red","trigger":"Peppa 拉的声音难听到爆","action":"家长夸张地捂耳朵，痛苦扭曲的表情"},
            {"emoji":"😮","bg":"green","trigger":"George 吹响了号角","action":"家长做出惊掉下巴的表情，指着 George，不敢相信"},
        ],
    },

    phase3={
        "intro":"全程聊天，不是考试。家长读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":"\"So... could ANYONE in the family play the horn？ YES or NO？\"",
            "note":"",
            "rows":[
                {"child":"\"Yes！ George！\"","parent":"\"GEORGE！ The YOUNGEST one！ Nobody else could！ Impossible for everyone else！ But for George...？\""},
                {"child":"\"No！\"","parent":"（假装震惊）\"NOBODY？ Then who made that sound at the end？ Was that... ？\"（等孩子说 George）"},
                {"child":"不说话","parent":"家长做出三个人依次吹号，全部失败的动作，最后做出小 George 轻松吹响的惊喜脸"},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":"\"Was the violin easy or IMPOSSIBLE for Peppa？\"",
            "note":"",
            "rows":[
                {"child":"\"Impossible！\"","parent":"\"IMPOSSIBLE！ She played it like a SCREAMING CAT！ （做出捂耳朵痛苦脸） But she was very CONFIDENT！\""},
                {"child":"\"Easy！\"","parent":"（假装思考）\"She thought it was easy... but it sounded like... （做出难听的动作） Hmm, was that easy for EVERYONE listening？\""},
                {"child":"说中文","parent":"\"It was IMPOSSIBLE for her! <em>（Recast）</em> Playing the violin was <strong>impossible</strong> for Peppa！\""},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":"\"If YOU found a box of old musical instruments, which one would YOU want to play？\"",
            "note":"",
            "rows":[
                {"child":"选乐器","parent":"\"[乐器名]！ Can you show me？ What sound does it make？ Play it for me！\""},
                {"child":"说都想玩","parent":"\"ALL of them！ Like the Pig family！ What would YOU try first？\""},
                {"child":"说不会","parent":"\"That's OK！ Daddy Pig hadn't played for a LONG time too！ That's why he said...\" 等孩子接"},
                {"child":"不说话","parent":"家长假装各种乐器，\"This one？ Or this one？ Or THIS one？\" （做出打鼓/吹号/拉琴的动作）"},
            ],
        },
        "personal":{
            "intro":"把学乐器和孩子的经历挂钩。",
            "script_lines":[
                "\"Have YOU ever tried to play an instrument？\"",
                "（做出各种乐器动作）",
                "\"And did it sound AMAZING... or more like Peppa's violin？\"",
            ],
            "rows":[
                {"child":"说有学过","parent":"\"Did it sound amazing at first？ Or did YOU need practice？ 'I haven't played it for a long time' is the BEST excuse！\""},
                {"child":"说没有","parent":"\"Not yet！ But if you found a dusty old box with instruments inside... which one？\""},
                {"child":"说学钢琴/小提琴","parent":"\"So you're Mummy Pig！ Do you play nicely even if you say so yourself？ （做出自夸动作）\""},
                {"child":"不说话","parent":"家长做出自己假装吹号，脸憋得通红，发出奇怪声音，\"Like this？ BRAVO for me？\""},
            ],
        },
        "role_play":{
            "intro":"孩子扮演 George（意外能吹号），家长扮演惊讶的观众。",
            "script_lines":[
                "\"Okay！ Everyone has tried. It's IMPOSSIBLE. Nobody can blow the horn.\"",
                "\"Wait... George？ YOU want to try？ Ha！ Go ahead... （摆出怀疑的表情）\"",
            ],
            "rows":[
                {"child":"假装吹号","T_line":"\"Is it working？ Is it？ ... （假装震惊） BRAVO！ BRAVO GEORGE！ Say 'I did it！'\""},
                {"child":"发出任何声音","T_line":"\"You blew it！ That counts！ Now say 'Even George can do it！'\""},
                {"child":"不做动作","T_line":"\"Go on！ Just pretend！ Take a big breath and... BLOW！ Like this!\" （示范）"},
            ],
        },
        "recast":[
            {"child":"Peppa <u>play</u> the violin","correct":"Peppa <strong>played</strong> the violin！","note":"规则过去式"},
            {"child":"George <u>blowed</u> the horn","correct":"George <strong>blew</strong> the horn！","note":"不规则过去式 blew"},
            {"child":"it <u>sound</u> terrible","correct":"it <strong>sounded</strong> terrible！","note":"规则过去式"},
            {"child":"nobody <u>can</u> play it","correct":"nobody <strong>could</strong> play it！","note":"过去式 could"},
            {"child":"Daddy find the box","correct":"Daddy <strong>found</strong> the box！","note":"不规则过去式 found"},
        ],
    },

    phase4={
        "tpr":[
            {"command":"\"Find the old box in the attic！\"","action":"踮脚尖，双手向上伸，做用力搬重物的样子，咬牙发出 \"Nnnggg！\""},
            {"command":"\"Play the violin！\"","action":"夹起想象的小提琴，拉弓，发出世界上最难听的猫叫声 \"Eeeeeek~\""},
            {"command":"\"Bang the drum！\"","action":"双手交替猛捶大腿，越来越快，嘴里数 \"BOOM BOOM BOOM！\""},
            {"command":"\"Blow the horn！ Blow very hard！\"","action":"双手握拳靠嘴，憋住气，用全身力气吹，发出任何奇怪的声音"},
            {"command":"\"Cover your ears！ It sounds terrible！\"","action":"双手使劲捂耳朵，做痛苦扭曲的表情，大喊 \"Oh no！ Stop！\""},
            {"command":"\"It's impossible！\"","action":"双手向两侧摊开，耸肩摇头，深深叹气，\"Phhhh...\""},
            {"command":"\"George blew the horn！ BRAVO！\"","action":"做出极度惊讶的表情，然后使劲鼓掌，喊 \"BRAVO！ BRAVO GEORGE！\""},
        ],
        "dubbing":[
            {"num":1,"time":"约第1分30秒","scene":"Peppa 夹起小提琴，满脸自信地开始拉，爸妈捂耳朵露出痛苦表情。",
             "l1":"Terrible！","l1_note":"捂耳朵，痛苦脸","l2":"Stop！ Too loud！","l3":"\"Oh dear！ I do not think that is meant to sound like that！\""},
            {"num":2,"time":"约第3分钟","scene":"Daddy Pig 深情地拉手风琴，Mummy Pig 旁边心动，两人对视，气氛甜到发腻。",
             "l1":"Lovely！","l1_note":"做一个爱心手势","l2":"Beautiful！ So romantic！","l3":"\"I used to play this to Mummy Pig when we first met. Even if I say so myself.\""},
            {"num":3,"time":"约第4分钟","scene":"全家三人依次拿起号角，每人都深吸气，吹出各种奇怪的声音。",
             "l1":"Impossible！","l1_note":"摊手耸肩","l2":"Nobody can！ Too hard！","l3":"\"Maybe it just needs someone big and strong like me！ （吹） ...Still impossible！\""},
            {"num":4,"time":"约第5分钟","scene":"George 走过去捡起号角，轻轻一吹，\"嘀——\"响了！全家惊讶张嘴。",
             "l1":"Wow！","l1_note":"张大嘴，愣住","l2":"George！ He did it！","l3":"\"Mummy couldn't！ Daddy couldn't！ Peppa couldn't！ But GEORGE can！\""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"They are a bit old and STINKY SOCKS.","answer":"DUSTY！",
             "correct_line":"They are a bit old and <strong>dusty</strong>."},
            {"num":2,"is_trap":False,
             "bug_line":"I haven't EATEN it for a long time.","answer":"PLAYED！",
             "correct_line":"I haven't <strong>played</strong> it for a long time."},
            {"num":3,"is_trap":True,
             "bug_line":"You have to blow it very hard.","answer":"","correct_line":""},
            {"num":4,"is_trap":False,
             "bug_line":"Maybe it just needs someone big and SMELLY like me.","answer":"STRONG！",
             "correct_line":"Maybe it just needs someone big and <strong>strong</strong> like me."},
            {"num":5,"is_trap":False,
             "bug_line":"Mummy couldn't. Daddy couldn't. Even GRANDPA couldn't. But George can！","answer":"I (Peppa)！",
             "correct_line":"Mummy couldn't. Daddy couldn't. Even <strong>I</strong> couldn't. But George can！"},
        ],
    },

    phase5={
        "l1":"Daddy find old instruments. Everyone try play horn. All fail. George blow it！ BRAVO！",
        "l1_response":"\"BRAVO！ And George is the YOUNGEST one！ Was anyone expecting that？！\"",
        "l2":"The Pig family found dusty old instruments in the attic. Everyone tried to blow the horn but nobody could. Then little George tried... and he did it！",
        "l2_response":"\"Great！ <em>（Recast）</em> Nobody <strong>could</strong>！ Past tense！ But George <strong>did</strong> it！\"",
        "l3":"The Pig family discovered a box of old musical instruments in the attic. Everyone tried to blow the horn, but it seemed impossible. Then George picked it up, blew once — and everyone was amazed！",
        "l3_response":"\"PERFECT！ 'It seemed impossible' — beautiful！ And 'everyone was amazed' — perfect！\"",
        "scaffold":[
            {"stuck":"第1句说不出来","rescue":"\"OK, what did Daddy find？ Old... <strong>instruments</strong>！ From where？ The... <strong>attic</strong>！\""},
            {"stuck":"第2句说不出来","rescue":"\"Then everyone tried to blow the... <strong>horn</strong>！ Could they？ <em>（摇头，摊手）</em> Impossible！\""},
            {"stuck":"第3句说不出来","rescue":"\"But little George picked it up and... <em>（做吹号动作）</em>... <strong>BRAVO</strong>！\""},
            {"stuck":"完全不开口","rescue":"家长先说 L1，\"Now YOU say it！ Just say: instruments, impossible, George！\""},
        ],
        "roleplay_child":"George（意外能吹号）",
        "roleplay_parent":"全家（一一尝试，然后惊讶）",
        "roleplay_situations":[
            {"label":"孩子假装吹号但没声音","T_line":"\"Nobody can！ Say 'It's impossible！'\""},
            {"label":"孩子继续吹","T_line":"\"Don't give up！ Say 'I'll try again！ Blow very hard！'\""},
            {"label":"孩子发出任何声音","T_line":"\"IT WORKED！ Say 'BRAVO！' or 'I did it！'\""},
        ],
    },

    phase6={
        "phonics_title":"规则：-tion 和 -sion 都发 /ʃən/",
        "phonics_word":"station /ˈsteɪʃən/ · musician /mjuːˈzɪʃən/",
        "phonics_mnemonic":"\"tion 和 sion 结尾的词，都发 /ʃən/——就像乐器发出的 \"shhhh\" 一样！\"",
        "phonics_table":[
            {"word":"station","wrong":"sta-TI-on","right":"/ˈsteɪʃən/","rule":"-tion → /ʃən/"},
            {"word":"musician","wrong":"musi-CI-an","right":"/mjuːˈzɪʃən/","rule":"-cian → /ʃən/"},
            {"word":"action","wrong":"ac-TI-on","right":"/ˈækʃən/","rule":"-tion → /ʃən/"},
            {"word":"passion","wrong":"pas-SI-on","right":"/ˈpæʃən/","rule":"-sion → /ʃən/"},
        ],
        "next_script":"\"Next time — Peppa and George go to Grandpa's garden again！ They see frogs, worms, and butterflies... and decide to BECOME them！ Which one do you think Peppa will want to be？\"",
        "next_a":"蝴蝶（最漂亮）",
        "next_b":"青蛙（可以跳泥坑！）",
    },

    checklist=[
        "Phase 1：孩子喊出了上集的词 wasp / So much for",
        "Phase 2：孩子做出了至少一种乐器的演奏动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 当过考官 + 配音每个画面说过至少 Level 1 + Bugs 少于 2 次扣分",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],

    ammo=[
        {"sentence":"I haven't [done] it for a long time！","zh":"我好久没...了","usage":"孩子很久没做某件事，或者生疏了，用这句找借口"},
        {"sentence":"Even if I say so myself！","zh":"虽然是我自夸，但……","usage":"做出了一件事觉得不错，自我欣赏时"},
        {"sentence":"You have to blow very hard！","zh":"你得用很大力气","usage":"孩子遇到需要努力的事，鼓励他加油"},
        {"sentence":"It's impossible！","zh":"不可能！","usage":"先夸张地说，然后让孩子证明给你看 \"It's impossible！ Can YOU do it？\""},
    ],
)


# ═══════════════════════════════════════════════════════════════════════════════
# EP 17 · Frogs and Worms and Butterflies 青蛙虫子蝴蝶
# ═══════════════════════════════════════════════════════════════════════════════
EP17 = _ep(
    num=17, title_en="Frogs and Worms and Butterflies", title_zh="青蛙虫子蝴蝶", color="emerald",
    synopsis="Peppa 和 George 在 Grandpa 的花园里，Peppa 扮蝴蝶，George 不要当虫子，非要当蝴蝶。Grandpa 示范当虫子扭来扭去，最后全家一起发现青蛙最棒——因为青蛙可以跳泥坑！",

    vocab=[
        {"word":"frog","phonetic":"/frɒɡ/","pos":"n.","zh":"青蛙","action":"蹲低，双手撑地，使劲跳起，嘴里 \"Ribbit！\""},
        {"word":"butterfly","phonetic":"/ˈbʌtəflaɪ/","pos":"n.","zh":"蝴蝶","action":"双臂像翅膀优雅地展开，原地慢慢转圈，\"I'm a beautiful butterfly！\""},
        {"word":"worm","phonetic":"/wɜːm/","pos":"n.","zh":"蚯蚓","action":"躺地上（或做弯腰动作），全身扭来扭去，\"I'm a wriggly worm！\""},
        {"word":"wriggle","phonetic":"/ˈrɪɡl/","pos":"v.","zh":"扭动","action":"全身快速扭动，像被触电，嘴里 \"Wriggle wriggle wriggle！\""},
        {"word":"pretend","phonetic":"/prɪˈtend/","pos":"v.","zh":"假装/扮演","action":"做出戴面具的手势，\"Let's pretend！ I am a...\" 然后做出某个动物"},
        {"word":"pond","phonetic":"/pɒnd/","pos":"n.","zh":"池塘","action":"双手做出捞水的动作，\"There's a pond！ With frogs！\""},
        {"word":"lovely","phonetic":"/ˈlʌvli/","pos":"adj.","zh":"可爱的/美丽的","action":"双手捧脸，做出陶醉的表情，\"Lovely！\""},
        {"word":"muddy","phonetic":"/ˈmʌdi/","pos":"adj.","zh":"满是泥的","action":"低头看脚，假装踩进泥里，\"It's muddy！ Perfect！\""},
    ],

    patterns=[
        {"pattern":"Let's play at being...！","zh":"我们来扮演...吧！","example":"Let's play at being frogs！ I'm a little froggy！"},
        {"pattern":"I'm a wriggly worm！","zh":"我是一条扭来扭去的虫！","example":"First you have to lie down... then wriggle！ I'm a wriggly worm！"},
        {"pattern":"Butterflies are nice, but frogs are better！","zh":"蝴蝶很好，但青蛙更好","example":"Because frogs can jump in muddy puddles！"},
        {"pattern":"Frogs love jumping in muddy puddles！","zh":"青蛙喜欢在泥坑里跳","example":"Grandpa Pig: Yes！ Frogs love jumping in muddy puddles！"},
    ],

    goals={
        "min":"孩子能模仿蝴蝶、虫子、青蛙三个动作",
        "mid":"孩子能说 \"I'm a [frog/butterfly/worm]！\"",
        "ideal":"孩子主动说 <strong>\"Frogs love jumping in muddy puddles！\"</strong>",
    },

    phase1={
        "review_intro":"上集（第16集《Musical Instruments》）孩子学过 <code>impossible</code>。用故意说错触发：",
        "review_script":"\"上次 George 拿起那个旧号角，吹了半天，完全吹不响，大家都笑他！\"（说错结局）",
        "review_response":"孩子会喊：\"不对！George<strong>吹响了</strong>！所有人都惊讶！BRAVO！\"",
        "preview_intro":"家长突然四肢着地，开始像虫子一样扭来扭去——",
        "preview_script":"\"Today! Peppa and George visit Grandpa's garden! And they see REAL animals! And Grandpa teaches them to BECOME those animals！ （站起来，摊手）Worm？ Butterfly？ Or FROG？ Which is best？\"",
        "preview_mission":"\"Your mission while watching: which animal does Peppa like BEST at the end？ Remember！\"",
    },

    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":"🦋","bg":"emerald","trigger":"Peppa 开始假装蝴蝶","action":"家长优雅地展开双臂，原地慢慢转圈，做出蝴蝶的动作"},
            {"emoji":"🐛","bg":"green","trigger":"Grandpa 示范当虫子扭来扭去","action":"家长做出夸张的虫子扭动动作，滚来滚去，越来越搞笑"},
            {"emoji":"🐸","bg":"blue","trigger":"大家都变成青蛙跳泥坑","action":"家长做出青蛙跳的动作，\"Ribbit！ Ribbit！\" 找泥坑跳"},
        ],
    },

    phase3={
        "intro":"全程聊天，不是考试。家长读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":"\"So... at the end, did everyone want to be FROGS？ YES or NO？\"",
            "note":"",
            "rows":[
                {"child":"\"Yes！\"","parent":"\"YES！ Because frogs can do Peppa's FAVOURITE thing！ What is it？\"（等孩子说跳泥坑）"},
                {"child":"\"No！\"","parent":"（假装困惑）\"Really？ Then why was everyone jumping in the muddy puddle at the end？ Did they become ducks？\""},
                {"child":"不说话","parent":"家长做出蝴蝶 → 虫子 → 青蛙跳进泥坑的三段动作，\"At the end？ FROGS？ YES or NO？\""},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":"\"Is a butterfly more beautiful... or is a frog more FUN？\"",
            "note":"",
            "rows":[
                {"child":"选 butterfly","parent":"\"Beautiful！ Like Peppa thought at first！ She was all...\" （做蝴蝶动作）\"But then she changed her mind！ Why？\""},
                {"child":"选 frog","parent":"\"FUN！ Because frogs...\" （等孩子说）\"...jump in MUDDY PUDDLES！ BEST. ANIMAL. EVER！\""},
                {"child":"两个都","parent":"\"Both！ You know what？ That's the smartest answer！ Be a beautiful frog！\""},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":"\"If YOU could pretend to be ANY animal, which would you choose？\"",
            "note":"",
            "rows":[
                {"child":"选动物","parent":"\"[动物名]！ Show me！ What sound does it make？ What does it do？ Come on！\""},
                {"child":"选恐龙","parent":"（笑）\"Like George！ Always！ OK, show me your best dinosaur！ GRRR！\""},
                {"child":"选蝴蝶","parent":"\"Beautiful butterfly！ 'I'm a little butterfly！' — say it while doing the wing movement！\""},
                {"child":"不说话","parent":"家长先做出三种动物，\"Which one is YOUR favourite？ Fly？ Wriggle？ Jump in puddles？\""},
            ],
        },
        "personal":{
            "intro":"把扮演动物的游戏与孩子日常玩法挂钩。",
            "script_lines":[
                "\"Have YOU ever pretended to be an animal？\"",
                "（做出各种动物的动作）",
                "\"Which animal were YOU？\"",
            ],
            "rows":[
                {"child":"说动物","parent":"\"Show me！ Be a [动物] right now！ I'll guess what you are！\""},
                {"child":"说没有","parent":"\"You've never pretended？ Come on！ Right now — you're a FROG！ Ribbit！ Jump！\""},
                {"child":"做动作","parent":"\"Is that a... butterfly？ Worm？ Frog？ Oh！ It's a [孩子做的动物]！ BRAVO！\""},
                {"child":"指家长先做","parent":"家长做出夸张的各种动物，\"Your turn！ Choose one！ Any animal！ Go！\""},
            ],
        },
        "role_play":{
            "intro":"全家都变成动物！孩子选，家长跟着做。",
            "script_lines":[
                "\"OK！ Let's play at being animals！ YOU choose！",
                "\"Say 'Let's pretend to be...！' And we'll both do it！\"",
            ],
            "rows":[
                {"child":"说蝴蝶","T_line":"\"BUTTERFLY！ Wings out！ Turn around！ 'I'm a little butterfly！' Say it！\""},
                {"child":"说虫子","T_line":"\"WORM！ Lie down and wriggle！ 'I'm a wriggly worm！' The wigglier the better！\""},
                {"child":"说青蛙","T_line":"\"FROG！ Ribbit！ Jump！ Find a muddy puddle！ 'Frogs love jumping in muddy puddles！'\""},
            ],
        },
        "recast":[
            {"child":"Peppa <u>is</u> a butterfly","correct":"Peppa <strong>was</strong> a butterfly！（过去）/ Peppa <strong>pretended to be</strong> a butterfly！","note":"时态/词汇"},
            {"child":"the worm <u>wriggle</u>","correct":"the worm <strong>wriggles</strong>！","note":"第三人称单数"},
            {"child":"frog <u>jump</u> in puddle","correct":"frogs <strong>jump</strong> in puddles！","note":"复数 frogs + puddles"},
            {"child":"I <u>pretend</u> to be frog","correct":"I <strong>pretended</strong> to be a frog！","note":"过去式 + 冠词 a"},
            {"child":"Grandpa <u>show</u> me how","correct":"Grandpa <strong>showed</strong> me how！","note":"规则过去式 showed"},
        ],
    },

    phase4={
        "tpr":[
            {"command":"\"Be a butterfly！ Fly！\"","action":"双臂展开，轻盈地转圈，踮脚尖，\"I'm a beautiful butterfly！\""},
            {"command":"\"Be a wriggly worm！\"","action":"弯腰，全身扭来扭去，\"I'm a wriggly worm！ Wriggle wriggle！\""},
            {"command":"\"Be a FROG！ Ribbit！\"","action":"蹲低，双手撑膝盖，跳起，\"Ribbit！ Ribbit！\""},
            {"command":"\"Wriggle like a worm！ Faster！\"","action":"越来越快地扭动，停不下来，\"Wriggle wriggle wriggle！\""},
            {"command":"\"Jump in the muddy puddle！\"","action":"使劲跳，假装溅出泥水，\"SPLASH！ I'm a frog！\""},
            {"command":"\"Frogs love muddy puddles！\"","action":"蹲下，欢快地跳，\"BEST ANIMAL EVER！\""},
        ],
        "dubbing":[
            {"num":1,"time":"约第1分30秒","scene":"Peppa 展开双臂，优雅地说自己是美丽的蝴蝶，George 跟着也想当蝴蝶。",
             "l1":"I'm a butterfly！","l1_note":"展开双臂，做出转圈动作","l2":"Pretty butterfly！ Watch me！","l3":"\"I'm a little butterfly！ A beautiful butterfly！ George, butterflies are very elegant！\""},
            {"num":2,"time":"约第2分30秒","scene":"Grandpa Pig 示范当虫子，躺地上扭来扭去，非常夸张。",
             "l1":"Wriggle wriggle！","l1_note":"全身扭动","l2":"I'm a worm！ Look！","l3":"\"First you lie down! Then you wriggle! I'm a wriggly worm! This is great fun！\""},
            {"num":3,"time":"约第3分钟","scene":"Peppa 问有什么游戏是青蛙玩的，Grandpa 说青蛙喜欢跳泥坑。",
             "l1":"Frogs？ Puddles？！","l1_note":"先疑惑，然后恍然大悟","l2":"Frogs jump in puddles！ Yes！","l3":"\"Frogs love jumping in muddy puddles！ Wait — that's MY favourite game！ I want to be a frog！\""},
            {"num":4,"time":"约第4分30秒","scene":"全家都变成青蛙，在泥坑里使劲跳，大家都笑了。",
             "l1":"Ribbit！ SPLASH！","l1_note":"蹲下跳，最开心的表情","l2":"I'm a frog！ Best animal！","l3":"\"Butterflies and worms are very nice. But I like frogs the best！ Ribbit！\""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"Peppa: I'm a little DINOSAUR. I'm a little dinosaur！","answer":"BUTTERFLY！",
             "correct_line":"I'm a little <strong>butterfly</strong>. I'm a little butterfly！"},
            {"num":2,"is_trap":False,
             "bug_line":"Grandpa Pig: First, you have to lie down on the ground. Then, you SLEEP.","answer":"WRIGGLE！",
             "correct_line":"Then, you <strong>wriggle</strong> around. I'm a wriggly worm！"},
            {"num":3,"is_trap":True,
             "bug_line":"Frogs love jumping in muddy puddles.","answer":"","correct_line":""},
            {"num":4,"is_trap":False,
             "bug_line":"Peppa: Butterflies and worms are very nice. But I like SNAKES the best.","answer":"FROGS！",
             "correct_line":"But I like <strong>frogs</strong> the best."},
            {"num":5,"is_trap":False,
             "bug_line":"Grandpa Pig: Do you know what game frogs love？ Swimming！","answer":"JUMPING IN MUDDY PUDDLES！",
             "correct_line":"Frogs love <strong>jumping in muddy puddles</strong>！"},
        ],
    },

    phase5={
        "l1":"Peppa be butterfly. George want butterfly too. Grandpa show worm dance. Then everybody be frog！ Jump puddle！",
        "l1_response":"\"YES！ Jump puddle！ Because frogs...\" 等孩子接 \"love muddy puddles！\"",
        "l2":"Peppa and George visited Grandpa's garden. Peppa pretended to be a butterfly. Grandpa showed them how to be worms. But at the end, everyone became frogs and jumped in muddy puddles！",
        "l2_response":"\"Great！ <em>（Recast）</em> Grandpa <strong>showed</strong> them! And everyone <strong>became</strong> frogs！\"",
        "l3":"Peppa and George visited Grandpa Pig's garden. Peppa was a butterfly and George tried to be one too. Grandpa taught them to be worms instead, wriggling on the ground. But the best animal of all? The frog — because frogs love jumping in muddy puddles！",
        "l3_response":"\"PERFECT！ 'The best animal of all?' — love that question！ Great storytelling！\"",
        "scaffold":[
            {"stuck":"第1句说不出来","rescue":"\"OK, what did Peppa pretend to be？ A... <strong>butterfly</strong>！ Show me the wings！\""},
            {"stuck":"第2句说不出来","rescue":"\"Then Grandpa showed them the worm dance！ Wriggle wriggle！ Say <strong>wriggly worm</strong>！\""},
            {"stuck":"第3句说不出来","rescue":"\"But the best animal is... <em>（跳跳蹦蹦）</em>... <strong>frog</strong>！ Because frogs love...？\""},
            {"stuck":"完全不开口","rescue":"家长先说 L1，做出全套三个动物动作，\"Now YOU say it！ Just three words: butterfly, worm, frog！\""},
        ],
        "roleplay_child":"Peppa（引领游戏）",
        "roleplay_parent":"George（跟着玩）",
        "roleplay_situations":[
            {"label":"孩子展开翅膀","T_line":"\"I'm a butterfly too！ Watch me！ （笨拙地做）Am I pretty？\""},
            {"label":"孩子让家长当虫子","T_line":"\"Worm？ OK... lie down and wriggle！ Tell me: 'I'm a wriggly worm！'\""},
            {"label":"孩子说当青蛙","T_line":"\"FROG！ Because frogs love... <em>（等孩子说）</em>... muddy puddles！ Jump！\""},
        ],
    },

    phase6={
        "phonics_title":"规则：'w' 前缀的特殊变音 — worm 里的 'or' 不说 /ɔː/",
        "phonics_word":"worm /wɜːm/",
        "phonics_mnemonic":"\"w 后面跟 or，偷偷把 /ɔː/ 变成 /ɜː/——就像 worm 在变形！word, work, world, worse——都是这个规律！\"",
        "phonics_table":[
            {"word":"worm","wrong":"worm（/ɔːm/）","right":"/wɜːm/","rule":"w+or → /wɜː/"},
            {"word":"word","wrong":"word（/ɔːd/）","right":"/wɜːd/","rule":"w+or → /wɜː/"},
            {"word":"world","wrong":"world（/ɔːld/）","right":"/wɜːld/","rule":"w+or → /wɜː/"},
            {"word":"worse","wrong":"worse（/ɔːs/）","right":"/wɜːs/","rule":"w+or → /wɜː/"},
        ],
        "next_script":"\"Next time — Peppa finds a box of old clothes！ And she decides to dress up as... someone very familiar. Someone in this room！ Who do you think？\"",
        "next_a":"Daddy Pig！",
        "next_b":"Mummy Pig！",
    },

    checklist=[
        "Phase 1：孩子喊出了上集的词 impossible / BRAVO / George",
        "Phase 2：孩子模仿了蝴蝶、虫子或青蛙的动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 当过考官 + 配音每个画面说过至少 Level 1 + Bugs 少于 2 次扣分",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],

    ammo=[
        {"sentence":"Let's play at being...！","zh":"我们来扮演……吧","usage":"带孩子玩角色扮演时，用这句开场"},
        {"sentence":"I'm a wriggly worm！","zh":"我是一条扭来扭去的虫！","usage":"随时可以用来逗孩子笑，全身扭动"},
        {"sentence":"Frogs love jumping in muddy puddles！","zh":"青蛙喜欢跳泥坑","usage":"下雨天看到泥坑时，用来引导孩子参与"},
        {"sentence":"Which is best？","zh":"哪个最好？","usage":"帮孩子比较选项时的思考框架句"},
    ],
)


# ═══════════════════════════════════════════════════════════════════════════════
# EP 18 · Dressing Up 化装游戏
# ═══════════════════════════════════════════════════════════════════════════════
EP18 = _ep(
    num=18, title_en="Dressing Up", title_zh="化装游戏", color="rose",
    synopsis="Peppa 和 George 在爸妈房间发现旧衣服箱，Peppa 把自己打扮成 Mummy Pig，George 打扮成 Daddy Pig。两人模仿爸妈工作和园艺，Mummy 和 Daddy 差点认不出自己的孩子。最后冰淇淋时间让游戏结束。",

    vocab=[
        {"word":"dress up","phonetic":"/ˌdres ˈʌp/","pos":"phr.v.","zh":"化装/换装","action":"假装穿上大衣、戴上帽子，整理仪态，镜子前端详"},
        {"word":"makeup","phonetic":"/ˈmeɪkʌp/","pos":"n.","zh":"化妆品","action":"假装在脸上涂口红和粉，闭眼陶醉，\"Beautiful！\""},
        {"word":"lipstick","phonetic":"/ˈlɪpstɪk/","pos":"n.","zh":"口红","action":"做出用口红涂嘴唇的动作，噘嘴"},
        {"word":"powder","phonetic":"/ˈpaʊdə/","pos":"n.","zh":"粉底/散粉","action":"假装用粉扑扑粉，吹一口气，粉飞起来"},
        {"word":"pretend","phonetic":"/prɪˈtend/","pos":"v.","zh":"假装/扮演","action":"做出引号手势，\"Just pretend！ Watch！\""},
        {"word":"bored","phonetic":"/bɔːd/","pos":"adj.","zh":"无聊的","action":"无精打采，打哈欠，头靠向一侧，\"Bo-ring...\""},
        {"word":"fooled","phonetic":"/fuːld/","pos":"adj.","zh":"被骗了","action":"做出惊讶地被识破的表情，\"You really had us fooled！\""},
        {"word":"excuse","phonetic":"/ɪkˈskjuːz/","pos":"n./v.","zh":"打扰一下","action":"礼貌地抬手，假装打断别人，\"Excuse me！ I beg your pardon！\""},
    ],

    patterns=[
        {"pattern":"I'm not Peppa. I'm Mummy Pig！","zh":"我不是Peppa，我是Mummy Pig！","example":"Peppa: I beg your pardon？ I'm not Peppa Pig. I'm Mummy Pig."},
        {"pattern":"I beg your pardon？","zh":"你说什么？（礼貌反问）","example":"Peppa（扮演 Mummy Pig）用这句来提醒别人她在扮演角色"},
        {"pattern":"You really had us fooled！","zh":"你们真的骗到我们了！","example":"Daddy Pig: You really had us fooled."},
        {"pattern":"I've got a lot of work to do.","zh":"我有很多工作要做","example":"Peppa 扮演 Mummy Pig 时说"},
    ],

    goals={
        "min":"孩子能模仿化妆动作并说 \"I'm Mummy/Daddy Pig！\"",
        "mid":"孩子能说一句保持角色的话，比如 \"I beg your pardon？ I'm Mummy Pig！\"",
        "ideal":"孩子主动用 <strong>\"You really had us fooled！\"</strong> 或 <strong>\"I beg your pardon？\"</strong>",
    },

    phase1={
        "review_intro":"上集（第17集《Frogs and Worms and Butterflies》）孩子学过 <code>pretend</code> 和 <code>wriggly worm</code>。用故意说错触发：",
        "review_script":"\"上次 Peppa 最喜欢当虫子，一直在地上扭来扭去！\"（说错动物）",
        "review_response":"孩子会喊：\"不对！Peppa 最喜欢当<strong>青蛙</strong>（frog）！因为青蛙可以跳泥坑！\"",
        "preview_intro":"家长突然举起一件想象中的大衣，神神秘秘地问孩子——",
        "preview_script":"\"Today！ Peppa and George find a box of old clothes. And Peppa puts on... （假装在脸上涂口红） Mummy's lipstick. And Daddy's hat. And she walks around saying... 'I'm not Peppa. I am MUMMY PIG.' （用深沉的声音）\"",
        "preview_mission":"\"Your mission: does Mummy Pig know it's actually Peppa？ Watch carefully！\"",
    },

    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":"👒","bg":"rose","trigger":"Peppa 打开旧衣服箱","action":"家长做出惊喜地打开宝箱的动作，\"Wow！ Old clothes！\""},
            {"emoji":"💄","bg":"pink","trigger":"Peppa 涂口红化妆","action":"家长做出化妆动作，噘嘴，端详镜子中的自己，满意地点头"},
            {"emoji":"🍦","bg":"yellow","trigger":"Mummy 端来冰淇淋，游戏结束","action":"家长做出端冰淇淋的动作，等孩子的反应"},
        ],
    },

    phase3={
        "intro":"全程聊天，不是考试。家长读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":"\"So... did Daddy and Mummy recognize Peppa and George？ YES or NO？\"",
            "note":"",
            "rows":[
                {"child":"\"No！\"","parent":"\"They didn't recognize their own children！ Peppa said: 'I'm Mummy Pig！' And Daddy said...\" 等孩子接"},
                {"child":"\"Yes！\"","parent":"（假装困惑）\"They recognized them？ Then why did Daddy say 'You really had us FOOLED'？\""},
                {"child":"不说话","parent":"家长做出 Daddy 遇到穿着打扮成 Mummy/Daddy 的 Peppa 的惊讶场景，\"Did they recognize？ YES or NO？\""},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":"\"Was Peppa a good Mummy Pig... or did she forget to stay in character？\"",
            "note":"",
            "rows":[
                {"child":"说好","parent":"\"She was pretty good！ 'I beg your pardon？ I'm Mummy Pig！' Very Mummy Pig! But what about when the ice cream came？\""},
                {"child":"说忘了","parent":"（笑）\"She dropped the act for ice cream！ Very Peppa of her！ Would YOU drop your character for ice cream？\""},
                {"child":"两个都","parent":"\"Exactly！ She was good... until the ice cream! That's Peppa for you！\""},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":"\"If YOU could dress up as ANYONE, who would you pretend to be？\"",
            "note":"",
            "rows":[
                {"child":"说家人","parent":"\"Me？ Or Mummy？ Show me how you'd walk! Talk! What would you say？\""},
                {"child":"说超级英雄/动画人物","parent":"\"[角色名]！ Show me the signature move！ What's their famous line？\""},
                {"child":"说老师","parent":"\"Teacher！ 'Class, quiet please！' Would YOU be a strict teacher？ Or a fun teacher？\""},
                {"child":"不说话","parent":"家长假装是孩子，\"Hello！ I am [孩子名]！ I love [孩子喜欢的东西]！\" — 等孩子纠正"},
            ],
        },
        "personal":{
            "intro":"把角色扮演和孩子的生活挂钩。",
            "script_lines":[
                "\"Have YOU ever pretended to be ME...？\"",
                "（指着自己，等孩子反应）",
                "\"What would you SAY？ What would you DO？\"",
            ],
            "rows":[
                {"child":"模仿家长","parent":"\"Show me！ What am I like？ Do I sound like this？\" （夸张版自我模仿）"},
                {"child":"笑着摇头","parent":"\"No？ Come on！ If YOU were me, right now, what would you say to yourself？\""},
                {"child":"说话了","parent":"\"That's me？! I don't sound like that！ （假装生气，然后笑）That's pretty accurate actually.\""},
                {"child":"问家长","parent":"\"You want ME to be YOU？ Ok. 'I love playing and I want ice cream and I never want to go to bed！'\""},
            ],
        },
        "role_play":{
            "intro":"孩子扮演 Mummy 或 Daddy Pig，家长扮演自己（Peppa 的视角）。",
            "script_lines":[
                "\"YOU are Mummy Pig. I am Peppa.",
                "\"I will pretend I don't know it's you！\"",
            ],
            "rows":[
                {"child":"做出工作状","T_line":"\"Hello！ Are you... Mummy Pig？\" （等孩子回答）\"Oh！ Of course！ Sorry！ What are you working on？\""},
                {"child":"说不对","T_line":"\"Wait — if you're Mummy Pig, say 'I beg your pardon？' when someone calls you Peppa！\""},
                {"child":"保持角色","T_line":"\"You really had us fooled！ You're a GREAT Mummy Pig！\""},
            ],
        },
        "recast":[
            {"child":"Peppa <u>wear</u> Mummy's dress","correct":"Peppa <strong>wore</strong> Mummy's dress！","note":"不规则过去式 wore"},
            {"child":"she <u>put</u> lipstick on","correct":"she put <strong>the</strong> lipstick on！","note":"定冠词 the"},
            {"child":"Daddy <u>can't</u> recognize them","correct":"Daddy <strong>couldn't</strong> recognize them！","note":"过去式 couldn't"},
            {"child":"she <u>is</u> Mummy Pig","correct":"she <strong>pretended to be</strong> Mummy Pig！","note":"更准确的表达"},
            {"child":"George <u>look</u> like Daddy","correct":"George <strong>looked</strong> like Daddy！","note":"规则过去式"},
        ],
    },

    phase4={
        "tpr":[
            {"command":"\"Put on Mummy's hat！\"","action":"双手把想象的大帽子戴在头上，整理，然后照镜子端详"},
            {"command":"\"Apply the lipstick！\"","action":"做出涂口红的动作，噘嘴，然后满意地点头"},
            {"command":"\"I am NOT Peppa！ I am MUMMY PIG！\"","action":"挺胸，用夸张低沉的声音说 \"I beg your pardon？ I am Mummy Pig！\""},
            {"command":"\"I've got a lot of work to do！\"","action":"做出假装在电脑前工作的样子，接电话，\"Do this！ Do that！ Goodbye！\""},
            {"command":"\"You really had us fooled！\"","action":"做出被识破后惊讶的表情，然后笑着竖起大拇指"},
            {"command":"\"Ice cream！\"","action":"立刻放下所有装扮，手举高，大喊 \"ICE CREAM！ I want ice cream！\""},
        ],
        "dubbing":[
            {"num":1,"time":"约第1分钟","scene":"Peppa 打开旧衣服箱，发现 Daddy 的帽子和 Mummy 的裙子，决定化装。",
             "l1":"Wow！","l1_note":"惊喜地拿起衣服","l2":"Old clothes！ Let's dress up！","l3":"\"Wow！ Daddy's hat！ And Mummy's dress！ George, let's dress up and pretend to be Mummy and Daddy！\""},
            {"num":2,"time":"约第2分30秒","scene":"打扮好的 Peppa 遇到 Mummy，用 \"I beg your pardon\" 保持角色。",
             "l1":"I beg your pardon？","l1_note":"用假装严肃的声音","l2":"I'm Mummy Pig！ Not Peppa！","l3":"\"I beg your pardon？ I am not Peppa Pig. I am Mummy Pig. And I have a lot of work to do！\""},
            {"num":3,"time":"约第3分30秒","scene":"Daddy Pig 在花园里挖洞，Peppa（扮成 Mummy）来视察。",
             "l1":"Daddy Pig！","l1_note":"用\"家长\"的语气叫","l2":"Be careful！ Don't get dirty！","l3":"\"Daddy Pig！ I hope you are not digging in your best clothes！ That is a very deep hole！\""},
            {"num":4,"time":"约第5分钟","scene":"Mummy 端来冰淇淋，Peppa 立刻忘记扮演，大喊 \"我们在这里！\"",
             "l1":"Ice cream！！","l1_note":"马上破功，尖叫跑过去","l2":"Here we are！ It's us！","l3":"\"We were just pretending to be you and Daddy！ You really had us fooled！ Now can we have ice cream？\""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"Peppa: First, some KETCHUP. Lovely.","answer":"POWDER！",
             "correct_line":"First, some <strong>powder</strong>. Lovely."},
            {"num":2,"is_trap":False,
             "bug_line":"Peppa: Hello！ Yes. Do this. Do that. No thank you. DANCE！","answer":"GOODBYE！",
             "correct_line":"Hello！ Yes. Do this. Do that. No, thank you. <strong>Goodbye！</strong>"},
            {"num":3,"is_trap":True,
             "bug_line":"You really had us fooled.","answer":"","correct_line":""},
            {"num":4,"is_trap":False,
             "bug_line":"Daddy Pig: You really had us SCARED.","answer":"FOOLED！",
             "correct_line":"You really had us <strong>fooled</strong>."},
            {"num":5,"is_trap":False,
             "bug_line":"Mummy Pig: Hello, Peppa. Hello, GRANDPA.","answer":"GEORGE！",
             "correct_line":"Hello, Peppa. Hello, <strong>George</strong>."},
        ],
    },

    phase5={
        "l1":"Peppa find old clothes. She dress up Mummy Pig. George is Daddy Pig. Mummy and Daddy fooled！",
        "l1_response":"\"YES！ Fooled！ And then what broke the game？\" 等孩子说\"冰淇淋！\"",
        "l2":"Peppa and George found a box of old clothes. Peppa dressed up as Mummy Pig with makeup and everything. They fooled Mummy and Daddy！ Until ice cream arrived.",
        "l2_response":"\"Great！ <em>（Recast）</em> Peppa <strong>dressed up</strong> as Mummy Pig！ And they <strong>fooled</strong> them！\"",
        "l3":"Peppa and George discovered a box of old clothes in Mummy and Daddy's room. Peppa put on Mummy's dress, hat and makeup, while George wore Daddy's coat and hat. They fooled their parents completely — until Mummy brought ice cream and Peppa immediately dropped the act！",
        "l3_response":"\"PERFECT！ 'Dropped the act' — brilliant phrase！ Peppa just can't resist ice cream！\"",
        "scaffold":[
            {"stuck":"第1句说不出来","rescue":"\"OK, what did Peppa find？ Old... <strong>clothes</strong>！ In a box！\""},
            {"stuck":"第2句说不出来","rescue":"\"Then Peppa put on Mummy's... <em>（做涂口红动作）</em>... <strong>makeup</strong>！ And said 'I'm Mummy Pig！'\""},
            {"stuck":"第3句说不出来","rescue":"\"But then Mummy brought... <em>（做端着东西的动作）</em>... <strong>ice cream</strong>！ And Peppa forgot the game！\""},
            {"stuck":"完全不开口","rescue":"家长先说 L1，\"Now YOU say it！ Just say: clothes, dress up, fooled！\""},
        ],
        "roleplay_child":"Mummy Pig（被扮演的）",
        "roleplay_parent":"Peppa（扮演者）",
        "roleplay_situations":[
            {"label":"孩子扮成严肃的Mummy","T_line":"\"Oh！ Mummy Pig！ Is that you？ Are you Peppa？ 'I beg your pardon？ I am Mummy Pig！'\""},
            {"label":"家长叫孩子名字","T_line":"\"Peppa！ — Oh！ Say: 'I beg your pardon？ I am NOT Peppa！'\""},
            {"label":"家长拿出零食","T_line":"\"Are you still Mummy Pig？ Or do you want... （亮出零食） THIS？\""},
        ],
    },

    phase6={
        "phonics_title":"规则：加 -ing 时双写辅音 vs 不双写",
        "phonics_word":"dressing /ˈdresɪŋ/ vs pretending /prɪˈtendɪŋ/",
        "phonics_mnemonic":"\"短元音+单辅音？双写再加ing（running, sitting）。长元音+e结尾？去e加ing（hiding, making）。两个辅音？直接加（dressing, helping）！\"",
        "phonics_table":[
            {"word":"dress → dressing","wrong":"dresiing","right":"/ˈdresɪŋ/","rule":"两个辅音ss，直接加ing"},
            {"word":"run → running","wrong":"runing","right":"/ˈrʌnɪŋ/","rule":"短元音+单辅音，双写"},
            {"word":"hide → hiding","wrong":"hideing","right":"/ˈhaɪdɪŋ/","rule":"长元音+e，去e加ing"},
            {"word":"pretend → pretending","wrong":"pretending（正确！）","right":"/prɪˈtendɪŋ/","rule":"两个辅音nd，直接加ing"},
        ],
        "next_script":"\"Next time — Peppa loses something she wears on her feet. She can't find them anywhere！ And Mummy says... they'll buy NEW ones. What colour do you think Peppa will choose？\"",
        "next_a":"红色！",
        "next_b":"蓝色",
    },

    checklist=[
        "Phase 1：孩子喊出了上集的词 frog / pretend / muddy puddles",
        "Phase 2：孩子做出了化妆或换装的动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 当过考官 + 配音每个画面说过至少 Level 1 + Bugs 少于 2 次扣分",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],

    ammo=[
        {"sentence":"I beg your pardon？","zh":"你说什么？（礼貌问）","usage":"孩子没听清或想让对方重复时，用这句比 \"what？\" 更礼貌"},
        {"sentence":"I'm not [名字]. I am [角色名]！","zh":"我不是...，我是...！","usage":"任何角色扮演游戏的开场白"},
        {"sentence":"You really had us fooled！","zh":"你们真的骗到我们了","usage":"孩子做了一个出人意料的事情之后"},
        {"sentence":"I've got a lot of work to do.","zh":"我有很多工作要做","usage":"孩子模仿大人工作时，或者告诉孩子大人需要时间"},
    ],
)


# ═══════════════════════════════════════════════════════════════════════════════
# EP 19 · New Shoes 新鞋子
# ═══════════════════════════════════════════════════════════════════════════════
EP19 = _ep(
    num=19, title_en="New Shoes", title_zh="新鞋子", color="red",
    synopsis="Peppa 找不到鞋子了，全家都找不到。Mummy 说买新的，Peppa 要红色的。新红鞋太好看了，Peppa 不肯脱，洗澡穿，睡觉穿。第二天下雨，全家穿靴子跳泥坑——Peppa 乖乖换上了靴子。",

    vocab=[
        {"word":"smart","phonetic":"/smɑːt/","pos":"adj.","zh":"漂亮的/帅气的","action":"整理仪态，打量自己一番，满意地竖大拇指，\"Looking smart！\""},
        {"word":"flowerbed","phonetic":"/ˈflaʊəbed/","pos":"n.","zh":"花坛","action":"蹲下，假装在花坛里找东西，翻来翻去"},
        {"word":"wheelbarrow","phonetic":"/ˈwiːlbærəʊ/","pos":"n.","zh":"独轮车","action":"做出推独轮车的动作，前倾，\"Nothing in here！\""},
        {"word":"pajamas","phonetic":"/pəˈdʒɑːməz/","pos":"n.","zh":"睡衣","action":"假装穿睡衣，揉眼睛，打哈欠，\"Time for bed！\""},
        {"word":"boots","phonetic":"/buːts/","pos":"n.","zh":"靴子","action":"假装用力把靴子踩进泥里，\"STOMP STOMP！\""},
        {"word":"proper","phonetic":"/ˈprɒpə/","pos":"adj.","zh":"合适的/像样的","action":"摆出正式的姿势，用严肃的声音说 \"Proper shoes！\""},
        {"word":"lost","phonetic":"/lɒst/","pos":"adj.","zh":"丢失的","action":"双手一摊，四处张望，\"Where are they？ Lost！ Gone！\""},
        {"word":"pair","phonetic":"/peə/","pos":"n.","zh":"一双","action":"把两只手并在一起，\"A pair！ Two！ Together！\""},
    ],

    patterns=[
        {"pattern":"They make you look very smart.","zh":"它们让你看起来非常好看","example":"Mummy Pig: They make you look very smart."},
        {"pattern":"I don't want to ever take my shoes off！","zh":"我永远都不想脱鞋！","example":"Peppa: I like my new shoes so much. I don't want to ever take them off."},
        {"pattern":"If you jump in muddy puddles, you must wear your boots！","zh":"如果你要跳泥坑，你必须穿靴子！","example":"Peppa: If you jump in muddy puddles, you must wear your boots."},
        {"pattern":"We'll buy you a new pair！","zh":"我们给你买新的一双！","example":"Mummy Pig: We'll buy you a new pair."},
    ],

    goals={
        "min":"孩子能说 \"New shoes！ Red shoes！\" 并做出穿鞋的动作",
        "mid":"孩子能说 Peppa 的一句台词：I don't want to take them off！",
        "ideal":"孩子主动用 <strong>\"If you jump in muddy puddles, you must wear your boots！\"</strong>",
    },

    phase1={
        "review_intro":"上集（第18集《Dressing Up》）孩子学过 <code>dress up</code> 和 <code>fooled</code>。用故意说错触发：",
        "review_script":"\"上次 Peppa 穿上了妈妈的旧衣服，Mummy 和 Daddy 立刻认出了她，说'你是Peppa！'\"（说错结果）",
        "review_response":"孩子会喊：\"不对！他们<strong>没认出来</strong>！Peppa 真的<strong>骗到了</strong>他们！\"",
        "preview_intro":"家长假装到处找东西，掀沙发垫，翻包，越来越着急——",
        "preview_script":"\"Today！ Peppa has LOST something very important. Something she wears... on her FEET！ （指脚）And everyone is searching... （搜遍各处）...but they're NOWHERE to be found！ But wait... this might be a good thing！ Why？\"",
        "preview_mission":"\"Your mission while watching: which colour shoes does Peppa choose？ Red？ Blue？ Remember！\"",
    },

    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":"🔍","bg":"red","trigger":"全家到处找鞋","action":"家长假装认真搜索，掀垫子，看花盆里，一脸认真"},
            {"emoji":"👟","bg":"pink","trigger":"Peppa 得到新红鞋","action":"家长做出爱不释手、捧着宝贝的动作，\"So beautiful！\""},
            {"emoji":"🌧️","bg":"blue","trigger":"下雨了，大家换靴子跳泥坑","action":"家长做出穿靴子的动作，然后开心地假装跳进泥坑"},
        ],
    },

    phase3={
        "intro":"全程聊天，不是考试。家长读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":"\"So... did Peppa EVER take her new shoes off？ YES or NO？\"",
            "note":"",
            "rows":[
                {"child":"\"No！\"","parent":"\"NO！ She wore them in the BATH！ She wore them to BED！ She wore them... everywhere！ Until...？\"（等孩子说泥坑/靴子）"},
                {"child":"\"Yes！\"","parent":"（假装惊讶）\"She took them off？ When？ Was it for bath time？ Or for the muddy puddle？ Or for bed？\""},
                {"child":"不说话","parent":"家长做出洗澡穿鞋、睡觉穿鞋、起床穿鞋的夸张动作，\"Did she EVER take them off？ YES or NO？\""},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":"\"Was Peppa being sensible... or was she being a bit silly about her shoes？\"",
            "note":"",
            "rows":[
                {"child":"说 silly","parent":"\"SILLY！ Wearing shoes in the bath！ In bed！ But she loved them SO much！ Have YOU ever loved something so much？\""},
                {"child":"说 sensible","parent":"（假装思考）\"Sensible？ In the BATH？ Hmm... I suppose they'd stay clean in the bath... No, that's still silly！\""},
                {"child":"两个都","parent":"\"She was sensible about WHICH shoes — red！ And silly about WHEN to wear them — always！\""},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":"\"Is there anything YOU love SO much that you never want to take it off or put it down？\"",
            "note":"",
            "rows":[
                {"child":"说玩具/游戏机","parent":"\"YES！ Like how Peppa loved her shoes！ Would YOU wear it to bed？ To the bath？\""},
                {"child":"说衣服","parent":"\"Oh！ A favourite T-shirt！ I totally get it！ Would you wear it every single day if you could？\""},
                {"child":"说没有","parent":"\"Nothing？ You're very reasonable！ More reasonable than Peppa！ （假装崇拜）\""},
                {"child":"问问题","parent":"家长做出Peppa穿着新鞋做各种活动的动作，\"Like this？ Shoes in the bath？ Shoes in bed？\""},
            ],
        },
        "personal":{
            "intro":"把买新东西、不舍得用的心情跟孩子挂钩。",
            "script_lines":[
                "\"Have YOU ever got something NEW...\"",
                "（做出新东西的惊喜样子）",
                "\"...and not wanted to TOUCH it in case you break it or dirty it？\"",
            ],
            "rows":[
                {"child":"说有","parent":"\"YES！ Just like Peppa！ But she did the opposite — she wore them EVERYWHERE！\""},
                {"child":"说没有","parent":"\"No？ You use your things right away？ That's brave！ Peppa went the other extreme！\""},
                {"child":"说新玩具","parent":"\"A new toy！ Did you play with it straight away？ Or did you just admire it？\""},
                {"child":"不说话","parent":"家长做出捧着新东西舍不得用的样子，\"Like this？ 'I can't use it — it's too beautiful！'\""},
            ],
        },
        "role_play":{
            "intro":"孩子扮演 Peppa（超级爱新鞋），家长扮演 Mummy 或 Daddy Pig。",
            "script_lines":[
                "\"Peppa！ It's bath time！ Take your shoes off！\"",
            ],
            "rows":[
                {"child":"假装不肯脱","T_line":"\"Say: 'I don't want to take them off！ Not EVER！'\""},
                {"child":"扮演拒绝","T_line":"\"Say it properly: 'I like my new shoes so much. I don't want to EVER take them off！'\""},
                {"child":"假装跳泥坑","T_line":"\"Wait! Before you jump — what should you be wearing？ Say: 'If you jump in muddy puddles, you must wear your... boots！'\""},
            ],
        },
        "recast":[
            {"child":"Peppa <u>lose</u> her shoes","correct":"Peppa <strong>lost</strong> her shoes！","note":"不规则过去式 lost"},
            {"child":"she <u>buyed</u> new shoes","correct":"she <strong>bought</strong> new shoes！","note":"不规则过去式 bought"},
            {"child":"the shoes is red","correct":"the shoes <strong>are</strong> red！","note":"shoes 是复数用 are"},
            {"child":"she <u>wear</u> them to bed","correct":"she <strong>wore</strong> them to bed！","note":"不规则过去式 wore"},
            {"child":"she put on the <u>boot</u>","correct":"she put on the <strong>boots</strong>！","note":"复数 boots"},
        ],
    },

    phase4={
        "tpr":[
            {"command":"\"Peppa！ Where are your shoes？ They're LOST！\"","action":"双手一摊，四处张望，\"Lost！ Nowhere！ Oh no！\""},
            {"command":"\"Try on your new RED shoes！\"","action":"假装穿上新鞋，站起来，左右看脚，\"Beautiful！ I love them！\""},
            {"command":"\"I don't EVER want to take them off！\"","action":"抱着脚，死不松手，夸张地说 \"NEVER！ Not EVER！\""},
            {"command":"\"Bath time！ Keep your shoes on！\"","action":"假装在浴缸里，脚抬起来，确保鞋子不沾水，\"Careful！\""},
            {"command":"\"It's raining！ Put on your BOOTS！\"","action":"快速假装换靴子，踩脚，做好跳泥坑的准备"},
            {"command":"\"If you jump in muddy puddles, you must wear your boots！\"","action":"用手指指地，用 Peppa 的严肃语气说这句话"},
        ],
        "dubbing":[
            {"num":1,"time":"约第2分钟","scene":"全家到处找 Peppa 的鞋，翻花坛、独轮车、花盆，都没有。",
             "l1":"Not here！","l1_note":"一个接一个搜索，越来越沮丧","l2":"Can't find them！ Lost！","l3":"\"We've looked everywhere！ In the flowerbed！ In the wheelbarrow！ In the flowerpots！ They're GONE！\""},
            {"num":2,"time":"约第3分钟","scene":"Peppa 得到新的红鞋，立刻爱上了，到处展示给人看。",
             "l1":"RED shoes！！","l1_note":"指着新鞋，激动地跳","l2":"New red shoes！ Look！","l3":"\"Daddy！ Look at my new shoes！ They're RED！ Do you like them？ Aren't they beautiful？\""},
            {"num":3,"time":"约第4分钟","scene":"睡前，Peppa 还穿着新鞋不肯脱，Mummy 无奈。",
             "l1":"Not taking them off！","l1_note":"双脚缩起来，保护新鞋","l2":"I love them！ Won't take off！","l3":"\"I like my new shoes so much. I don't want to EVER take them off！ Not even for bed！\""},
            {"num":4,"time":"约第5分钟","scene":"下雨，全家穿靴子，Peppa 换靴子去跳泥坑，最终宣告靴子规则。",
             "l1":"SPLASH！","l1_note":"最开心的跳泥坑动作","l2":"Boots on！ Jump！","l3":"\"If you jump in muddy puddles, you must wear your boots！ I'm a very sensible Peppa Pig！\""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"Mummy Pig: Maybe we should try the ATTIC.","answer":"GARDEN！",
             "correct_line":"Maybe we should try the <strong>garden</strong>."},
            {"num":2,"is_trap":False,
             "bug_line":"Mummy Pig: They make you look very TALL.","answer":"SMART！",
             "correct_line":"They make you look very <strong>smart</strong>."},
            {"num":3,"is_trap":True,
             "bug_line":"If you jump in muddy puddles, you must wear your boots.","answer":"","correct_line":""},
            {"num":4,"is_trap":False,
             "bug_line":"Peppa: I like my new shoes so much. I don't want to ever take them to SCHOOL.","answer":"OFF！",
             "correct_line":"I don't want to ever take them <strong>off</strong>."},
            {"num":5,"is_trap":False,
             "bug_line":"Narrator: Peppa is wearing her new shoes in BED. And her new shoes are BLUE.","answer":"RED！",
             "correct_line":"And her new shoes are <strong>red</strong>."},
        ],
    },

    phase5={
        "l1":"Peppa lose shoes. Buy new red shoes. She love them too much！ Rain come. She wear boots. Jump puddle！",
        "l1_response":"\"YES！ Jump puddle！ And what did she say？ 'If you jump in muddy puddles...' — what？\"",
        "l2":"Peppa lost her old shoes and bought new red ones. She loved them so much she wouldn't take them off. But when it rained, she wore her boots to jump in muddy puddles！",
        "l2_response":"\"Great！ <em>（Recast）</em> She <strong>bought</strong> new ones！ And she <strong>wore</strong> her boots to jump！\"",
        "l3":"Peppa couldn't find her shoes anywhere. So Mummy bought her a brand new pair of red shoes. Peppa loved them so much that she wore them everywhere — even to bed！ But when it rained and everyone put on their boots, Peppa realized that jumping in muddy puddles is always better than pretty shoes.",
        "l3_response":"\"PERFECT！ 'Even to bed' — great detail！ And that last lesson is very Peppa！\"",
        "scaffold":[
            {"stuck":"第1句说不出来","rescue":"\"OK, what did Peppa lose？ Her... <strong>shoes</strong>！ They were... <strong>lost</strong>！\""},
            {"stuck":"第2句说不出来","rescue":"\"Then Mummy bought her NEW shoes！ What colour？ <strong>Red！</strong>\""},
            {"stuck":"第3句说不出来","rescue":"\"But then it rained! And Peppa put on her... <em>（做穿靴子动作）</em>... <strong>boots</strong>！ Jump！ SPLASH！\""},
            {"stuck":"完全不开口","rescue":"家长先说 L1，\"Now YOU say it！ Just say: shoes, red, boots！\""},
        ],
        "roleplay_child":"Peppa（超级爱新鞋）",
        "roleplay_parent":"Mummy（说要洗澡/睡觉）",
        "roleplay_situations":[
            {"label":"孩子假装穿新鞋走路","T_line":"\"Do you like your new shoes？ Are they pretty？ Say 'They make me look very smart！'\""},
            {"label":"家长说脱鞋","T_line":"\"Peppa！ Take off your shoes！ — Say: 'I don't want to EVER take them off！'\""},
            {"label":"家长说下雨了","T_line":"\"It's raining！ Put on your boots！ Why？ Say: 'If you jump in muddy puddles, you must wear your boots！'\""},
        ],
    },

    phase6={
        "phonics_title":"规则：'oo' 的两种读法 — /uː/ vs /ʊ/",
        "phonics_word":"boots /buːts/ vs foot /fʊt/",
        "phonics_mnemonic":"\"'oo' 大多数时候说 /uː/（像吹泡泡）——boots, food, moon, zoo。但有时候任性说 /ʊ/（短促的）——foot, good, look, book！\"",
        "phonics_table":[
            {"word":"boots","wrong":"boots（/ʊ/）","right":"/buːts/","rule":"oo → /uː/"},
            {"word":"shoes","wrong":"shoos","right":"/ʃuːz/","rule":"oe/oe → /uː/"},
            {"word":"foot","wrong":"foot（/uː/）","right":"/fʊt/","rule":"oo → /ʊ/（任性版）"},
            {"word":"good","wrong":"good（/uː/）","right":"/ɡʊd/","rule":"oo → /ʊ/（任性版）"},
        ],
        "next_script":"\"Next time — there's a special day at Peppa's school！ There's face painting, balloons, and bouncy castles！ And Peppa wants to be painted as something FIERCE. What do you think she chooses？\"",
        "next_a":"老虎！Tiger！",
        "next_b":"大象",
    },

    checklist=[
        "Phase 1：孩子喊出了上集的词 dress up / fooled",
        "Phase 2：孩子做出了穿新鞋或穿靴子的动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 当过考官 + 配音每个画面说过至少 Level 1 + Bugs 少于 2 次扣分",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],

    ammo=[
        {"sentence":"They make you look very smart！","zh":"它们让你看起来很好看","usage":"孩子穿了新衣服/新鞋，真心夸他"},
        {"sentence":"I don't want to EVER take it off！","zh":"我永远不想脱掉它！","usage":"孩子爱上某件东西，让他用这句表达"},
        {"sentence":"If you jump in muddy puddles, you must wear your boots！","zh":"要跳泥坑，必须穿靴子！","usage":"下雨天的必备教育句，孩子用这句教大人"},
        {"sentence":"We'll buy you a new pair.","zh":"我们给你买新的一双","usage":"孩子的东西坏了/丢了，安慰他的句子"},
    ],
)


# ═══════════════════════════════════════════════════════════════════════════════
# EP 20 · The School Fete 学校游园会
# ═══════════════════════════════════════════════════════════════════════════════
EP20 = _ep(
    num=20, title_en="The School Fete", title_zh="学校游园会", color="orange",
    synopsis="学校游园会！有画脸、气球、蹦蹦床。Miss Rabbit 只会画老虎，所以全班都变成老虎。Candy Cat 教老虎怎么爬行、跳跃和发出呼噜声。Daddy Pig 保证说有恐龙气球，结果没有——但他用长气球给 George 做了一个！",

    vocab=[
        {"word":"fete","phonetic":"/feɪt/","pos":"n.","zh":"游园会","action":"做出热闹的节日手势，四处张望，\"So many things to do！\""},
        {"word":"face painting","phonetic":"/feɪs ˈpeɪntɪŋ/","pos":"n.","zh":"画脸","action":"用手指假装在脸上画画，然后用镜子照照，\"Wow！\""},
        {"word":"tiger","phonetic":"/ˈtaɪɡə/","pos":"n.","zh":"老虎","action":"弓背，双手张开成爪子，龇牙，低沉地 \"GRRR！\""},
        {"word":"creep","phonetic":"/kriːp/","pos":"v.","zh":"蹑手蹑脚地走","action":"蹲低，双手放地，极慢极安静地向前移动，连呼吸都放轻"},
        {"word":"purr","phonetic":"/pɜː/","pos":"v.","zh":"发出呼噜声","action":"放松，闭眼，发出 \"Purrr...\" 的满足声，像猫一样"},
        {"word":"certain","phonetic":"/ˈsɜːtn/","pos":"adj.","zh":"确定的","action":"点头，双手叉腰，用自信的语气说 \"I am CERTAIN of it！\""},
        {"word":"bouncy castle","phonetic":"/ˈbaʊnsi ˈkɑːsl/","pos":"n.","zh":"充气城堡/蹦蹦床","action":"假装跳蹦蹦床，越跳越高，\"Bounce bounce bounce！\""},
        {"word":"balloon","phonetic":"/bəˈluːn/","pos":"n.","zh":"气球","action":"假装吹一个很大的气球，越吹越大，然后捏着细细的线"},
    ],

    patterns=[
        {"pattern":"I'm certain of it！","zh":"我确定！","example":"Daddy Pig: I'm certain they have dinosaur balloons！（结果没有）"},
        {"pattern":"Tigers creep very very slowly.","zh":"老虎走路非常非常轻","example":"Candy Cat: Tigers creep very very slowly. And then — they jump！"},
        {"pattern":"I don't know how to do elephants. I can do tigers.","zh":"我不会画大象。我会画老虎","example":"Miss Rabbit: I can do tigers."},
        {"pattern":"Best of all, when tigers are happy, they purr.","zh":"最好的是，老虎开心时会发出呼噜声","example":"Candy Cat teaches everyone to be proper tigers."},
    ],

    goals={
        "min":"孩子能做出老虎的动作（爬行+跳+呼噜）",
        "mid":"孩子能说 \"Tigers creep very slowly... and then JUMP！\"",
        "ideal":"孩子主动用 <strong>\"I'm certain of it！\"</strong> 或 <strong>\"Purr...\"</strong> 在日常中使用",
    },

    phase1={
        "review_intro":"上集（第19集《New Shoes》）孩子学过 <code>boots</code> 和 <code>smart</code>。用故意说错触发：",
        "review_script":"\"上次 Peppa 得到了新的蓝色鞋子，她非常喜欢，一直穿着它跳泥坑！\"（两处说错）",
        "review_response":"孩子会喊：\"不对！是<strong>红色</strong>鞋子！而且她换上了<strong>靴子</strong>才去跳泥坑的！\"",
        "preview_intro":"家长做出在脸上画老虎纹的动作，然后蹲低，缓缓爬向孩子——",
        "preview_script":"\"Today！ It's a very special day at Peppa's school！ （做脸部彩绘动作）And by the end... everyone looks like THIS—\" （做出老虎的动作） \"— because Miss Rabbit only knows how to paint one thing！\"",
        "preview_mission":"\"Your mission: who teaches everyone HOW to be a proper tiger？ Remember the name！\"",
    },

    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":"🎨","bg":"orange","trigger":"Miss Rabbit 给所有人画脸","action":"家长做出在别人脸上画画的动作，然后退后端详，\"Perfect tiger！\""},
            {"emoji":"🐯","bg":"yellow","trigger":"Candy Cat 教大家怎么当老虎","action":"家长蹲低，极缓慢地向前爬，然后突然跳起来"},
            {"emoji":"🎈","bg":"blue","trigger":"Daddy 想给 George 买恐龙气球","action":"家长做出认真张望、四处找恐龙气球的动作，越找越慌"},
        ],
    },

    phase3={
        "intro":"全程聊天，不是考试。家长读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":"\"So... did Miss Rabbit paint any faces that were NOT tigers？ YES or NO？\"",
            "note":"",
            "rows":[
                {"child":"\"No！\"","parent":"\"NONE！ She could only paint tigers！ Even Peppa who wanted an ELEPHANT got a tiger！ Ha！\""},
                {"child":"\"Yes！\"","parent":"（假装困惑）\"Really？ What else did she paint？ Did she manage an elephant？ A lion？\"（等孩子说没有）"},
                {"child":"不说话","parent":"家长做出 Peppa 要大象、得到老虎的失望转惊喜表情，\"Only tigers？ YES or NO？\""},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":"\"Who was a better tiger teacher — Candy Cat... or Daddy Pig？\"",
            "note":"（Daddy Pig 根本不会当老虎）",
            "rows":[
                {"child":"选 Candy Cat","parent":"\"CANDY！ She's a CAT — she knows！ Creep slowly, jump, lick yourself, PURR！ Perfect！\""},
                {"child":"选 Daddy Pig","parent":"（假装困惑）\"Daddy Pig？ Was he teaching anyone？ He was busy looking for... DINOSAUR BALLOONS！\""},
                {"child":"两个都","parent":"\"Hmm, Daddy Pig did give George a dinosaur balloon in the end... so maybe? But Candy Cat clearly wins！\""},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":"\"If YOU went to a face painting stall, what would YOU want to be painted as？\"",
            "note":"",
            "rows":[
                {"child":"说动物","parent":"\"[动物名]！ Do you know how a [动物] moves？ Show me！ Can you ROAR？ Or PURR？ Or HISS？\""},
                {"child":"说老虎","parent":"\"TIGER！ Like everyone in the class！ Show me: creep... creep... creep... AND JUMP！\""},
                {"child":"说大象","parent":"\"Like Peppa！ But Miss Rabbit doesn't know how！ （做出Miss Rabbit摊手的样子） 'I can do tigers！'\""},
                {"child":"说恐龙","parent":"（大笑）\"Like GEORGE！ Always！ Can you make a dinosaur face for me？ GRRR！\""},
            ],
        },
        "personal":{
            "intro":"把今天所学的老虎知识和孩子的生活挂钩。",
            "script_lines":[
                "\"Candy Cat says: 'Tigers like to lick themselves clean.'",
                "（做出猫咪舔爪子的动作）",
                "\"Do YOU ever lick yourself clean？ Hehe...\"",
            ],
            "rows":[
                {"child":"做出吃饭舔手指","parent":"\"YES！ Like a tiger！ And when you're happy... do you PURR？\" （做出呼噜声）"},
                {"child":"说不（做不到）","parent":"\"No？ But you do lick ice cream！ And cake！ And your fingers after！ That's pretty tiger！\""},
                {"child":"做出舔动作","parent":"\"TIGER！ Now the full tiger routine: creep... jump... lick clean... PURR！ Do it！\""},
                {"child":"不说话","parent":"家长做出完整的老虎教程，\"Now YOU try！ Tigers creep...\" （等孩子跟着做）"},
            ],
        },
        "role_play":{
            "intro":"孩子扮演老虎，家长是面对老虎的猎物。",
            "script_lines":[
                "\"YOU are a tiger！ I am a... （看向远方）...a very slow wildebeest.",
                "\"Candy Cat says: tigers CREEP... then JUMP！ Ready？\"",
            ],
            "rows":[
                {"child":"开始慢慢爬","T_line":"\"Very very slowly！ Say: 'I am a tiger！ I am creeping！'\""},
                {"child":"跳起来","T_line":"\"JUMP！ You got me！ Now do what tigers do when they're happy！ PURR！\""},
                {"child":"发出呼噜声","T_line":"\"PURR！ Happy tiger！ That was PERFECT！ Best of all — tigers are happy when they catch their prey！\""},
            ],
        },
        "recast":[
            {"child":"Candy <u>teach</u> everyone","correct":"Candy <strong>taught</strong> everyone！","note":"不规则过去式 taught"},
            {"child":"they <u>paint</u> their faces","correct":"they <strong>had</strong> their faces <strong>painted</strong>！","note":"被动语态更准确"},
            {"child":"the tiger is <u>creep</u>","correct":"the tiger <strong>creeps</strong>！","note":"第三人称单数 creeps"},
            {"child":"Daddy <u>buyed</u> a balloon","correct":"Daddy <strong>bought</strong> a balloon！","note":"不规则过去式 bought"},
            {"child":"George <u>get</u> a dinosaur one","correct":"George <strong>got</strong> a dinosaur one！","note":"不规则过去式 got"},
        ],
    },

    phase4={
        "tpr":[
            {"command":"\"I want my face painted！ I want to be a tiger！\"","action":"兴奋地举手，\"Me！ Me！ Paint me as a tiger！ GRRRR！\""},
            {"command":"\"Creep like a tiger！ Very very slowly！\"","action":"蹲低，四肢缓慢移动，每一步都极轻极慢，屏住呼吸"},
            {"command":"\"JUMP！\"","action":"突然从蹲下状态猛地跳起来，\"GRRRR！ GOT YOU！\""},
            {"command":"\"Lick yourself clean！ Like a cat！\"","action":"假装用舌头舔爪子，然后用爪子洗脸，很满足"},
            {"command":"\"When you're happy... PURR！\"","action":"闭眼，发出长长的满足的 \"Purrrrrr...\" 身体微微震动"},
            {"command":"\"I'm CERTAIN they have dinosaur balloons！\"","action":"挺胸，双手叉腰，用 Daddy Pig 的自信语气，\"CERTAIN！ Absolutely CERTAIN！\""},
            {"command":"\"Bounce on the bouncy castle！\"","action":"假装跳蹦蹦床，越跳越高，手举起，\"BOUNCE！ BOUNCE！ WHEEE！\""},
        ],
        "dubbing":[
            {"num":1,"time":"约第2分钟","scene":"Peppa 想被画成大象，但 Miss Rabbit 只会画老虎。",
             "l1":"Tiger？","l1_note":"失望但接受","l2":"Can't do elephant？ Tiger OK！","l3":"\"I wanted an elephant, but I suppose a tiger is fine！ Tigers are actually quite magnificent！\""},
            {"num":2,"time":"约第3分钟","scene":"Candy Cat 教所有人怎么真正当一只老虎。",
             "l1":"Creep... jump！","l1_note":"跟着示范动作","l2":"Creep slowly... then JUMP！","l3":"\"Tigers creep very very slowly... and then they POUNCE！ And best of all — tigers PURR！\""},
            {"num":3,"time":"约第4分钟","scene":"Daddy Pig 到处找恐龙气球，找不到，Madame Gazelle 没有。",
             "l1":"Oh...","l1_note":"Daddy 的失望脸","l2":"No dinosaur balloon！ Oh no！","l3":"\"I was CERTAIN there would be dinosaur balloons！ I was so certain！ What do we do for George？\""},
            {"num":4,"time":"约第5分钟","scene":"Daddy 用长气球扭出恐龙形状，George 惊喜。",
             "l1":"Dinosaur！！","l1_note":"George 的惊喜表情","l2":"It IS a dinosaur！ Grrr！","l3":"\"Daddy Pig made a dinosaur balloon！ It's not perfect, but George loves it！ GRRR！\""},
        ],
        "bugs":[
            {"num":1,"is_trap":False,
             "bug_line":"Miss Rabbit: Oh dear, I don't know how to do DINOSAURS. I can do tigers.","answer":"ELEPHANTS！",
             "correct_line":"Oh dear, I don't know how to do <strong>elephants</strong>. I can do tigers."},
            {"num":2,"is_trap":False,
             "bug_line":"Candy Cat: Tigers creep very very slowly. And then, they SLEEP.","answer":"JUMP！",
             "correct_line":"And then, they <strong>jump</strong>！ Grrr！"},
            {"num":3,"is_trap":True,
             "bug_line":"I'm certain of it.","answer":"","correct_line":""},
            {"num":4,"is_trap":False,
             "bug_line":"Candy Cat: Best of all, when tigers are happy, they ROAR.","answer":"PURR！",
             "correct_line":"Best of all, when tigers are happy, they <strong>purr</strong>."},
            {"num":5,"is_trap":False,
             "bug_line":"Daddy Pig: I've got an idea. We'll make George a DINOSAUR CAKE with the balloons.","answer":"（气球做恐龙形状！not cake）BALLOON DINOSAUR！",
             "correct_line":"Daddy Pig used the long balloons to make George a <strong>dinosaur balloon</strong>！"},
        ],
    },

    phase5={
        "l1":"School have fun day. Everyone paint tiger face. Candy Cat teach tiger walk. Daddy make dinosaur balloon for George！",
        "l1_response":"\"YES！ And how does a tiger walk？ Can you show me？ Creep... creep... JUMP！\"",
        "l2":"It was the school fete. Miss Rabbit painted everyone as tigers because that's all she could do. Candy Cat taught them to creep and purr. Daddy made a dinosaur balloon for George！",
        "l2_response":"\"Great！ <em>（Recast）</em> Miss Rabbit <strong>painted</strong> them all！ And Candy Cat <strong>taught</strong> them！\"",
        "l3":"The school fete had face painting, balloons, and bouncy castles. Miss Rabbit painted everyone as tigers since she couldn't do elephants. Candy Cat gave the class a full tiger lesson — how to creep, jump, and purr. Meanwhile, Daddy Pig was certain there would be dinosaur balloons for George, but there weren't — so he made one himself！",
        "l3_response":"\"PERFECT！ 'Full tiger lesson' — brilliant！ And the detail about Daddy Pig being wrong — great memory！\"",
        "scaffold":[
            {"stuck":"第1句说不出来","rescue":"\"OK, what was special about today？ School... <strong>fete</strong>！ What did they do？ <strong>Face painting！</strong>\""},
            {"stuck":"第2句说不出来","rescue":"\"And what did EVERYONE look like？ <em>（做出老虎脸）</em> <strong>Tigers</strong>！ Because Miss Rabbit only knows tigers！\""},
            {"stuck":"第3句说不出来","rescue":"\"And George's special balloon? Daddy made a... <em>（做出 GRRR）</em>... <strong>dinosaur</strong>！\""},
            {"stuck":"完全不开口","rescue":"家长先说 L1，\"Now YOU say it！ Just say: fete, tiger, dinosaur！\""},
        ],
        "roleplay_child":"Candy Cat（教老虎的那个）",
        "roleplay_parent":"老虎学生（跟着学）",
        "roleplay_situations":[
            {"label":"孩子做出爬行动作","T_line":"\"Creep！ Very very slowly！ Say: 'Tigers creep very very slowly！'\""},
            {"label":"孩子突然跳起来","T_line":"\"JUMP！ YES！ Now say: 'And then — they JUMP！ GRRR！'\""},
            {"label":"孩子做满足的样子","T_line":"\"Best of all — say it! 'Best of all, when tigers are happy... they PURR！'\""},
        ],
    },

    phase6={
        "phonics_title":"规则：soft 'c' — 'c' 在 e, i, y 前发 /s/",
        "phonics_word":"face /feɪs/ · certain /ˈsɜːtn/",
        "phonics_mnemonic":"\"c 遇到 e, i, y，就变温柔，说 /s/——face, ice, city, pencil, dance！ 遇到 a, o, u 还是硬邦邦的 /k/！\"",
        "phonics_table":[
            {"word":"face","wrong":"face（/k/）","right":"/feɪs/","rule":"c+e → /s/"},
            {"word":"certain","wrong":"certain（/k/）","right":"/ˈsɜːtn/","rule":"c+e → /s/"},
            {"word":"dance","wrong":"danke","right":"/dɑːns/","rule":"c+e → /s/"},
            {"word":"city","wrong":"kity","right":"/ˈsɪti/","rule":"c+i → /s/"},
        ],
        "next_script":"\"That's the end of our adventure through episodes 10 to 20！ Which episode was YOUR favourite？ Gardening？ Kite？ Picnic？ Or becoming a tiger at the school fete？\"",
        "next_a":"Picnic（黄蜂追人太好笑了）",
        "next_b":"Musical Instruments（George 吹响了号角）",
    },

    checklist=[
        "Phase 1：孩子喊出了上集的词 red shoes / boots",
        "Phase 2：孩子做出了老虎爬行、跳跃或呼噜声",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 当过考官 + 配音每个画面说过至少 Level 1 + Bugs 少于 2 次扣分",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],

    ammo=[
        {"sentence":"I'm certain of it！","zh":"我确定！","usage":"说完以后假装 Daddy Pig，然后等事情出错，笑着说 'Well... almost certain'"},
        {"sentence":"Tigers creep very very slowly.","zh":"老虎走路非常轻","usage":"叫孩子安静走路时，\"Creep like a tiger！ Very very slowly！\""},
        {"sentence":"Best of all, when tigers are happy, they purr.","zh":"最好的是，老虎开心时会发出呼噜声","usage":"孩子开心时，说\"Are you a happy tiger？ Show me your PURR！\""},
        {"sentence":"I don't know how to do that. But I can do...！","zh":"我不会那个，但我会...！","usage":"诚实承认局限性，然后展示自己擅长的"},
    ],
)



# ── 自动生成：EP01-09 和 EP21-52 数据 ────────────────────────────────────────


# ═══════════════════════════════════════════════════════════════════════════════
# EP 01 · Muddy Puddles 泥坑
# ═══════════════════════════════════════════════════════════════════════════════
EP01 = _ep(
    num=1, title_en='Muddy Puddles', title_zh='泥坑', color='blue',
    synopsis='Peppa 最爱跳泥坑！雨停后，她和 George 穿上靴子，在花园里找到各种大大小小的泥坑，跳得满身是泥。最后连 Mummy 和 Daddy 都一起跳起来了。',
    vocab=[        {"word":'muddy',"phonetic":'ˈmʌdi',"pos":'adj.',"zh":'泥泞的',"action":'指地板或鞋子，皱眉摇头，"Ewww, muddy！"'},        {"word":'puddle',"phonetic":'ˈpʌdl',"pos":'n.',"zh":'水坑',"action":'用手指画一个圆，"A puddle — round, full of water and MUD"'},        {"word":'boots',"phonetic":'buːts',"pos":'n.',"zh":'靴子',"action":'拍自己的腿，从脚踝到膝盖，"Boots go all the way up here"'},        {"word":'jump',"phonetic":'dʒʌmp',"pos":'v.',"zh":'跳',"action":'原地跳一下，双脚落地，停顿'},        {"word":'outside',"phonetic":'ˌaʊtˈsaɪd',"pos":'adv.',"zh":'外面',"action":'手指向门，"Outside — the garden, the sky!"'},        {"word":'safe',"phonetic":'seɪf',"pos":'adj.',"zh":'安全的',"action":'双手托胸，保护姿态，"Is it safe？ Check first！"'},        {"word":'mess',"phonetic":'mes',"pos":'n.',"zh":'脏乱',"action":'指自己，双手摊开，"Look at this mess！"'},        {"word":'clean',"phonetic":'kliːn',"pos":'v.',"zh":'弄干净',"action":'假装洗手，从泥手变干净手'},    ],
    patterns=[        {"pattern":'If you jump in muddy puddles, you must wear your boots.',"zh":'跳泥坑必须穿靴子',"example":'If you go outside in the rain, you must wear your boots.'},        {"pattern":'I love muddy puddles.',"zh":'我爱泥坑',"example":'I love jumping in muddy puddles so much!'},        {"pattern":"I must check if it's safe for you.","zh":'我得先确认安全',"example":"Wait, I must check if it's safe before you jump."},        {"pattern":"It's only mud.","zh":'只是泥而已',"example":"Don't worry, it's only mud. We can clean up."},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾上一集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🥾',"bg":'yellow',"trigger":'Mummy 叫 Peppa 穿靴子',"action":'家长指自己的脚，"Boots！ Get your boots！"'},
            {"emoji":'💦',"bg":'blue',"trigger":'Peppa 找到大泥坑',"action":'张开双臂，"BIG puddle！ REALLY big！"'},
            {"emoji":'😱',"bg":'orange',"trigger":'全家一起跳泥坑',"action":'家长原地跳，"SPLASH！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"So, what does Peppa love doing? YES or NO — does she love muddy puddles?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Yes!" / 点头',"parent":'"YES！ She LOVES muddy puddles！ SPLASH！" 做出踩泥动作'},
                {"child":'"No!"',"parent":'"She doesn\'t love them?！ Then why did she say I LOVE muddy puddles five times？！"'},
                {"child":'不说话',"parent":'家长自己跳："SPLASH！ Muddy puddles！ Does Peppa love them？ YES or NO？"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Did Peppa wear her boots, or did she just jump without boots?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Boots!"',"parent":'"She remembered her boots！ Mummy said: If you jump in muddy puddles, you must wear your boots！"'},
                {"child":'"No boots!"',"parent":'"She jumped without boots first！ Then Mummy said what？ IF you jump..."'},
                {"child":'说中文',"parent":'"BOOTS！ Boots. Like these." 指自己的鞋 <em>（Recast）</em>'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If it was raining today and you could jump in ONE puddle — big or small — which would you choose?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'选大水坑',"parent":'"The BIG one！ Like George！ SPLASH！ Up to your knees！"'},
                {"child":'选小水坑',"parent":'"The small one？ Wise choice — less mud！ But less fun too..."'},
                {"child":'不说话',"parent":'"Me — I\'d choose the BIGGEST one. SPLASH！ Arms out, eyes closed..."'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have YOU ever jumped in a puddle and got your clothes all muddy?"'],
            "rows":[
                {"child":'说曾经跳过',"parent":'"And what happened?！ Were you in trouble？ \'Look at the mess!\'"'},
                {"child":'摇头否认',"parent":'"Never？ You\'re more careful than Daddy Pig！"'},
                {"child":'笑/点头',"parent":'"YES！ Muddy clothes! And did someone say — \'It\'s only mud\'？"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Excuse me！ Are you Peppa？ I heard you\'re the expert on muddy puddles！"'],
            "rows":[
                {"child":'指泥坑/做跳跃动作',"parent":'"Show me！ Do I need anything？ What must I wear？"'},
                {"child":'说 boots',"parent":'"Boots！ And then what？ How do I jump？ Show me！"'},
                {"child":'说中文',"parent":'家长扮 Peppa："I love muddy puddles. Now YOU try！"'},
            ],
        },
        "recast":[
            {"term":'muddy puddles',"explanation":'"What a muddy puddle！ = That puddle is full of MUD！"'},
            {"term":'If you jump... you must...',"explanation":'"If you eat sweets, you must clean your teeth！ Same pattern！"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Put on your boots！" — 做出穿靴子动作',
            '"Jump in the puddle！" — 原地跳，喊 SPLASH！',
            '"It\'s muddy！ Ewww！" — 皱眉，抖手',
            '"Clean up！ Quick！" — 假装快速擦手、擦脚',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Peppa 穿靴子踩第一个泥坑',"L1":'L1: "Jump！"',"L2":'L2: "I love muddy puddles！"',"L3":'L3: "If you jump in muddy puddles, you must wear your boots！"'},
            {"scene":'George 找到大水坑',"L1":'L1: "Big puddle！"',"L2":'L2: "George found a big puddle！"',"L3":'L3: "Look！ There\'s a really big puddle！ Let me check if it\'s safe！"'},
            {"scene":'全家一起跳',"L1":'L1: "SPLASH！"',"L2":'L2: "Everyone loves muddy puddles！"',"L3":'L3: "Mummy, Daddy, Peppa, George — all jumping！ It\'s only mud！"'},
        ],
        },
        "bugs":{
            "rule":'说出任何含 "jump" 的句子得1分；说 "It\'s only mud" 得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'rain → boots → jump → mud → clean'},
            {"level":'L2 (句)',"text":'It rained. They put on boots. They jumped in muddy puddles. They got very muddy. They cleaned up.'},
            {"level":'L3 (完整)',"text":"It was raining, so Peppa and George couldn't go outside. When the rain stopped, Daddy said they could play. Peppa loves muddy puddles! But Mummy said: if you jump in muddy puddles, you must wear your boots. They found a little puddle and a really BIG puddle. George jumped in the big one — SPLASH! At the end, even Mummy and Daddy jumped in. It's only mud!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'短元音 /ʌ/ → 字母 u',
            "examples":['mud', 'muddy', 'mummy', 'jump', 'run'],
            "tongue_tip":'嘴微张，舌头放松，发 /ʌ/ 短促。"Mummy jumps in mud！" 三个 /ʌ/ 连成一串！',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP02 Mr Dinosaur is Lost（恐龙不见了）——" 故意停顿制造悬念',
        "next_a":'EP02 Mr Dinosaur is Lost',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'I love muddy puddles.',"zh":'我爱泥坑',"usage":'每次遇到水坑，小声说这句，等孩子跟着说'},
        {"sentence":'If you jump in muddy puddles, you must wear your boots.',"zh":'跳泥坑必须穿靴子',"usage":'出门前要求穿鞋时用这句'},
        {"sentence":"It's only mud.","zh":'只是泥而已',"usage":'孩子弄脏衣服时说这句，把 Daddy Pig 的豁达传递给孩子'},
        {"sentence":"Look at the mess you're in.","zh":'你看你弄成什么样了',"usage":'洗澡前夸张指着孩子，等孩子笑着回 "It\'s only mud!"'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 02 · Mr Dinosaur is Lost 恐龙不见了
# ═══════════════════════════════════════════════════════════════════════════════
EP02 = _ep(
    num=2, title_en='Mr Dinosaur is Lost', title_zh='恐龙不见了', color='green',
    synopsis='George 的宝贝玩具 Mr Dinosaur 不见了！Peppa 自告奋勇当侦探去找。她猜了浴缸、床上都没有。后来 Daddy 想到——George 喜欢把恐龙扔高高，也许扔进树里去了！果然在树上找到了。',
    vocab=[        {"word":'favourite',"phonetic":'ˈfeɪvərɪt',"pos":'adj.',"zh":'最爱的',"action":'双手握胸，"My favourite！ I love it MOST！"'},        {"word":'lost',"phonetic":'lɒst',"pos":'adj.',"zh":'不见了',"action":'摊手，四处张望，"Where is it？ LOST！"'},        {"word":'detective',"phonetic":'dɪˈtektɪv',"pos":'n.',"zh":'侦探',"action":'假装戴帽子、拿放大镜，"I am the detective！"'},        {"word":'search',"phonetic":'sɜːtʃ',"pos":'v.',"zh":'搜寻',"action":'弯腰到处查看，"Search everywhere！"'},        {"word":'throw',"phonetic":'θrəʊ',"pos":'v.',"zh":'扔、抛',"action":'做出用力抛球动作，"Throw it HIGH！"'},        {"word":'catch',"phonetic":'kætʃ',"pos":'v.',"zh":'接住',"action":'双手张开准备接，"Catch it！ Got it！"'},        {"word":'simple',"phonetic":'ˈsɪmpl',"pos":'adj.',"zh":'简单的',"action":'摆手，"Simple question. Easy."'},        {"word":'worried',"phonetic":'ˈwʌrid',"pos":'adj.',"zh":'担心的',"action":'皱眉，双手托腮，"I\'m worried. Very worried."'},    ],
    patterns=[        {"pattern":"George's favourite toy is Mr Dinosaur.","zh":'George 最爱的玩具是恐龙先生',"example":'My favourite toy is my teddy bear.'},        {"pattern":'A detective is good at finding things.',"zh":'侦探擅长找东西',"example":'Dad is very good at finding lost things.'},        {"pattern":'Have you lost Mr Dinosaur?',"zh":'你把恐龙先生弄丢了？',"example":"Have you lost your keys? They're on the table!"},        {"pattern":"We'll find Mr Dinosaur.","zh":'我们会找到恐龙先生的',"example":"Don't worry, we'll find your toy."},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第1集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🦕',"bg":'green',"trigger":'George 抱着 Mr Dinosaur 到处玩',"action":'家长做出抱玩具动作'},
            {"emoji":'😭',"bg":'blue',"trigger":'George 发现恐龙不见了，大哭',"action":'皱眉摊手，"Where is Mr Dinosaur？ LOST！"'},
            {"emoji":'🔍',"bg":'yellow',"trigger":'Peppa 当侦探开始调查',"action":'假装戴帽子，"I am the detective！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Did Peppa find Mr Dinosaur? Yes or no?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Yes!"',"parent":'"YES！ She found him！ WHERE？ In the TREE！" 指向天花板'},
                {"child":'"No"',"parent":'"Wait... yes she did！ Up in the tree！ Did you forget？ It went WHOOSH！"'},
                {"child":'不说话',"parent":'家长做抛恐龙动作："Whee！ UP！ And then... stuck in the tree！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Why was Mr Dinosaur in the tree?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"George threw it"',"parent":'"George threw Mr Dinosaur UP UP UP — and it got stuck in the tree！ WHOOPS！"'},
                {"child":'说其他',"parent":'"George loves throwing Mr Dinosaur into the air... but this time..." 手做飞走动作'},
                {"child":'不说话',"parent":'做出抛球动作，越比越高，"Too HIGH！ Into the tree！"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If YOU were the detective, what would be the FIRST place you\'d look for a lost dinosaur?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说房间/浴室',"parent":'"Smart detective！ That\'s where Peppa looked first！"'},
                {"child":'说树上/外面',"parent":'"Straight to the tree！ You\'re a BETTER detective than Peppa！"'},
                {"child":'不说话',"parent":'"Me — I\'d look... under the sofa. Then the bath. Then... UP！" 仰头'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever lost something you really, really loved?"'],
            "rows":[
                {"child":'说过去丢过玩具',"parent":'"And how did you FEEL？ Like George? Whaaaa!"'},
                {"child":'摇头',"parent":'"Never lost anything？ Very careful！ But if you DID lose something, who would help you？"'},
                {"child":'说某个玩具',"parent":'"And when you found it — did you feel like this?" 做出 George 开心抱恐龙的动作'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Hello！ Are you Detective Peppa？ I\'ve lost something very important！"'],
            "rows":[
                {"child":'假装调查/问问题',"parent":'"Ask me a simple question！ Where did I last have it？"'},
                {"child":'说 "Where is it?"',"parent":'"Maybe check the bath？ The bed？ Or... look UP！"'},
                {"child":'说中文',"parent":'家长扮 Peppa："I am the detective！ Where did you last put it？"'},
            ],
        },
        "recast":[
            {"term":'favourite toy',"explanation":'"My favourite！ = I love it most!"'},
            {"term":'A detective is good at finding things',"explanation":'"Good at = 擅长。I\'m good at swimming."'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Look for it！ Search！" — 弯腰到处东张西望',
            '"Throw the dinosaur！ Catch！" — 做抛接动作',
            '"I\'m the detective！" — 假装拿放大镜',
            '"Found it！ UP there！" — 猛地抬头仰望',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'George 发现恐龙不见了',"L1":'L1: "No！ Lost！"',"L2":'L2: "Mr Dinosaur is lost！"',"L3":'L3: "George has lost Mr Dinosaur! He is very very sad!"'},
            {"scene":'Peppa 当侦探',"L1":'L1: "Detective！"',"L2":'L2: "I am the detective！"',"L3":'L3: "I\'m a very good detective! I will find Mr Dinosaur!"'},
            {"scene":'在树上找到恐龙',"L1":'L1: "There！ Found！"',"L2":'L2: "Mr Dinosaur is in the tree！"',"L3":'L3: "George threw Mr Dinosaur too high — it went into the tree!"'},
        ],
        },
        "bugs":{
            "rule":'每说一次 "detective" 得1分；说 "Found it!" 得1分；说出完整句 "Have you lost...?" 得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'dinosaur → lost → detective → search → tree → found'},
            {"level":'L2 (句)',"text":'Mr Dinosaur was lost. Peppa became the detective. She searched everywhere. She found him in the tree.'},
            {"level":'L3 (完整)',"text":"George's favourite toy is Mr Dinosaur. He loves throwing it up and catching it. One day, Mr Dinosaur disappeared! Peppa became the detective. She looked in the bath — not there. She looked in the bed — not there. Then Daddy had an idea: George always throws Mr Dinosaur up high... it went too high this time! They looked up in the tree. There he was! George was so happy!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ou/ow → /aʊ/ 双元音',
            "examples":['found', 'out', 'down', 'now', 'owl'],
            "tongue_tip":'嘴从圆到扁快速过渡，/aʊ/ 像 "啊-乌" 连起来。"Found him! Down from the tree! Wow!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP03 Best Friend（最好的朋友）——" 故意停顿制造悬念',
        "next_a":'EP03 Best Friend',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"George's favourite toy is Mr Dinosaur.","zh":'最爱的玩具',"usage":'把孩子名字和最爱的玩具代入'},
        {"sentence":'I am the detective.',"zh":'我是侦探',"usage":'帮孩子找东西时宣布自己是侦探'},
        {"sentence":'A detective is good at finding things.',"zh":'侦探擅长找东西',"usage":'夸孩子找到东西时用'},
        {"sentence":"Maybe it isn't a good idea to play with dinosaurs near trees.","zh":'也许在树边玩恐龙不是好主意',"usage":'每次孩子把东西扔到够不到处时引用'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 03 · Best Friend 最好的朋友
# ═══════════════════════════════════════════════════════════════════════════════
EP03 = _ep(
    num=3, title_en='Best Friend', title_zh='最好的朋友', color='pink',
    synopsis='Peppa 的好朋友 Suzy Sheep 来玩。她们不让 George 参加游戏。George 很孤独。最后她们邀请 George 扮演病人一起玩医生护士游戏，George 终于开心了。',
    vocab=[        {"word":'best friend',"phonetic":'best frend',"pos":'n.',"zh":'最好的朋友',"action":'双手握在一起，"Best friends forever！"'},        {"word":'lonely',"phonetic":'ˈləʊnli',"pos":'adj.',"zh":'孤独的',"action":'一个人缩角落，"Lonely... all alone..."'},        {"word":'fairy princess',"phonetic":'ˈfeəri ˈprɪnsəs',"pos":'n.',"zh":'仙女公主',"action":'想象拿魔法棒，轻盈转圈'},        {"word":'magic wand',"phonetic":'ˈmædʒɪk wɒnd',"pos":'n.',"zh":'魔法棒',"action":'挥动想象的棒子，"Bibbidi-boo！"'},        {"word":'nurse',"phonetic":'nɜːs',"pos":'n.',"zh":'护士',"action":'假装听诊器，"The nurse checks patients"'},        {"word":'doctor',"phonetic":'ˈdɒktə',"pos":'n.',"zh":'医生',"action":'假装开处方，"The doctor is busy"'},        {"word":'invite',"phonetic":'ɪnˈvaɪt',"pos":'v.',"zh":'邀请',"action":'张开双臂，"Come！ You\'re invited！"'},        {"word":'share',"phonetic":'ʃeə',"pos":'v.',"zh":'分享',"action":'手拿东西递给别人，"Share!"'},    ],
    patterns=[        {"pattern":'This game is just for big girls.',"zh":'这个游戏只给大女孩玩',"example":'This room is just for Mummy and Daddy.'},        {"pattern":"I'm going to turn you into a frog!","zh":'我要把你变成一只青蛙！',"example":"I'm going to turn this pumpkin into a carriage!"},        {"pattern":'George feels a bit lonely.',"zh":'George 有点孤独',"example":'When no one plays with me, I feel a bit lonely.'},        {"pattern":"Why don't you go and play in your bedroom?","zh":'为什么不去房间里玩呢？',"example":"Why don't you and Suzy play in the garden?"},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第2集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'👗',"bg":'pink',"trigger":'Peppa 扮仙女公主',"action":'家长轻盈转圈，"I\'m a fairy princess！"'},
            {"emoji":'😢',"bg":'blue',"trigger":'George 被拒绝，感到孤独',"action":'缩成一团，"Lonely..."'},
            {"emoji":'🏥',"bg":'green',"trigger":'Peppa 邀请 George 扮病人',"action":'假装听诊器，"Open wide！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Did Peppa let George play at first? Yes or no?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"No!"',"parent":'"Right！ She said \'This game is just for big girls！\' Poor George. How did he feel?"'},
                {"child":'"Yes!"',"parent":'"Hmm... at FIRST she said NO. She said \'Go away, George！\'"'},
                {"child":'不说话',"parent":'做出推走的手势，"Go away, George！ Only BIG GIRLS！ Was that nice？"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Who did George play in the doctor game — doctor, nurse, or patient?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Patient!"',"parent":'"YES！ George was the sick person! And Peppa was the DOCTOR. He was just happy to play!"'},
                {"child":'"Doctor!"',"parent":'"Peppa was the doctor and Suzy was the nurse... so George was the...?"'},
                {"child":'说中文',"parent":'"Patient = 病人！ George was the patient. <em>（Recast）</em>"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If your best friend came over, what game would you want to play most?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说游戏名称',"parent":'"Would there be room for someone else？ Like George？"'},
                {"child":'说医生/护士',"parent":'"Doctor and nurse！ Like Peppa and Suzy！ Who would be the sick person？"'},
                {"child":'不说话',"parent":'"Me — I\'d play a guessing game where everyone can join!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever felt lonely when everyone was playing without you?"'],
            "rows":[
                {"child":'点头/说感受',"parent":'"Like George！ Standing outside, watching..."'},
                {"child":'摇头',"parent":'"Lucky you！ But George felt very lonely..."'},
                {"child":'说过经历',"parent":'"And how did it feel when someone finally let you in？"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Oh no！ I\'ve got a tummy ache. Is there a doctor here？"'],
            "rows":[
                {"child":'假装听诊器/检查',"parent":'"Doctor！ What\'s wrong with me？"'},
                {"child":'说 "Open wide"',"parent":'"I open wide... AHHH..."'},
                {"child":'说中文',"parent":'家长扮病人："I\'m the patient. I\'m not very well. Who\'s the doctor?"'},
            ],
        },
        "recast":[
            {"term":'best friend',"explanation":'"Best friend = 最好的朋友. Best = better than all others!"'},
            {"term":'a bit lonely',"explanation":'"A BIT lonely = 有一点点孤独. Not super lonely, just a little bit."'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Wave your magic wand！" — 挥动想象的魔法棒',
            '"You\'re a frog！ Jump！" — 蹲低跳',
            '"The patient needs help！" — 假装胸口不舒服',
            '"Best friends hug！" — 张开手臂做拥抱状',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Peppa 不让 George 参加',"L1":'L1: "No, George！"',"L2":'L2: "Go away, George！"',"L3":'L3: "This game is just for big girls. Go play with your own toys!"'},
            {"scene":'George 一个人站在门口',"L1":'L1: "Lonely..."',"L2":'L2: "George feels lonely."',"L3":'L3: "George doesn\'t like playing on his own. He wants to play with Peppa."'},
            {"scene":'Peppa 邀请 George 当病人',"L1":'L1: "George！ Come！"',"L2":'L2: "George can be the patient！"',"L3":'L3: "George! Do you want to play? You can be the sick person!"'},
        ],
        },
        "bugs":{
            "rule":'说出 "best friend" 得1分；说出 "lonely" 得1分；用英文邀请对方得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'best friend → bedroom → fairy → lonely → doctor → nurse → patient'},
            {"level":'L2 (句)',"text":'Suzy came to play. Peppa said no to George. George felt lonely. Later they let George be the patient.'},
            {"level":'L3 (完整)',"text":"Peppa's best friend Suzy came over. They wanted to play in the bedroom — just for big girls! Poor George was left out. He felt very lonely. Then Peppa had an idea: they'd play doctors and nurses! Peppa was the doctor, Suzy was the nurse, and George could be the patient! George was so happy just to play together."},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ea → /iː/ 长音',
            "examples":['please', 'each', 'dream', 'team', 'treat'],
            "tongue_tip":'嘴角向两侧拉，发 /iː/，像在笑。"Please！ Team！ Dream！"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP04 Polly Parrot（鹦鹉波利）——" 故意停顿制造悬念',
        "next_a":'EP04 Polly Parrot',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'This game is just for big girls.',"zh":'这个游戏只给大女孩',"usage":'孩子拒绝别人时轻声重复，再问 George 的感受'},
        {"sentence":'George feels a bit lonely.',"zh":'George 有点孤独',"usage":'孩子被排除时共情'},
        {"sentence":"I'm going to wave my magic wand and turn you into a frog!","zh":'挥魔法棒把你变成青蛙',"usage":'睡前游戏的魔法仪式'},
        {"sentence":"Why don't you go and play in your bedroom?","zh":'为什么不去房间玩呢',"usage":'温柔转移注意力'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 04 · Polly Parrot 鹦鹉波利
# ═══════════════════════════════════════════════════════════════════════════════
EP04 = _ep(
    num=4, title_en='Polly Parrot', title_zh='鹦鹉波利', color='orange',
    synopsis='爷爷奶奶有一只新宠物——鹦鹉 Polly！Polly 会模仿所有人说话。Peppa 和 George 很兴奋，一直想让 Polly 学说话。最后 George 说了 Grrr，Polly 也学会了。',
    vocab=[        {"word":'parrot',"phonetic":'ˈpærət',"pos":'n.',"zh":'鹦鹉',"action":'双手做成翅膀，歪头，"Polly want a cracker！"'},        {"word":'repeat',"phonetic":'rɪˈpiːt',"pos":'v.',"zh":'重复',"action":'拍手一次，"Repeat — say it again！"'},        {"word":'clever',"phonetic":'ˈklevə',"pos":'adj.',"zh":'聪明的',"action":'点头，竖大拇指，"Very clever！"'},        {"word":'copy',"phonetic":'ˈkɒpi',"pos":'v.',"zh":'模仿',"action":'做镜像动作跟着对方，"Copy exactly what I do！"'},        {"word":'surprise',"phonetic":'səˈpraɪz',"pos":'n.',"zh":'惊喜',"action":'捂嘴，眼睛睁大，"Surprise！！！"'},        {"word":'pet',"phonetic":'pet',"pos":'n.',"zh":'宠物',"action":'假装摸小动物，"Nice pet！"'},        {"word":'pretty',"phonetic":'ˈprɪti',"pos":'adj.',"zh":'漂亮的',"action":'做出欣赏的样子，"Pretty！ Beautiful！"'},        {"word":'whisper',"phonetic":'ˈwɪspə',"pos":'v.',"zh":'低声说',"action":'凑近耳边，用耳语声说话'},    ],
    patterns=[        {"pattern":'What a clever parrot!',"zh":'真是只聪明的鹦鹉！',"example":'What a clever child! What a surprise!'},        {"pattern":"That's what parrots do.","zh":'这就是鹦鹉的特点',"example":"That's what dogs do — they bark!"},        {"pattern":'Can you say hello, Polly?',"zh":'你能说你好吗，波利？',"example":'Can you say thank you? Can you say please?'},        {"pattern":'Polly can say anything you say.',"zh":'波利能说任何你说的话',"example":'The parrot copies everything!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第3集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🦜',"bg":'orange',"trigger":'Granny 揭晓新宠物鹦鹉',"action":'捂嘴，"A PARROT！ Wow！"'},
            {"emoji":'🗣️',"bg":'yellow',"trigger":'Polly 模仿人说话',"action":'歪头，用奇怪的声音重复刚说的话'},
            {"emoji":'🦕',"bg":'green',"trigger":'George 说 Grrr，Polly 学了',"action":'做恐龙吼声'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What does Polly do? Does she copy what people say, or say different things?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Copy!"',"parent":'"RIGHT！ Let me be Polly — you say something!" 完全模仿孩子'},
                {"child":'"Different!"',"parent":'"When Granny said \'I am a clever parrot\', Polly said..." 等孩子想'},
                {"child":'不说话',"parent":'说一句话，指孩子："Now you be Polly — copy me！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What was the last word Polly learned? From Peppa, or from George?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"George!"',"parent":'"YES！ George said GRRR and Polly learned GRRR！ A dinosaur-parrot！"'},
                {"child":'说 Peppa',"parent":'"Peppa tried many things! But the last word... George made a dinosaur sound..."'},
                {"child":'不说话',"parent":'做出 George 的恐龙动作，"Grrr！ And Polly said..."'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If YOU had a parrot, what one word would you teach it first?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说词语',"parent":'"Polly would say [word] all day long！ Imagine！"'},
                {"child":'说自己名字',"parent":'"Your name！ Imagine the parrot calling you all day！"'},
                {"child":'不说话',"parent":'"Me — I\'d teach it to say \'dinner\'s ready！\'"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever tried to copy someone exactly — like a parrot?"'],
            "rows":[
                {"child":'说过/笑了',"parent":'"Like a parrot！ Was it funny or annoying？"'},
                {"child":'摇头',"parent":'"Never？ Let\'s try！ Say something..." 完全模仿孩子'},
                {"child":'做出模仿动作',"parent":'"Copy！ Just like Polly！"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Hello Polly！ Pretty Polly！ Can you say... hello？"'],
            "rows":[
                {"child":'重复 "hello"',"parent":'"What a clever parrot！ Can you say: I am a clever parrot？"'},
                {"child":'做鹦鹉动作',"parent":'"Polly！ Can you say... Grrr？"'},
                {"child":'说中文',"parent":'家长扮 Polly："Pretty Polly！ Now YOU be Polly！"'},
            ],
        },
        "recast":[
            {"term":"That's what parrots do","explanation":'"That\'s what + noun + verb = 这就是...的特点"'},
            {"term":'What a clever parrot!',"explanation":'"What a + adj + noun = 感叹句！What a beautiful day!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Pretty Polly！" — 歪头，做鹦鹉样子',
            '"Copy me！" — 做一个动作，让孩子模仿',
            '"What a surprise！" — 捂嘴，眼睛睁大',
            '"Say it again！ Repeat！" — 指孩子，拍手节奏',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Polly 模仿说话',"L1":'L1: "Clever！"',"L2":'L2: "What a clever parrot！"',"L3":'L3: "I am a clever parrot! That\'s what parrots do!"'},
            {"scene":'George 说 Grrr',"L1":'L1: "Grrr！"',"L2":'L2: "Polly says Grrr！"',"L3":'L3: "George said Grrr — and now Polly can say Grrr too!"'},
            {"scene":'Peppa 教 Polly',"L1":'L1: "Say it, Polly！"',"L2":'L2: "Can you say hello, Polly？"',"L3":'L3: "Polly! I\'m going to teach you a new word. Say: hello！"'},
        ],
        },
        "bugs":{
            "rule":'模仿对方说的话1分；说 "What a clever parrot" 得1分；说出 "That\'s what parrots do" 得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'parrot → copy → repeat → clever → surprise → Grrr'},
            {"level":'L2 (句)',"text":'Granny had a new pet parrot. The parrot copies everything. Polly learned to say Grrr.'},
            {"level":'L3 (完整)',"text":'Peppa and George visited Granny and Grandpa. They had a surprise — a new pet parrot called Polly! Polly can copy anything anyone says. George said his favourite word: Grrr! And Polly said: Grrr! George taught the parrot a dinosaur word. What a clever parrot!'},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母 a 在辅音前 → /æ/ 短促音',
            "examples":['parrot', 'cat', 'catch', 'can', 'happy'],
            "tongue_tip":'嘴张开，舌头平放，发 /æ/。"Can a cat catch a parrot？"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP05 Hide and Seek（捉迷藏）——" 故意停顿制造悬念',
        "next_a":'EP05 Hide and Seek',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'What a clever parrot!',"zh":'真聪明的鹦鹉',"usage":'夸孩子说出英文时用'},
        {"sentence":"That's what parrots do.","zh":'这就是鹦鹉的特点',"usage":'孩子模仿大人时笑着说'},
        {"sentence":'Can you say... Polly?',"zh":'波利，你能说...吗',"usage":'练新词时用鹦鹉游戏'},
        {"sentence":'Pretty Polly.',"zh":'漂亮的波利',"usage":'夸孩子的搞怪方式'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 05 · Hide and Seek 捉迷藏
# ═══════════════════════════════════════════════════════════════════════════════
EP05 = _ep(
    num=5, title_en='Hide and Seek', title_zh='捉迷藏', color='purple',
    synopsis='Peppa 和 George 玩捉迷藏。George 藏得太明显被一眼找到。轮到 Peppa 藏，她藏得超好，连 Daddy Mummy 都找不到！最后大家总算找到了 Peppa。',
    vocab=[        {"word":'hide',"phonetic":'haɪd',"pos":'v.',"zh":'躲藏',"action":'弓腰蹲下，把脸遮住，"Hide！"'},        {"word":'seek',"phonetic":'siːk',"pos":'v.',"zh":'寻找',"action":'双手遮眼，移开，四处张望，"Seek！"'},        {"word":'count',"phonetic":'kaʊnt',"pos":'v.',"zh":'数数',"action":'竖起手指，"One... two... three..." 闭眼'},        {"word":'ready',"phonetic":'ˈredi',"pos":'adj.',"zh":'准备好了',"action":'双脚站稳，"Ready！ Set！"'},        {"word":'found',"phonetic":'faʊnd',"pos":'v.',"zh":'找到了',"action":'手指向前，"Found you！"'},        {"word":'together',"phonetic":'təˈɡeðə',"pos":'adv.',"zh":'一起',"action":'双手合拢，"Together！"'},        {"word":'behind',"phonetic":'bɪˈhaɪnd',"pos":'prep.',"zh":'在...后面',"action":'躲到某物后，"Behind the tree！"'},        {"word":'easily',"phonetic":'ˈiːzɪli',"pos":'adv.',"zh":'容易地',"action":'摆手，"Too easy！ Found you immediately！"'},    ],
    patterns=[        {"pattern":'Ready or not, here I come!',"zh":'准备好没有，我来了！',"example":"Ready or not, it's time for dinner!"},        {"pattern":"You're very good at hiding.","zh":'你藏得很好',"example":"You're very good at counting."},        {"pattern":'Found you!',"zh":'找到你了！',"example":'Found you! You were hiding behind the curtain!'},        {"pattern":'I could see you too easily.',"zh":'我一眼就看到你了',"example":'That hiding place is too easy!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第4集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🙈',"bg":'purple',"trigger":'George 躲在明显的地方',"action":'家长数数，眼睛故意往 George 方向看'},
            {"emoji":'🔍',"bg":'yellow',"trigger":'全家人一起找 Peppa',"action":'到处张望，"Where is Peppa？"'},
            {"emoji":'🎉',"bg":'green',"trigger":'终于找到 Peppa',"action":'做出惊喜找到的表情'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Was George good at hiding, or could Peppa find him too easily?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Too easily!"',"parent":'"YES！ Peppa said \'I could see you too easily\'！ George was right there！"'},
                {"child":'"Good!"',"parent":'"Actually Peppa found him VERY quickly. He wasn\'t well hidden!"'},
                {"child":'不说话',"parent":'做出 George 躲到不行的样子，等孩子笑'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Who was BEST at hiding — Peppa, George, or Mummy and Daddy?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Peppa!"',"parent":'"YES！ Peppa hid SO well that even Mummy and Daddy couldn\'t find her！"'},
                {"child":'说 George',"parent":'"George was found SO quickly！ Who was BETTER？"'},
                {"child":'不说话',"parent":'"Peppa was so good that everyone was looking everywhere！"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"In our house — what is the BEST hiding place?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说具体地方',"parent":'"Would I find you easily or not？ Let\'s test it！"'},
                {"child":'说家长找不到的地方',"parent":'"You think I can\'t find you？ Go hide — I\'ll count to ten！"'},
                {"child":'不说话',"parent":'"Me — I\'d hide behind the big coat. Nobody looks there！"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you played hide and seek? Who was best at hiding?"'],
            "rows":[
                {"child":'说名字',"parent":'"What was their secret hiding place？"'},
                {"child":'说自己最好',"parent":'"YOU are the best！ Like Peppa！"'},
                {"child":'不说话',"parent":'"Ready or not..." 假装开始数数'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Let\'s play hide and seek！ I\'ll count — you hide！ Ready？"'],
            "rows":[
                {"child":'去藏/笑',"parent":'家长数："One... two... three..." 假装找不到'},
                {"child":'说 "Ready!"',"parent":'"Ready？ Ready or not, here I come！"'},
                {"child":'说中文',"parent":'直接开始游戏'},
            ],
        },
        "recast":[
            {"term":'Ready or not, here I come',"explanation":'"Ready or not = 准备好没有。 Here I come = 我来了！"'},
            {"term":'I could see you too easily',"explanation":'"Too + adv = 太...了。 Too easily = 太容易了"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Cover your eyes！ Count！" — 双手遮眼，数数',
            '"Hide！ Quick！" — 做蹲下躲藏动作',
            '"Ready or not, here I come！" — 移开双手，向前走',
            '"Found you！" — 手指向某处，惊喜状',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'George 躲在明显地方',"L1":'L1: "Found！"',"L2":'L2: "Found you, George！"',"L3":'L3: "George, I could see you too easily! You\'re not good at hiding!"'},
            {"scene":'大家找不到 Peppa',"L1":'L1: "Where？ Peppa？"',"L2":'L2: "Where is Peppa hiding？"',"L3":'L3: "Peppa！ We\'ve looked everywhere and can\'t find you！"'},
            {"scene":'数数开始游戏',"L1":'L1: "One, two, three..."',"L2":'L2: "Ready or not, here I come!"',"L3":'L3: "Close your eyes! One... two... three... ready or not, here I come！"'},
        ],
        },
        "bugs":{
            "rule":'说出 "Ready or not" 得2分；说出 "Found you" 得1分；说出藏身处英文词得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'hide → seek → count → ready → found → behind'},
            {"level":'L2 (句)',"text":'Peppa and George played hide and seek. Peppa found George easily. Peppa hid so well nobody could find her.'},
            {"level":'L3 (完整)',"text":"Peppa and George played hide and seek. George hid but Peppa found him too easily! Then it was Peppa's turn. She hid SO well that George couldn't find her. Mummy helped count: one, two, three... ready or not, here I come! But still couldn't find Peppa! Finally they found her. She was the best at hiding!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ee/ea → /iː/ 长音',
            "examples":['seek', 'see', 'easily', 'each', 'tree'],
            "tongue_tip":'嘴角向两侧拉，"ee" 就像在微笑。"Seek！ Can you see me？ Easily！"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP06 The Playgroup（幼儿园）——" 故意停顿制造悬念',
        "next_a":'EP06 The Playgroup',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Ready or not, here I come!',"zh":'准备好没有，我来了！',"usage":'每次去找孩子时用'},
        {"sentence":'I could see you too easily!',"zh":'我一眼就看到你了',"usage":'找到孩子后，激励他藏更好'},
        {"sentence":'Found you!',"zh":'找到你了！',"usage":'找到任何东西都可用'},
        {"sentence":'Where could Peppa be?',"zh":'Peppa 可能在哪里呢？',"usage":'找人找物的经典句'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 06 · The Playgroup 幼儿园
# ═══════════════════════════════════════════════════════════════════════════════
EP06 = _ep(
    num=6, title_en='The Playgroup', title_zh='幼儿园', color='yellow',
    synopsis='这是 George 第一天去 Peppa 的幼儿园。Peppa 不太想带他去。但 Madame Gazelle 热情欢迎 George，小伙伴们也很喜欢 Mr Dinosaur。George 爱上了幼儿园！',
    vocab=[        {"word":'playgroup',"phonetic":'ˈpleɪɡruːp',"pos":'n.',"zh":'幼儿园',"action":'双手展示，"Everyone comes to playgroup!"'},        {"word":'teacher',"phonetic":'ˈtiːtʃə',"pos":'n.',"zh":'老师',"action":'假装站讲台，"I am the teacher！"'},        {"word":'paint',"phonetic":'peɪnt',"pos":'v./n.',"zh":'画画/颜料',"action":'用手指假装蘸颜料，空中画圈'},        {"word":'pencil',"phonetic":'ˈpensl',"pos":'n.',"zh":'铅笔',"action":'拿起想象的铅笔，假装写字'},        {"word":'lesson',"phonetic":'ˈlesn',"pos":'n.',"zh":'课程',"action":'坐直，"Time for our lesson！"'},        {"word":'together',"phonetic":'təˈɡeðə',"pos":'adv.',"zh":'一起',"action":'双手合拢，"Let\'s do it together！"'},        {"word":'favourite',"phonetic":'ˈfeɪvərɪt',"pos":'adj.',"zh":'最喜欢的',"action":'点头，"This is my favourite！"'},        {"word":'company',"phonetic":'ˈkʌmpəni',"pos":'n.',"zh":'陪伴',"action":'指身边的人，"Keep me company！"'},    ],
    patterns=[        {"pattern":'Are you looking forward to the playgroup?',"zh":'你期待幼儿园吗？',"example":'Are you looking forward to your birthday?'},        {"pattern":"He'll be fine.","zh":'他会没事的',"example":"Don't worry, she'll be fine."},        {"pattern":'This is my favourite lesson.',"zh":'这是我最喜欢的课',"example":'This is my favourite song.'},        {"pattern":'Madame Gazelle looks after the children.',"zh":'羚羊老师照顾小朋友',"example":'Our teacher looks after everyone.'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第5集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🏫',"bg":'yellow',"trigger":'幼儿园到了，Madame Gazelle 迎接',"action":'坐好，假装听老师说话'},
            {"emoji":'🎨',"bg":'pink',"trigger":'大家在幼儿园画画',"action":'用手指空中乱涂'},
            {"emoji":'🦕',"bg":'green',"trigger":'小伙伴们喜欢 Mr Dinosaur',"action":'做恐龙吼声，"Grrr！ Wow！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Did George like his first day at playgroup?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Yes!"',"parent":'"YES！ He loved it！ All the children wanted to see his dinosaur！"'},
                {"child":'"No!"',"parent":'"Actually at the end George was very happy! He made friends!"'},
                {"child":'不说话',"parent":'做出 George 开心的表情，"Was George happy？"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Who is the teacher at the playgroup?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说 Madame Gazelle',"parent":'"Madame Gazelle！ She\'s a gazelle — graceful animals with long necks!"'},
                {"child":'说老师',"parent":'"Madame Gazelle！ She welcomed George on his first day!"'},
                {"child":'不说话',"parent":'"Ma-dame Ga-ZELLE！ It sounds very fancy! Can you say it？"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you started at a new school, what would you hope to find there?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说朋友/游戏',"parent":'"New friends！ Like George found friends who loved his dinosaur！"'},
                {"child":'说玩具/活动',"parent":'"Painting！ Building！ Like the playgroup！"'},
                {"child":'不说话',"parent":'"I\'d hope to find someone friendly who says \'hello!\'"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Can you remember your first day at school? Were you nervous?"'],
            "rows":[
                {"child":'说紧张/害怕',"parent":'"Like George！ A little scared but then it was fine. He\'ll be fine — and he WAS!"'},
                {"child":'说开心',"parent":'"Brave！ George was worried too — but then he loved it!"'},
                {"child":'不说话',"parent":'"George was worried. But then all the children loved his dinosaur!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Good morning！ Welcome to the playgroup！ Are you a new student？"'],
            "rows":[
                {"child":'回答/说 yes',"parent":'"Wonderful！ What\'s your name？ Do you have a favourite toy？"'},
                {"child":'说自己名字',"parent":'"Welcome, [name]！ We have painting today！"'},
                {"child":'说中文',"parent":'家长扮 Madame Gazelle："Hello！ Welcome! We have painting today！"'},
            ],
        },
        "recast":[
            {"term":"He'll be fine","explanation":'"He\'ll = He will. Fine = 一切好。"'},
            {"term":'looking forward to',"explanation":'"Look forward to = 期待。 Are you looking forward to your birthday？"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Sit down！ Class is starting！" — 坐直',
            '"Paint a picture！" — 手指蘸颜料',
            '"Good morning, Madame Gazelle！" — 站起来，鞠躬',
            '"He\'ll be fine！" — 竖大拇指',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Daddy 安慰说 George 会没事',"L1":'L1: "Fine！"',"L2":'L2: "He\'ll be fine！"',"L3":'L3: "Don\'t worry, Peppa. George will be fine at the playgroup!"'},
            {"scene":'Madame Gazelle 欢迎 George',"L1":'L1: "Hello, George！"',"L2":'L2: "Welcome to the playgroup！"',"L3":'L3: "Hello George! We\'re very happy to have you here today."'},
            {"scene":'小朋友们围着恐龙',"L1":'L1: "Wow！ Dinosaur！"',"L2":'L2: "Is that a real dinosaur？"',"L3":'L3: "George has a dinosaur toy! It says Grrr！ So cool！"'},
        ],
        },
        "bugs":{
            "rule":'说出 "playgroup" 得1分；说出 "Madame Gazelle" 得1分；用英文欢迎别人得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'playgroup → first day → Madame Gazelle → friends → dinosaur → happy'},
            {"level":'L2 (句)',"text":"George went to playgroup for the first time. Peppa wasn't sure. But George loved it."},
            {"level":'L3 (完整)',"text":"It was George's first day at Peppa's playgroup. Peppa wasn't sure she wanted George there. But Daddy said: he'll be fine. Madame Gazelle welcomed George. All the children loved his Mr Dinosaur toy! George made new friends on his very first day. He loved the playgroup!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母 g 在 a/o/u 前发 /ɡ/ 硬音',
            "examples":['group', 'garden', 'game', 'go', 'got'],
            "tongue_tip":'舌后根抵上颚，快速弹出 /ɡ/。"Go to the garden！ George plays games！"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP07 Mummy Pig at Work（猪妈妈工作）——" 故意停顿制造悬念',
        "next_a":'EP07 Mummy Pig at Work',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"He'll be fine.","zh":'他会没事的',"usage":'孩子面对新环境时的安慰语'},
        {"sentence":'Are you looking forward to playgroup?',"zh":'你期待幼儿园吗？',"usage":'每天出门前的热身问句'},
        {"sentence":'This is my favourite lesson.',"zh":'这是我最喜欢的课',"usage":'让孩子用英文说最喜欢的事'},
        {"sentence":'George will be fine.',"zh":'George 会没事的',"usage":'入园焦虑时的积极暗示'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 07 · Mummy Pig at Work 猪妈妈工作
# ═══════════════════════════════════════════════════════════════════════════════
EP07 = _ep(
    num=7, title_en='Mummy Pig at Work', title_zh='猪妈妈工作', color='blue',
    synopsis='Mummy Pig 在电脑上工作，要求 Peppa 和 George 不要打扰。Peppa 一直缠着想玩游戏，还假装教 George 顺便自己碰了电脑弄乱文件。Daddy 来修越弄越糟，最后 Mummy 自己修好了。',
    vocab=[        {"word":'computer',"phonetic":'kəmˈpjuːtə',"pos":'n.',"zh":'电脑',"action":'两手放想象的键盘，"Working on the computer！"'},        {"word":'important',"phonetic":'ɪmˈpɔːtnt',"pos":'adj.',"zh":'重要的',"action":'双手交叉，严肃，"Very important！"'},        {"word":'disturb',"phonetic":'dɪˈstɜːb',"pos":'v.',"zh":'打扰',"action":'做打断动作，然后摆手，"Don\'t disturb！"'},        {"word":'mend',"phonetic":'mend',"pos":'v.',"zh":'修理',"action":'假装动手修，"Fix it！ Mend it！"'},        {"word":'button',"phonetic":'ˈbʌtn',"pos":'n.',"zh":'按键',"action":'用食指假装按按钮'},        {"word":'press',"phonetic":'pres',"pos":'v.',"zh":'按',"action":'手指向下压，"Don\'t press that button！"'},        {"word":'wrong',"phonetic":'rɒŋ',"pos":'adj.',"zh":'出错了',"action":'摇头，"Something went wrong！"'},        {"word":'expert',"phonetic":'ˈekspɜːt',"pos":'n.',"zh":'专家',"action":'指自己，"I\'m an expert！"'},    ],
    patterns=[        {"pattern":'Mummy has a lot of important work to do.',"zh":'妈妈有很多重要的工作',"example":'Daddy has a lot of important work today.'},        {"pattern":"You mustn't touch the computer.","zh":'你不能碰电脑',"example":"You mustn't run in the corridor."},        {"pattern":'Can you mend the computer, Daddy?',"zh":'爸爸，你能修电脑吗？',"example":'Can you fix my toy?'},        {"pattern":'I was just showing George what not to do.',"zh":'我只是在给 George 示范',"example":'I was showing him how NOT to do it!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第6集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'💻',"bg":'blue',"trigger":'Mummy 专心工作',"action":'假装认真打字，"Busy！ Don\'t disturb！"'},
            {"emoji":'⌨️',"bg":'red',"trigger":'Peppa 偷偷碰了电脑',"action":'做 "oops" 表情，捂嘴'},
            {"emoji":'🔧',"bg":'yellow',"trigger":'Daddy 来修电脑',"action":'假装修，越弄越糟，耸肩'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Could Peppa and George touch Mummy\'s computer?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"No!"',"parent":'"RIGHT！ Mummy said: \'You mustn\'t touch the computer!\' Did they listen？"'},
                {"child":'"Yes!"',"parent":'"Mummy said MUSTN\'T！ They weren\'t supposed to！ But Peppa sneaked a touch..."'},
                {"child":'不说话',"parent":'伸出手指做碰电脑状，"Can I touch it？" 等孩子喊 "No！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Who fixed the computer — Daddy or Mummy herself?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Mummy!"',"parent":'"YES！ Mummy fixed it! Daddy tried but made it worse! Then Mummy pressed one button — fixed!"'},
                {"child":'说 Daddy',"parent":'"Daddy TRIED! But made it worse! It was MUMMY who fixed it!"'},
                {"child":'不说话',"parent":'假装按一个按钮，"Click！ Fixed！ Who did that？"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"What would YOU do if you accidentally broke something important?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说告诉大人',"parent":'"Tell Mummy or Daddy！ That\'s what happened! Mummy called Daddy!"'},
                {"child":'说自己修',"parent":'"Fix it yourself！ Like Mummy Pig!"'},
                {"child":'不说话',"parent":'做出 "oops" 表情，"I\'d say: Daddy Pig！ Can you mend it？!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Has Mummy or Daddy ever had to do important work at home?"'],
            "rows":[
                {"child":'说曾经帮忙',"parent":'"Like Peppa！ Wanting to help but maybe a little in the way？"'},
                {"child":'摇头',"parent":'"You waited patiently？ Better than Peppa! She kept asking for Happy Mrs Chicken!"'},
                {"child":'笑了',"parent":'"Happy Mrs Chicken！ That was Peppa\'s favourite game!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Oh no！ My computer is broken！ Daddy Pig, can you mend it?"'],
            "rows":[
                {"child":'假装修/检查',"parent":'"What\'s wrong with it？ Can you fix it？"'},
                {"child":'说 "I can fix it"',"parent":'"Are you sure？ Daddy made it WORSE last time！"'},
                {"child":'说中文',"parent":'家长扮 Daddy："Let me look... hmm..." 假装越弄越糟'},
            ],
        },
        "recast":[
            {"term":"You mustn't touch","explanation":'"Mustn\'t = must not = 绝对不能. Stronger than \'don\'t\'!"'},
            {"term":'I was just showing him what not to do',"explanation":'"What NOT to do = 怎么做是不对的"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Important work！ Don\'t disturb！" — 认真打字状',
            '"Oops！ Wrong button！" — 捂嘴，失误表情',
            '"Can you mend it？" — 假装动手修',
            '"Fixed！ All better！" — 竖大拇指',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Mummy 叫孩子不要碰电脑',"L1":'L1: "Don\'t touch！"',"L2":'L2: "You mustn\'t touch the computer！"',"L3":'L3: "Peppa! You mustn\'t touch the computer. Mummy has important work!"'},
            {"scene":'Peppa 碰了电脑后出问题',"L1":'L1: "Oops！ Wrong！"',"L2":'L2: "Something went wrong！"',"L3":'L3: "I was just showing George what NOT to do... and now the computer is broken!"'},
            {"scene":'Daddy Pig 来修',"L1":'L1: "I can fix it！"',"L2":'L2: "Daddy can mend the computer！"',"L3":'L3: "Don\'t worry! I\'m an expert! I\'ll have it fixed in no time!"'},
        ],
        },
        "bugs":{
            "rule":'说 "mustn\'t" 得2分；说 "important" 得1分；说 "mend" 或 "fix" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'computer → important → touch → mend → button → fixed'},
            {"level":'L2 (句)',"text":"Mummy was working on the computer. They mustn't touch it. But something went wrong. Daddy tried to fix it."},
            {"level":'L3 (完整)',"text":"Mummy Pig had important work to do. She told Peppa and George: you mustn't touch the computer! But Peppa accidentally touched it and it went wrong! Daddy came to mend it — but made it worse! In the end, Mummy pressed one button and fixed everything. Mummy is the real expert!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 or → /ɔː/ 长音',
            "examples":['important', 'work', 'more', 'floor', 'door'],
            "tongue_tip":'嘴巴圆圆，舌头往后，发 /ɔː/。"Important work on the floor！"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP08 Piggy in the Middle（夹心饼干）——" 故意停顿制造悬念',
        "next_a":'EP08 Piggy in the Middle',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"You mustn't touch the computer.","zh":'不能碰电脑',"usage":'真实场景直接用'},
        {"sentence":"I'm an expert.","zh":'我是专家',"usage":'搞笑自称'},
        {"sentence":'I was just showing him what not to do.',"zh":'我只是在示范不该做什么',"usage":'孩子犯错找借口时引用'},
        {"sentence":'Mummy has a lot of important work.',"zh":'妈妈有很多重要工作',"usage":'需要安静空间时用'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 08 · Piggy in the Middle 夹心饼干
# ═══════════════════════════════════════════════════════════════════════════════
EP08 = _ep(
    num=8, title_en='Piggy in the Middle', title_zh='夹心饼干', color='red',
    synopsis='George 在花园踢球，Peppa 嘲笑他踢得不对。Mummy Pig 看到了，教他们玩 Piggy in the Middle 游戏：Mummy 站中间，Peppa 和 George 扔球，Mummy 要拦截。大家玩得非常开心！',
    vocab=[        {"word":'middle',"phonetic":'ˈmɪdl',"pos":'n.',"zh":'中间',"action":'双手比出三个位置，中间那个'},        {"word":'catch',"phonetic":'kætʃ',"pos":'v.',"zh":'接住',"action":'双手张开准备接，"Catch！"'},        {"word":'throw',"phonetic":'θrəʊ',"pos":'v.',"zh":'扔',"action":'手做抛球动作，"Throw it！"'},        {"word":'fair',"phonetic":'feə',"pos":'adj.',"zh":'公平的',"action":'双手伸平做天平，"Fair！"'},        {"word":'tease',"phonetic":'tiːz',"pos":'v.',"zh":'逗弄',"action":'做调皮捉弄的样子，然后摇头'},        {"word":'cheeky',"phonetic":'ˈtʃiːki',"pos":'adj.',"zh":'淘气的',"action":'做鬼脸，"What a cheeky one！"'},        {"word":'teach',"phonetic":'tiːtʃ',"pos":'v.',"zh":'教',"action":'做讲解手势，"I\'ll teach you!"'},        {"word":'well done',"phonetic":'wel dʌn',"pos":'interj.',"zh":'做得好',"action":'鼓掌，"Well done！"'},    ],
    patterns=[        {"pattern":"You're doing it all wrong!","zh":'你完全做错了！',"example":"That's not right! All wrong!"},        {"pattern":'This is how to catch a ball.',"zh":'这才是正确的接球方式',"example":'This is how to hold a pencil correctly.'},        {"pattern":'I know a game that will teach George to catch.',"zh":'我知道一个能教 George 接球的游戏',"example":'I know a game that will make you laugh.'},        {"pattern":'Well done, George!',"zh":'做得好，George！',"example":'Well done! You did it!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第7集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'⚽',"bg":'red',"trigger":'George 和 Peppa 玩球',"action":'做踢球接球动作'},
            {"emoji":'😒',"bg":'orange',"trigger":'Peppa 嘲笑 George',"action":'摇头，"You\'re doing it all wrong！"'},
            {"emoji":'🎉',"bg":'yellow',"trigger":'大家一起玩夹心饼干',"action":'原地跳，"Piggy in the middle！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Was Peppa nice to George at first?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"No!"',"parent":'"NO！ She teased him！ \'You\'re doing it all wrong！\' Poor George. Kind or cheeky?"'},
                {"child":'"Yes!"',"parent":'"She said \'You\'re doing it ALL WRONG!\' Was that kind or cheeky?"'},
                {"child":'不说话',"parent":'模仿 Peppa 嘲笑 George，"Was that nice？ Or cheeky？"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"In Piggy in the Middle, who was the piggy in the middle first?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Mummy!"',"parent":'"YES！ Mummy was in the middle！ She had to jump and catch the ball！"'},
                {"child":'说 George 或 Peppa',"parent":'"They were throwing! Mummy was IN THE MIDDLE！"'},
                {"child":'不说话',"parent":'跳到中间，双手乱抓，"I\'m the PIGGY IN THE MIDDLE！"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"Do you think it\'s fair to make fun of someone trying their best?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'"No!"',"parent":'"RIGHT！ George was trying his best！ Peppa wasn\'t very kind!"'},
                {"child":'"Yes!"',"parent":'"Imagine YOU were trying something new and someone laughed... would that feel good？"'},
                {"child":'不说话',"parent":'"When someone tries hard... we say: Well done！ Not \'all wrong！\'"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever taught someone younger to do something?"'],
            "rows":[
                {"child":'说教过某事',"parent":'"Like Peppa! Though her style was... cheeky at first!"'},
                {"child":'摇头',"parent":'"One day you will！ Teaching is amazing!"'},
                {"child":'笑了',"parent":'"Did it work？ Or did they do it all wrong?"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"I want to play Piggy in the Middle！ You be in the middle？"'],
            "rows":[
                {"child":'说好/站中间',"parent":'"OK！ I\'ll throw the ball... CATCH IT！"'},
                {"child":'说 "Me middle!"',"parent":'"Ready？ Here it comes！"'},
                {"child":'说中文',"parent":'直接开始游戏'},
            ],
        },
        "recast":[
            {"term":"You're doing it all wrong","explanation":'"All wrong = 完全错了。 \'A little wrong\' vs \'all wrong\'"'},
            {"term":'cheeky',"explanation":'"Cheeky = 淘气、有点顽皮. Not bad, just naughty!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Catch the ball！" — 双手张开接球',
            '"Throw it to me！" — 做抛球动作',
            '"Piggy in the middle！" — 跳到两人中间',
            '"Well done！ 👏" — 鼓掌',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Peppa 嘲笑 George',"L1":'L1: "Wrong！ All wrong！"',"L2":'L2: "You\'re doing it all wrong！"',"L3":'L3: "That\'s NOT how to catch a ball! This is how you do it — watch me!"'},
            {"scene":'Mummy 解释游戏规则',"L1":'L1: "Middle！ Catch！"',"L2":'L2: "Mummy is in the middle！"',"L3":'L3: "In Piggy in the Middle, Mummy stands in the middle and tries to catch the ball!"'},
            {"scene":'George 第一次接住球',"L1":'L1: "Got it！"',"L2":'L2: "George caught the ball！"',"L3":'L3: "George caught it! Well done! You ARE good at catching!"'},
        ],
        },
        "bugs":{
            "rule":'说 "Well done" 得1分；说 "in the middle" 得1分；嘲笑别人被说 "cheeky" 扣1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'ball → catch → throw → middle → tease → well done'},
            {"level":'L2 (句)',"text":'George played with the ball. Peppa teased him. Mummy taught them Piggy in the Middle.'},
            {"level":'L3 (完整)',"text":"George was playing with his ball when Peppa came and laughed at him. 'You're doing it all wrong!' Mummy saw and said: I know a game! Piggy in the Middle! Mummy stood in the middle. Peppa and George threw the ball to each other. They all laughed and had fun!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母 ch → /tʃ/ 音',
            "examples":['catch', 'cheeky', 'chicken', 'lunch', 'each'],
            "tongue_tip":'舌尖先堵气，然后快速放开。"Cheeky Peppa catches chickens！"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP09 Daddy Loses His Glasses（爸爸丢了眼镜）——" 故意停顿制造悬念',
        "next_a":'EP09 Daddy Loses His Glasses',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"You're doing it all wrong.","zh":'完全做错了',"usage":'记得加上正确示范'},
        {"sentence":'Well done!',"zh":'做得好！',"usage":'每天至少用5次'},
        {"sentence":'I know a game!',"zh":'我知道一个游戏！',"usage":'提起孩子兴趣的神奇开场白'},
        {"sentence":"That's what you do.","zh":'这才是正确做法',"usage":'示范时配合动作'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 09 · Daddy Loses His Glasses 爸爸丢了眼镜
# ═══════════════════════════════════════════════════════════════════════════════
EP09 = _ep(
    num=9, title_en='Daddy Loses His Glasses', title_zh='爸爸丢了眼镜', color='orange',
    synopsis='Daddy Pig 找不到眼镜，没有眼镜什么都看不清，变得很烦躁。Peppa 和 George 帮他到处找，找了好久都没找到。最后发现眼镜一直戴在 Daddy 自己的头上！',
    vocab=[        {"word":'glasses',"phonetic":'ˈɡlɑːsɪz',"pos":'n.',"zh":'眼镜',"action":'手指搭在鼻子两侧，"Glasses！"'},        {"word":'clearly',"phonetic":'ˈklɪəli',"pos":'adv.',"zh":'清楚地',"action":'眼睛瞪大，"I can see clearly now！"'},        {"word":'fuzzy',"phonetic":'ˈfʌzi',"pos":'adj.',"zh":'模糊的',"action":'用手捂半边视线，"Fuzzy — can\'t see！"'},        {"word":'grumpy',"phonetic":'ˈɡrʌmpi',"pos":'adj.',"zh":'烦躁的',"action":'皱眉，双臂交叉，"I\'m not grumpy！"'},        {"word":'pocket',"phonetic":'ˈpɒkɪt',"pos":'n.',"zh":'口袋',"action":'手插口袋，"In my pocket！"'},        {"word":'search',"phonetic":'sɜːtʃ',"pos":'v.',"zh":'搜寻',"action":'弯腰到处找，"Search everywhere！"'},        {"word":'ridiculous',"phonetic":'rɪˈdɪkjʊləs',"pos":'adj.',"zh":'荒谬的',"action":'摊手，"This is ridiculous！"'},        {"word":'all along',"phonetic":'ɔːl əˈlɒŋ',"pos":'adv.ph.',"zh":'一直都是',"action":'拍额头，"They were there all along！"'},    ],
    patterns=[        {"pattern":"I can't see anything without my glasses.","zh":'没有眼镜什么都看不见',"example":"I can't do anything without my phone!"},        {"pattern":'Do you remember where you last put them?',"zh":'你还记得上次放哪里了吗？',"example":'Do you remember where you left your keys?'},        {"pattern":'They were on his head all along!',"zh":'它们一直都在他头上！',"example":"It was there all along — we just didn't look properly!"},        {"pattern":'Somebody must have moved my glasses.',"zh":'一定有人动了我的眼镜',"example":'Somebody must have eaten my biscuit!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第8集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'👓',"bg":'orange',"trigger":'Daddy 发现找不到眼镜',"action":'假装摸头，"Where are my glasses？"'},
            {"emoji":'🔍',"bg":'yellow',"trigger":'全家帮忙找眼镜',"action":'到处翻，"Not here... not there..."'},
            {"emoji":'😂',"bg":'red',"trigger":'发现眼镜在 Daddy 头上',"action":'拍额头，大笑'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Where were Daddy Pig\'s glasses all along?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"On his head!"',"parent":'"YES！ On his HEAD！ He was looking EVERYWHERE — they were right there ALL ALONG！"'},
                {"child":'说口袋/桌上',"parent":'"That\'s where he THOUGHT they were! But actually... on his HEAD!"'},
                {"child":'不说话',"parent":'假装摸自己头上，做惊讶表情'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Was Daddy grumpy when he couldn\'t find his glasses?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Grumpy!"',"parent":'"VERY grumpy！ \'This is ridiculous！ Somebody must have moved them！\'"'},
                {"child":'"Calm!"',"parent":'"He said \'I\'m not grumpy\' — but he was！"'},
                {"child":'不说话',"parent":'皱眉双臂交叉，"I am NOT grumpy." — 等孩子笑'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"In your house, who is most likely to lose something?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'指大人',"parent":'"Like Daddy Pig！ Do they say \'Somebody must have moved it\'?"'},
                {"child":'指自己',"parent":'"You? What do you usually lose?"'},
                {"child":'不说话',"parent":'"In our house... who is the most forgetful?" 故意看着孩子'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever looked everywhere for something and found it somewhere obvious?"'],
            "rows":[
                {"child":'说过经历',"parent":'"Like Daddy Pig！ How did you feel when you found it？"'},
                {"child":'摇头',"parent":'"Never？ Maybe you\'re better at remembering than Daddy Pig!"'},
                {"child":'笑了',"parent":'"Imagine looking for your glasses for ten minutes... and they\'re on your head！"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"OH NO！ I\'ve lost my glasses！ Can you help me？"'],
            "rows":[
                {"child":'开始帮找',"parent":'"They\'re not here... not there... Could they be on my...?" 慢慢摸到头上'},
                {"child":'说 "head!"',"parent":'"ON MY HEAD？！ They were there all along！"'},
                {"child":'说中文',"parent":'家长假装找不到，让孩子当侦探'},
            ],
        },
        "recast":[
            {"term":'all along',"explanation":'"All along = 一直以来，从头到尾"'},
            {"term":'ridiculous',"explanation":'"Ridiculous = 荒谬的、可笑的"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Put on your glasses！" — 假装戴眼镜',
            '"I can\'t see！ Everything\'s fuzzy！" — 眯眼，伸手摸索',
            '"Search everywhere！" — 到处翻找',
            '"On my head all along！" — 拍额头，大笑',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Daddy 找不到眼镜很烦躁',"L1":'L1: "Where？ Glasses？"',"L2":'L2: "Where are my glasses？"',"L3":'L3: "This is ridiculous! I can\'t see anything! Somebody must have moved my glasses!"'},
            {"scene":'Peppa 和 George 帮忙找',"L1":'L1: "Not here..."',"L2":'L2: "We\'ll look everywhere！"',"L3":'L3: "Don\'t worry, Daddy! We\'ll find them. George, check the TV. I\'ll look under the newspaper!"'},
            {"scene":'发现眼镜在头上',"L1":'L1: "OH！ Head！"',"L2":'L2: "They\'re on your head！"',"L3":'L3: "Daddy Pig！ Your glasses are on your HEAD！ They were there all along！"'},
        ],
        },
        "bugs":{
            "rule":'说 "all along" 得2分；说 "grumpy" 得1分；说 "ridiculous" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'glasses → lost → fuzzy → grumpy → search → head → all along'},
            {"level":'L2 (句)',"text":"Daddy lost his glasses. He couldn't see. He was grumpy. Everyone searched. The glasses were on his head."},
            {"level":'L3 (完整)',"text":"Daddy Pig needs glasses to see clearly. Without them, everything looks fuzzy and he gets grumpy! He said 'Somebody must have moved my glasses!' Peppa and George searched everywhere. Nothing! Then they looked at Daddy's head... and there they were! On his head all along! Everyone laughed. Even grumpy Daddy Pig."},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ear → /ɪə/ 双元音',
            "examples":['clearly', 'hear', 'ear', 'year', 'near'],
            "tongue_tip":'从 /ɪ/ 滑向 /ə/，"伊-呃" 连起来。"Can you hear clearly？"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP10 Gardening（种花园）——" 故意停顿制造悬念',
        "next_a":'EP10 Gardening',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'They were there all along!',"zh":'它们一直都在那里！',"usage":'找到东西后的经典感叹'},
        {"sentence":"I'm not grumpy.","zh":'我没有不高兴',"usage":'谁说这句谁一定很 grumpy'},
        {"sentence":"I can't see anything without my glasses.","zh":'没有眼镜什么都看不见',"usage":'丢东西时的模拟场景'},
        {"sentence":'Somebody must have moved my glasses.',"zh":'一定有人动了我的眼镜',"usage":'幽默甩锅的句式'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 21 · Mummy Pig's Birthday 猪妈妈的生日
# ═══════════════════════════════════════════════════════════════════════════════
EP21 = _ep(
    num=21, title_en="Mummy Pig's Birthday", title_zh='猪妈妈的生日', color='pink',
    synopsis='今天是 Mummy Pig 的生日！Daddy 做了早餐送到床上，Peppa 和 George 做了生日卡。Daddy 还做了生日蛋糕，大家一起唱生日歌，Mummy 许愿吹灭蜡烛。',
    vocab=[        {"word":'birthday',"phonetic":'ˈbɜːθdeɪ',"pos":'n.',"zh":'生日',"action":'双手做蛋糕状，嘴巴轻吹蜡烛'},        {"word":'candle',"phonetic":'ˈkændl',"pos":'n.',"zh":'蜡烛',"action":'食指向上，假装是蜡烛'},        {"word":'wish',"phonetic":'wɪʃ',"pos":'v./n.',"zh":'许愿',"action":'闭眼，双手合十，"Make a wish！"'},        {"word":'surprise',"phonetic":'səˈpraɪz',"pos":'n.',"zh":'惊喜',"action":'捂嘴，眼睛睁大'},        {"word":'cake',"phonetic":'keɪk',"pos":'n.',"zh":'蛋糕',"action":'双手做出圆形，"Birthday cake！"'},        {"word":'card',"phonetic":'kɑːd',"pos":'n.',"zh":'卡片',"action":'假装打开一张卡，"Happy birthday!"'},        {"word":'present',"phonetic":'ˈpreznt',"pos":'n.',"zh":'礼物',"action":'假装接过包装礼物'},        {"word":'blow',"phonetic":'bləʊ',"pos":'v.',"zh":'吹',"action":'嘴巴圆，深呼吸，使劲吹'},    ],
    patterns=[        {"pattern":'Happy birthday, Mummy Pig!',"zh":'生日快乐！',"example":'Happy birthday, [name]!'},        {"pattern":'There are more surprises to come.',"zh":'还有更多惊喜',"example":'Wait, there are more surprises!'},        {"pattern":'Make a wish!',"zh":'许个愿望！',"example":'Close your eyes and make a wish!'},        {"pattern":'What a lovely birthday surprise!',"zh":'多美的生日惊喜！',"example":'What a lovely present!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第20集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🎂',"bg":'pink',"trigger":'Daddy 点燃蛋糕蜡烛',"action":'假装点蜡烛，"One candle... two..."'},
            {"emoji":'🎁',"bg":'yellow',"trigger":'大家送礼物给 Mummy',"action":'假装递礼物，"Happy birthday！"'},
            {"emoji":'🕯️',"bg":'red',"trigger":'Mummy 许愿吹蜡烛',"action":'闭眼，深吸气，使劲吹'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Who made breakfast in bed for Mummy Pig on her birthday?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Daddy!"',"parent":'"YES！ Daddy made breakfast in bed！ And Peppa and George made a birthday card！"'},
                {"child":'说 Peppa',"parent":'"Peppa made a birthday CARD！ But who made the breakfast？ Daddy!"'},
                {"child":'不说话',"parent":'假装端早餐进卧室，"Happy birthday！ Breakfast in bed！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"How many candles did Mummy Pig have?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说数字',"parent":'"Daddy was still counting when Mummy came in！ He wasn\'t ready yet！"'},
                {"child":'不知道',"parent":'"Daddy was still putting them on when Mummy arrived!"'},
                {"child":'不说话',"parent":'假装放蜡烛，"One... two..." 然后做惊慌样，"Mummy\'s coming！"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If it was YOUR birthday tomorrow, what ONE wish would you make?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说愿望',"parent":'"Close your eyes！ Make that wish RIGHT NOW！ Sssh!"'},
                {"child":'说礼物/蛋糕',"parent":'"What flavour cake？ Can I have some？"'},
                {"child":'不说话',"parent":'"My wish would be..." 凑近耳边轻声说个愿望，"Your turn！"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"What\'s the best birthday surprise you\'ve ever had?"'],
            "rows":[
                {"child":'说经历',"parent":'"That was YOUR best surprise！ Better than breakfast in bed？"'},
                {"child":'说不知道',"parent":'"No surprise？ Maybe this year someone will plan something special..." 神秘微笑'},
                {"child":'笑了',"parent":'"Was there a birthday CAKE？ Did you make a wish？"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"SURPRISE！ Happy birthday！ Close your eyes — we have a cake！"'],
            "rows":[
                {"child":'闭眼/配合',"parent":'假装点蜡烛，"Make a wish！ Ready？ BLOW！"'},
                {"child":'说 "Happy birthday"',"parent":'"AND TO YOU TOO！ Open your present!"'},
                {"child":'说中文',"parent":'家长扮 Mummy："Oh！ What a lovely surprise！ A birthday cake！"'},
            ],
        },
        "recast":[
            {"term":'Happy birthday',"explanation":'"Happy birthday = 生日快乐。 Say it ON the birthday!"'},
            {"term":'make a wish',"explanation":'"Make + wish = 许愿。 Make + cake = 做蛋糕！"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Blow out the candles！ One... blow！" — 深吸气，用力吹',
            '"Surprise！" — 跳出来，双手张开',
            '"Make a wish！ Close your eyes！" — 闭眼，双手合十',
            '"Happy birthday！ 🎂" — 鼓掌，唱生日歌',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Daddy 端早餐进卧室',"L1":'L1: "Happy birthday！"',"L2":'L2: "Happy birthday, Mummy Pig！"',"L3":'L3: "Happy birthday! Here is your breakfast! And Peppa and George made you a birthday card!"'},
            {"scene":'Daddy 还没准备好蛋糕',"L1":'L1: "Not ready！"',"L2":'L2: "We\'re not ready yet！"',"L3":'L3: "Oh no！ Mummy\'s coming! Quick — light the candles！"'},
            {"scene":'Mummy 许愿吹蜡烛',"L1":'L1: "Wish！ Blow！"',"L2":'L2: "Make a wish and blow！"',"L3":'L3: "Close your eyes, Mummy! Make a wish! Now blow out all the candles!"'},
        ],
        },
        "bugs":{
            "rule":'说 "Happy birthday" 得1分；说 "make a wish" 得2分；唱生日歌得3分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'birthday → cake → candles → wish → surprise → blow → present'},
            {"level":'L2 (句)',"text":"Today was Mummy's birthday. Daddy made breakfast in bed. They had a party with a cake."},
            {"level":'L3 (完整)',"text":"It was Mummy Pig's birthday! Daddy made her breakfast in bed. Then a big surprise — a birthday cake with candles! Friends came to celebrate. Everyone sang Happy Birthday. Mummy made a wish and blew out all the candles! What a wonderful birthday!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ir/ur/er → /ɜː/ 音',
            "examples":['birthday', 'girl', 'bird', 'her', 'turn'],
            "tongue_tip":'嘴微圆，舌头不动，发 /ɜː/ 像 "嗯..."。"Happy birthday, birthday girl!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP22 The Tooth Fairy（牙仙子）——" 故意停顿制造悬念',
        "next_a":'EP22 The Tooth Fairy',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Happy birthday!',"zh":'生日快乐！',"usage":'每年生日必用'},
        {"sentence":'There are more surprises to come!',"zh":'还有更多惊喜！',"usage":'制造期待感'},
        {"sentence":'Make a wish!',"zh":'许个愿望！',"usage":'吹蜡烛前的仪式感'},
        {"sentence":'What a lovely birthday surprise!',"zh":'多美的生日惊喜！',"usage":'感叹句模板'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 22 · The Tooth Fairy 牙仙子
# ═══════════════════════════════════════════════════════════════════════════════
EP22 = _ep(
    num=22, title_en='The Tooth Fairy', title_zh='牙仙子', color='yellow',
    synopsis='Peppa 吃意大利面时一颗乳牙掉了！Mummy 解释乳牙掉落是正常的，还会长新牙。更棒的是——牙仙子会来！把牙齿放枕头下，牙仙子会换一枚闪亮的硬币！',
    vocab=[        {"word":'tooth',"phonetic":'tuːθ',"pos":'n.',"zh":'牙齿（单）',"action":'指自己的牙，"One tooth！"'},        {"word":'teeth',"phonetic":'tiːθ',"pos":'n.',"zh":'牙齿（复）',"action":'张大嘴，"All my teeth！"'},        {"word":'fairy',"phonetic":'ˈfeəri',"pos":'n.',"zh":'仙子',"action":'做飞翔的手势，"The fairy flies！"'},        {"word":'pillow',"phonetic":'ˈpɪləʊ',"pos":'n.',"zh":'枕头',"action":'双手合拢放脸旁，假装睡觉'},        {"word":'coin',"phonetic":'kɔɪn',"pos":'n.',"zh":'硬币',"action":'拇指和食指做圆形，"A coin！"'},        {"word":'shiny',"phonetic":'ˈʃaɪni',"pos":'adj.',"zh":'闪亮的',"action":'眼睛发光，"Shiny！ So bright！"'},        {"word":'milk tooth',"phonetic":'mɪlk tuːθ',"pos":'n.',"zh":'乳牙',"action":'指嘴，"Baby teeth. They fall out!"'},        {"word":'grow',"phonetic":'ɡrəʊ',"pos":'v.',"zh":'长出',"action":'手指慢慢伸出，"New tooth growing in!"'},    ],
    patterns=[        {"pattern":"They're meant to fall out.","zh":'它们注定会脱落',"example":"Baby teeth are meant to fall out. It's normal!"},        {"pattern":'Will I grow a new one, Mummy?',"zh":'妈妈，我会长新的吗？',"example":'Will I grow taller?'},        {"pattern":'The tooth fairy will come tonight.',"zh":'今晚牙仙子会来',"example":"She'll leave something under your pillow!"},        {"pattern":'When I grow up, I want to be a tooth fairy.',"zh":'我长大想当牙仙子',"example":'When I grow up, I want to be a doctor.'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第21集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🦷',"bg":'yellow',"trigger":'Peppa 的牙掉到碗里',"action":'做惊讶表情，捂嘴，"A tooth！"'},
            {"emoji":'🧚',"bg":'pink',"trigger":'讲解牙仙子',"action":'飞翔手势，"The tooth fairy comes at night！"'},
            {"emoji":'🪙',"bg":'gold',"trigger":'枕头下的惊喜',"action":'假装把东西放枕头下，发现硬币'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What does the tooth fairy do?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Take tooth, leave coin!"',"parent":'"YES！ She takes the tooth and leaves a shiny coin！ Under the pillow！"'},
                {"child":'搞反了',"parent":'"She takes the TOOTH and leaves a COIN! Not the other way!"'},
                {"child":'不说话',"parent":'假装把牙放枕头下，睡觉，拿出硬币，"The fairy came！ A COIN！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What does George want to be when he grows up?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Dinosaur!"',"parent":'"A DINOSAUR！ Classic George！ And what do YOU want to be？"'},
                {"child":'说其他',"parent":'"George had a special answer — starts with D... Dino..."'},
                {"child":'笑了',"parent":'"GRRR！ George the dinosaur！ Peppa the tooth fairy！"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"Have you ever lost a tooth? What happened?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说过丢牙',"parent":'"Did the tooth fairy come？ Did you find a coin？"'},
                {"child":'还没丢过',"parent":'"Your teeth are all still there？ Any feel a bit wobbly?" 假装检查'},
                {"child":'不说话',"parent":'"My first lost tooth... I put it under my pillow and waited..."'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"If you were the tooth fairy, what would YOU leave under the pillow?"'],
            "rows":[
                {"child":'说礼物/零食',"parent":'"A [item]！ Children would love that！"'},
                {"child":'说硬币',"parent":'"Still a coin？ Sensible! How much?"'},
                {"child":'不说话',"parent":'"I\'d leave a tiny note: \'I borrowed your tooth. Building a fairy castle!\'"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Psst！ I am the tooth fairy！ Do you have a tooth for me？"'],
            "rows":[
                {"child":'假装给牙',"parent":'"Thank you！ Here is your shiny coin！ Sweet dreams！"'},
                {"child":'说 "coin"',"parent":'"YES！ A shiny coin！ Put your tooth under the pillow！"'},
                {"child":'说中文',"parent":'家长扮牙仙子："I fly at night！ Leave your tooth under the pillow！"'},
            ],
        },
        "recast":[
            {"term":'meant to fall out',"explanation":'"Meant to = 注定的。 Baby teeth are meant to fall out."'},
            {"term":'shiny',"explanation":'"Shiny = 闪闪发光。 Shiny coin, shiny star, shiny eyes!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Wiggle your tooth！" — 假装摇松一颗牙',
            '"Put it under the pillow！" — 假装放枕头下',
            '"The tooth fairy is coming！ Shhh！" — 飞翔手势，食指放嘴唇',
            '"A shiny coin！" — 眼睛发光，捏起想象的硬币',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Peppa 牙掉到碗里',"L1":'L1: "My tooth！"',"L2":'L2: "My tooth fell out！"',"L3":'L3: "What\'s that in my spaghetti？ Oh! It\'s my tooth!"'},
            {"scene":'Mummy 解释牙仙子',"L1":'L1: "Tooth fairy！ Coin！"',"L2":'L2: "The tooth fairy leaves a shiny coin！"',"L3":'L3: "Put your tooth under your pillow. The fairy will leave a shiny coin!"'},
            {"scene":'Peppa 说长大想当牙仙子',"L1":'L1: "Tooth fairy！"',"L2":'L2: "I want to be a tooth fairy！"',"L3":'L3: "When I grow up, I want to be a tooth fairy! I\'d fly around collecting teeth!"'},
        ],
        },
        "bugs":{
            "rule":'说 "tooth fairy" 得2分；说 "shiny" 得1分；说 "under the pillow" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'tooth → fairy → pillow → coin → shiny → grow'},
            {"level":'L2 (句)',"text":"Peppa's tooth fell out. Mummy said it's normal. The tooth fairy will leave a coin."},
            {"level":'L3 (完整)',"text":"Peppa was eating spaghetti when her tooth fell out! Mummy said: don't worry, they're meant to fall out. You'll grow a new one! And the tooth fairy will come! Put your tooth under your pillow — she'll leave a shiny coin. Peppa wants to be a tooth fairy when she grows up. George wants to be a dinosaur!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 th → /θ/ 清音',
            "examples":['tooth', 'teeth', 'think', 'three', 'thank'],
            "tongue_tip":'舌尖轻触上门牙背面，气流轻推出。"Think of three teeth!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP23 The New Car（新汽车）——" 故意停顿制造悬念',
        "next_a":'EP23 The New Car',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"They're meant to fall out.","zh":'注定会脱落',"usage":'孩子第一次掉牙时安慰'},
        {"sentence":'The tooth fairy will come tonight.',"zh":'今晚牙仙子会来',"usage":'睡前制造期待感'},
        {"sentence":'When I grow up, I want to be a...',"zh":'我长大想当...',"usage":'引导孩子说职业梦想'},
        {"sentence":'A shiny coin!',"zh":'一枚闪亮的硬币',"usage":'描述闪亮东西的万用句'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 23 · The New Car 新汽车
# ═══════════════════════════════════════════════════════════════════════════════
EP23 = _ep(
    num=23, title_en='The New Car', title_zh='新汽车', color='red',
    synopsis='Peppa 一家开着他们的红色旧车出门，结果车发出奇怪的声音！他们去了 Granddad Dog 的修车行，需要修一整天。于是一家人去看新车，最后买了一辆新车！',
    vocab=[        {"word":'garage',"phonetic":'ˈɡærɑːʒ',"pos":'n.',"zh":'修车行/车库',"action":'假装推开大门，"The garage！"'},        {"word":'mend',"phonetic":'mend',"pos":'v.',"zh":'修理',"action":'假装扳手拧零件，"Mend the car！"'},        {"word":'brand new',"phonetic":'brænd njuː',"pos":'adj.',"zh":'全新的',"action":'双手展示，"Brand new！ Nobody used it before！"'},        {"word":'shiny',"phonetic":'ˈʃaɪni',"pos":'adj.',"zh":'闪亮的',"action":'发光的样子，"Shiny！ So bright！"'},        {"word":'roof',"phonetic":'ruːf',"pos":'n.',"zh":'屋顶/车顶',"action":'双手摆在头顶，"The roof of the car！"'},        {"word":'engine',"phonetic":'ˈendʒɪn',"pos":'n.',"zh":'引擎',"action":'做出引擎轰鸣声，"Vroom！ The engine！"'},        {"word":'broken',"phonetic":'ˈbrəʊkən',"pos":'adj.',"zh":'坏了',"action":'耸肩，"Oh no！ It\'s broken！"'},        {"word":'choose',"phonetic":'tʃuːz',"pos":'v.',"zh":'选择',"action":'左右摇摆，"Choose... this one or that one？"'},    ],
    patterns=[        {"pattern":'Shall we have the roof down?',"zh":'我们把车顶打开吗？',"example":'Shall we have some music?'},        {"pattern":'It will take all day.',"zh":'要修一整天',"example":'This will take all day. We need time.'},        {"pattern":'Granddad Dog can fix it.',"zh":'Granddad Dog 能修好它',"example":"He's very good at mending things."},        {"pattern":"We'll take it to the garage.","zh":'我们把它开到修车行',"example":"Let's take it to someone who can fix it."},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第22集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🚗',"bg":'red',"trigger":'全家一起开车出门',"action":'假装开车，发动引擎声'},
            {"emoji":'⚙️',"bg":'yellow',"trigger":'车发出奇怪声音',"action":'做出困惑表情，"Hmm！ That doesn\'t sound right！"'},
            {"emoji":'🆕',"bg":'green',"trigger":'大家在看新车',"action":'眼睛发光，"So shiny！ Brand new！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What was wrong with Peppa\'s family car?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说发出怪声/坏了',"parent":'"YES！ The car made a strange noise! It needed mending!"'},
                {"child":'说不知道',"parent":'"It made a very strange sound... not normal! It needed to go to the garage!"'},
                {"child":'不说话',"parent":'做出引擎怪声，"What does that sound like？ Good or bad？"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Who fixed the family car?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说 Granddad Dog',"parent":'"YES！ Granddad Dog! He\'s very good at mending cars! He runs the garage!"'},
                {"child":'说 Daddy',"parent":'"Daddy Pig couldn\'t fix this one! They went to Granddad Dog\'s garage!"'},
                {"child":'不说话',"parent":'"Woof！ Who says woof？ Granddad Dog! And he runs the...?" 等孩子说 garage'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you could choose any colour for a new car, what would YOU pick?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说颜色',"parent":'"A [colour] car！ Would it be shiny？ And would it have the roof down？"'},
                {"child":'说 red',"parent":'"RED！ Like Peppa\'s family car! Classic choice！"'},
                {"child":'不说话',"parent":'"Me — I\'d choose... a rainbow car! No wait, maybe just blue. What about you？"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever been in a car when something went wrong?"'],
            "rows":[
                {"child":'说经历',"parent":'"Like Peppa\'s family！ What happened？ Did someone fix it？"'},
                {"child":'摇头',"parent":'"Lucky you！ Peppa\'s car made a VERY strange noise..."'},
                {"child":'不说话',"parent":'做出引擎怪声，等孩子笑'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Welcome to Granddad Dog\'s garage！ Woof！ What\'s wrong with your car?"'],
            "rows":[
                {"child":'说坏了/怪声',"parent":'"Hmm! Let me check the engine... Woof woof!" 假装检查'},
                {"child":'做引擎声',"parent":'"Yes! That doesn\'t sound right! I\'ll mend it! Come back tomorrow!"'},
                {"child":'说中文',"parent":'家长扮 Granddad Dog："Woof！ Oh dear. Your car needs mending！"'},
            ],
        },
        "recast":[
            {"term":'brand new',"explanation":'"Brand new = 全新的，没有人用过。 Brand new car!"'},
            {"term":'take all day',"explanation":'"Take + time = 花费时间。 It will take all day = 要花一整天"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Start the engine！ Vroom！" — 假装转钥匙，发动引擎声',
            '"Something\'s wrong！" — 皱眉，捂耳朵',
            '"Take it to the garage！" — 假装推车',
            '"Brand new! So shiny！" — 眼睛发光，摸想象的新车',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'全家出门开车',"L1":'L1: "Car！ Vroom！"',"L2":'L2: "I love our red car！"',"L3":'L3: "Shall we have the roof down? Let\'s go! Our car loves us!"'},
            {"scene":'车发出怪声',"L1":'L1: "Hmm！ Wrong！"',"L2":'L2: "Our car doesn\'t sound very well！"',"L3":'L3: "What\'s that noise？ Something is wrong with our car!"'},
            {"scene":'在修车行看新车',"L1":'L1: "New！ Shiny！"',"L2":'L2: "A brand new shiny car！"',"L3":'L3: "Look at that brand new car! It\'s so shiny! Shall we get this one?"'},
        ],
        },
        "bugs":{
            "rule":'说 "brand new" 得2分；说 "garage" 得1分；说出颜色+car 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'car → garage → broken → mend → brand new → shiny'},
            {"level":'L2 (句)',"text":"Peppa's family went for a drive. The car made a strange noise. Granddad Dog mended it. They got a new car."},
            {"level":'L3 (完整)',"text":"Peppa's family went for a drive in their red car. Then the car made a strange noise — something was wrong! They went to Granddad Dog's garage. He said it would take all day! So the family looked at other cars... and they found a beautiful brand new shiny car!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ar → /ɑː/ 长音',
            "examples":['car', 'garage', 'garden', 'start', 'park'],
            "tongue_tip":'嘴大张，舌头往后下，发 /ɑː/。"The car is parked in the garden!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP24 Treasure Hunt（寻宝游戏）——" 故意停顿制造悬念',
        "next_a":'EP24 Treasure Hunt',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Shall we have the roof down?',"zh":'我们把车顶打开吗？',"usage":'乘车时制造开心仪式感'},
        {"sentence":'It will take all day.',"zh":'要花一整天',"usage":'设定时间期待值'},
        {"sentence":'Brand new!',"zh":'全新的！',"usage":'形容任何新买的东西'},
        {"sentence":"That doesn't sound very well.","zh":'听起来不太对劲',"usage":'汽车或任何东西发出怪声时'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 24 · Treasure Hunt 寻宝游戏
# ═══════════════════════════════════════════════════════════════════════════════
EP24 = _ep(
    num=24, title_en='Treasure Hunt', title_zh='寻宝游戏', color='yellow',
    synopsis='爷爷奶奶为 Peppa 和 George 准备了寻宝游戏！Grandpa 画了藏宝图，把宝藏藏在了花园里。Peppa 和 George 跟着地图线索一步步寻找，最终挖出了宝藏！',
    vocab=[        {"word":'treasure',"phonetic":'ˈtreʒə',"pos":'n.',"zh":'宝藏',"action":'做出挖宝的姿势，眼睛发光，"TREASURE！"'},        {"word":'map',"phonetic":'mæp',"pos":'n.',"zh":'地图',"action":'展开想象的地图，"The map shows where to go!"'},        {"word":'clue',"phonetic":'kluː',"pos":'n.',"zh":'线索',"action":'食指指着地图，"Follow the clue！"'},        {"word":'bury',"phonetic":'ˈberi',"pos":'v.',"zh":'埋',"action":'弯腰，假装挖洞埋东西'},        {"word":'pirate',"phonetic":'ˈpaɪrət',"pos":'n.',"zh":'海盗',"action":'双手叉腰，"Ahoy there, matey！"'},        {"word":'dig',"phonetic":'dɪɡ',"pos":'v.',"zh":'挖掘',"action":'做出用铲子挖地的动作'},        {"word":'secret',"phonetic":'ˈsiːkrɪt',"pos":'n.',"zh":'秘密',"action":'凑近耳边，"It\'s a secret！ Sssh！"'},        {"word":'discover',"phonetic":'dɪˈskʌvə',"pos":'v.',"zh":'发现',"action":'张开双手，"Discovered! Found it!"'},    ],
    patterns=[        {"pattern":'Somewhere in the garden is buried treasure.',"zh":'花园某处藏着宝藏',"example":'Somewhere in this room is a surprise!'},        {"pattern":'Ahoy there, me hearties!',"zh":'哈罗，我的伙计们！',"example":'Ahoy! A pirate greeting!'},        {"pattern":'The map is a bit difficult.',"zh":'地图有点难看懂',"example":'This map is hard — can you help?'},        {"pattern":'X marks the spot.',"zh":'X 标记就是那个地方',"example":"That's where it is — X marks the spot!"},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第23集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🗺️',"bg":'gold',"trigger":'Grandpa 给出藏宝图',"action":'展开想象地图，"Follow the map！"'},
            {"emoji":'⚓',"bg":'blue',"trigger":'Grandpa 戴上海盗帽',"action":'双手叉腰，"Ahoy there！"'},
            {"emoji":'💎',"bg":'gold',"trigger":'挖出宝藏',"action":'做出挖掘动作，然后惊喜发现'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Who made the treasure hunt — Granny, Grandpa, or both?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Both!"',"parent":'"YES！ Granny drew the map and Grandpa buried the treasure！ Teamwork！"'},
                {"child":'说 Grandpa',"parent":'"Grandpa buried the treasure! But Granny drew the MAP! Both helped！"'},
                {"child":'不说话',"parent":'"Granny drew this..." 假装画地图，"Grandpa dug this..." 假装挖洞'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What did Captain George wear on his head?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Pirate hat!"',"parent":'"YES！ Grandpa\'s pirate hat！ \'Ahoy there, Captain George！\'"'},
                {"child":'说其他',"parent":'"Grandpa gave George his special hat — a PIRATE hat! Ahoy!"'},
                {"child":'不说话',"parent":'假装戴帽子，"Ahoy there！ Are you a pirate？"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you buried treasure in our garden, what would you put inside?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说物品',"parent":'"A [item]！ What a great treasure! How deep would you bury it?"'},
                {"child":'说金币/宝石',"parent":'"Real treasure！ Like a pirate! X marks the spot！"'},
                {"child":'不说话',"parent":'"I\'d bury a chocolate bar... but it might melt. What would YOU bury？"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever gone on a treasure hunt or scavenger hunt?"'],
            "rows":[
                {"child":'说经历',"parent":'"Did you find the treasure？ What was it？"'},
                {"child":'摇头',"parent":'"Let\'s make one！ I\'ll hide something... you follow the clues..."'},
                {"child":'笑了',"parent":'"Was there a map？ Did you dig？ Like a real pirate!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Ahoy there！ You are a pirate！ Here is your treasure map！"'],
            "rows":[
                {"child":'假装看地图',"parent":'"The first clue says... go to the big tree! What\'s there？"'},
                {"child":'说 "treasure!"',"parent":'"Dig！ Dig！ TREASURE！ What\'s inside？"'},
                {"child":'说中文',"parent":'家长扮 Grandpa："Ahoy！ Captain！ Follow the map!"'},
            ],
        },
        "recast":[
            {"term":'Ahoy there, me hearties',"explanation":'"Ahoy = 海盗打招呼。 Me hearties = 我的伙计们！"'},
            {"term":'X marks the spot',"explanation":'"X marks the spot = X 标记的就是那个地方"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Read the map！ Which way？" — 展开地图，指向不同方向',
            '"Dig！ Dig！ Dig！" — 做铲子挖地动作',
            '"Ahoy there！" — 双手叉腰，海盗姿态',
            '"TREASURE！ Found it！" — 惊喜举起双手',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Grandpa 介绍藏宝游戏',"L1":'L1: "Treasure！"',"L2":'L2: "Somewhere in the garden is buried treasure！"',"L3":'L3: "Ahoy! We\'ve made you a treasure hunt! Use the map to find the treasure!"'},
            {"scene":'Peppa 看地图',"L1":'L1: "Map！ Clue！"',"L2":'L2: "The map shows where to go！"',"L3":'L3: "The map is a bit difficult... Daddy, can you help? We need to follow the clues!"'},
            {"scene":'找到宝藏',"L1":'L1: "Found！ Treasure！"',"L2":'L2: "We found the treasure！"',"L3":'L3: "X marks the spot! Dig here! We found the treasure! Open it! What\'s inside?"'},
        ],
        },
        "bugs":{
            "rule":'说 "treasure" 得1分；说 "Ahoy" 得1分；用地图词汇（map/clue/spot）得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'treasure → map → clue → pirate → dig → found'},
            {"level":'L2 (句)',"text":'Granny and Grandpa made a treasure hunt. Granny drew the map. Grandpa buried the treasure. They found it!'},
            {"level":'L3 (完整)',"text":"Granny and Grandpa made a special treasure hunt for Peppa and George! Granny drew a treasure map. Grandpa buried the treasure in a secret place in the garden. George wore Grandpa's pirate hat. They followed the map and the clues. X marks the spot — DIG！ They found the treasure! What a brilliant adventure!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ure → /ʒə/ 或 /tʃə/ 音',
            "examples":['treasure', 'adventure', 'measure', 'pleasure', 'nature'],
            "tongue_tip":'结尾 -ure 通常轻读。"Treasure！ Adventure！ What a pleasure!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP25 Not Very Well（生病了）——" 故意停顿制造悬念',
        "next_a":'EP25 Not Very Well',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Ahoy there, me hearties!',"zh":'哈罗，我的伙计们！',"usage":'打招呼的趣味方式'},
        {"sentence":'Somewhere in the garden is buried treasure.',"zh":'花园里藏着宝藏',"usage":'在家里藏惊喜前用这句'},
        {"sentence":'X marks the spot.',"zh":'X 标记就是那里',"usage":'找东西时画一个X'},
        {"sentence":'Follow the map!',"zh":'跟着地图走！',"usage":'日常出游时用'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 25 · Not Very Well 生病了
# ═══════════════════════════════════════════════════════════════════════════════
EP25 = _ep(
    num=25, title_en='Not Very Well', title_zh='生病了', color='green',
    synopsis='Peppa 脸上长了红斑，感觉不舒服。Dr Brown Bear 来看诊，说只是皮疹，没有大问题，给了一些药。Peppa 的好朋友们纷纷来探病，结果每个人都出了红斑！',
    vocab=[        {"word":'spots',"phonetic":'spɒts',"pos":'n.',"zh":'红疹、斑点',"action":'用手指点在脸上，"Spots！ Red spots！"'},        {"word":'rash',"phonetic":'ræʃ',"pos":'n.',"zh":'皮疹',"action":'指脸，"A rash — little red spots"'},        {"word":'medicine',"phonetic":'ˈmedɪsn',"pos":'n.',"zh":'药',"action":'假装喝药，皱眉，"Ewww！ Medicine！"'},        {"word":'stick out',"phonetic":'stɪk aʊt',"pos":'v.ph.',"zh":'伸出（舌头）',"action":'做出伸舌头动作，"Stick out your tongue！ AHHH！"'},        {"word":'serious',"phonetic":'ˈsɪəriəs',"pos":'adj.',"zh":'严重的',"action":'严肃表情，"Is it serious？ Or not serious？"'},        {"word":'brave',"phonetic":'breɪv',"pos":'adj.',"zh":'勇敢的',"action":'挺胸，"You are very brave！"'},        {"word":'better',"phonetic":'ˈbetə',"pos":'adj.',"zh":'好转的',"action":'竖大拇指，"All better！ Feeling much better!"'},        {"word":'disgusting',"phonetic":'dɪsˈɡʌstɪŋ',"pos":'adj.',"zh":'令人恶心的',"action":'皱眉，伸舌头，"Disgusting！ Ewww！"'},    ],
    patterns=[        {"pattern":"I don't feel very well.","zh":'我感觉不太好',"example":"I don't feel very well today. I think I'm sick."},        {"pattern":"It's not anything serious.","zh":'不是什么严重的',"example":"Don't worry, it's not anything serious."},        {"pattern":'You are a brave little one.',"zh":'你是个勇敢的小家伙',"example":'You are so brave for taking the medicine!'},        {"pattern":'The rash will clear up quickly.',"zh":'皮疹很快就会消退',"example":"Don't worry, it will clear up."},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第24集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🤒',"bg":'green',"trigger":'Peppa 脸上有红斑，不舒服',"action":'皱眉，摸脸，"I don\'t feel very well..."'},
            {"emoji":'🐻',"bg":'blue',"trigger":'Dr Brown Bear 来看诊',"action":'假装听诊器，"Stick out your tongue！"'},
            {"emoji":'💊',"bg":'yellow',"trigger":'吃了难喝的药',"action":'做喝药皱眉，"Disgusting！ Ewww！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What was wrong with Peppa?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说红斑/皮疹',"parent":'"Red spots！ A rash！ Dr Brown Bear said it\'s not serious — just a rash!"'},
                {"child":'说生病了',"parent":'"She had red spots all over her face — a rash! But Dr Brown Bear said..."'},
                {"child":'不说话',"parent":'用手指点在脸上，"Red spots！ Like this！ What do you call them？"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Did the medicine taste nice?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"No！ Disgusting!"',"parent":'"YES — DISGUSTING！ But Peppa was brave and took it! She drank it all！"'},
                {"child":'"Yes!"',"parent":'"Hmm! Peppa said \'URGH! Disgusting!\'— it did NOT taste nice!"'},
                {"child":'不说话',"parent":'假装喝难喝的东西，皱眉，"Urgh！ Disgusting！ Was the medicine nice?"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If a friend came to visit you when you were sick, what would you want them to bring?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说食物/玩具',"parent":'"A [item]！ Perfect！ That\'s just what a sick person needs！"'},
                {"child":'说书/游戏',"parent":'"Entertainment! Great idea! Being sick is boring..."'},
                {"child":'不说话',"parent":'"Me — I\'d want someone to sit with me and tell me funny stories!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever been sick and had someone take care of you?"'],
            "rows":[
                {"child":'说经历',"parent":'"Who took care of you？ Was there medicine？ Did it taste disgusting?"'},
                {"child":'摇头',"parent":'"Never been sick? Lucky you! But Peppa had Dr Brown Bear come to her house!"'},
                {"child":'笑了',"parent":'"Did the medicine taste disgusting？ Peppa said URGH!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Hello! I\'m Dr Brown Bear. How are you feeling today?"'],
            "rows":[
                {"child":'说不舒服',"parent":'"Stick out your tongue, please! AHHH... Hmm. It\'s not serious!"'},
                {"child":'做生病状',"parent":'"You have a rash! Don\'t worry — not serious. Some medicine?" 假装倒药'},
                {"child":'说中文',"parent":'家长扮病人："Doctor! I don\'t feel very well! My face has red spots!"'},
            ],
        },
        "recast":[
            {"term":'not anything serious',"explanation":'"Not anything = nothing. Not anything serious = 没有任何严重的"'},
            {"term":'clear up',"explanation":'"Clear up = 消退，变好。 The rash will clear up = 皮疹会消退"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Stick out your tongue！ Say AHHH！" — 张大嘴，伸舌头',
            '"I don\'t feel very well..." — 无力耷拉，皱眉',
            '"Take your medicine！ Brave！" — 假装喝药，竖大拇指',
            '"All better！" — 精神抖擞，竖大拇指',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Peppa 说不舒服',"L1":'L1: "Not well..."',"L2":'L2: "I don\'t feel very well！"',"L3":'L3: "Mummy, I don\'t feel very well. My face has red spots!"'},
            {"scene":'Dr Brown Bear 检查',"L1":'L1: "Not serious！"',"L2":'L2: "It\'s just a rash！"',"L3":'L3: "Stick out your tongue please... Hmm. It\'s not anything serious. Just a rash!"'},
            {"scene":'喝了难喝的药',"L1":'L1: "Disgusting！"',"L2":'L2: "The medicine tastes disgusting！"',"L3":'L3: "Urgh! Disgusting! But I\'m brave — I took it all. All better soon!"'},
        ],
        },
        "bugs":{
            "rule":'说 "disgusting" 得1分；说 "brave" 得1分；说出完整句 "I don\'t feel very well" 得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'spots → rash → doctor → medicine → disgusting → brave → better'},
            {"level":'L2 (句)',"text":"Peppa had red spots. She didn't feel well. Dr Brown Bear came. The medicine was disgusting. She was brave."},
            {"level":'L3 (完整)',"text":"Peppa had red spots all over her face and didn't feel well. Dr Brown Bear came to examine her. He said: stick out your tongue! Hmm — it's not anything serious, just a rash. The medicine tasted disgusting! But Peppa was brave and took it. Then her friends came to visit... and they all got spots too!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ious → /ɪəs/ 结尾音',
            "examples":['serious', 'curious', 'various', 'mysterious'],
            "tongue_tip":'结尾 -ious 轻读，快速带过。"Is it serious？ It\'s mysterious！"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP26 Snow（下雪了）——" 故意停顿制造悬念',
        "next_a":'EP26 Snow',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"I don't feel very well.","zh":'我感觉不太好',"usage":'孩子装病时用，认真处理'},
        {"sentence":"It's not anything serious.","zh":'不是什么严重的',"usage":'安抚孩子轻微伤痛'},
        {"sentence":'You are a brave little one.',"zh":'你是个勇敢的小家伙',"usage":'孩子忍住痛时夸'},
        {"sentence":'Disgusting！',"zh":'令人恶心的！',"usage":'每次喝苦药时的仪式感发泄词'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 26 · Snow 下雪了
# ═══════════════════════════════════════════════════════════════════════════════
EP26 = _ep(
    num=26, title_en='Snow', title_zh='下雪了', color='blue',
    synopsis='今天下雪了！Peppa 和 George 穿上帽子围巾手套出门玩雪。他们踩脚印、打雪仗、堆雪人，Daddy 还加入进来。最后大家都玩得很开心！',
    vocab=[        {"word":'snow',"phonetic":'snəʊ',"pos":'n./v.',"zh":'雪/下雪',"action":'张开手指，假装雪花落在手上'},        {"word":'snowball',"phonetic":'ˈsnəʊbɔːl',"pos":'n.',"zh":'雪球',"action":'双手搓圆，"A snowball！"'},        {"word":'snowman',"phonetic":'ˈsnəʊmæn',"pos":'n.',"zh":'雪人',"action":'双手从下到上描绘雪人轮廓'},        {"word":'scarf',"phonetic":'skɑːf',"pos":'n.',"zh":'围巾',"action":'假装围围巾，"Wrap up warm！"'},        {"word":'gloves',"phonetic":'ɡlʌvz',"pos":'n.',"zh":'手套',"action":'假装戴手套，一根一根套上'},        {"word":'footprint',"phonetic":'ˈfʊtprɪnt',"pos":'n.',"zh":'脚印',"action":'踩地，回头看，"Footprints！ We made them！"'},        {"word":'wrap up',"phonetic":'ræp ʌp',"pos":'v.ph.',"zh":'穿暖和',"action":'做穿很多衣服的动作，"Wrap up warm!"'},        {"word":'cold',"phonetic":'kəʊld',"pos":'adj.',"zh":'冷',"action":'抱紧自己，抖动，"Brrrr！ So cold！"'},    ],
    patterns=[        {"pattern":"It's very cold outside, so you must wrap up warm.","zh":'外面很冷，所以你必须穿暖和',"example":"It's raining outside, so you must wear your boots."},        {"pattern":"Don't forget your hat and scarf and gloves.","zh":'别忘了帽子围巾和手套',"example":"Don't forget to take your umbrella!"},        {"pattern":'Peppa and George love making footprints in the snow.',"zh":'Peppa 和 George 爱在雪地踩脚印',"example":'We love jumping in muddy puddles!'},        {"pattern":"Let's build a snowman.","zh":'我们来堆雪人吧',"example":"Let's build something in the snow!"},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第25集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'❄️',"bg":'blue',"trigger":'看到雪景，兴奋出门',"action":'张开双臂，"Snow！ It\'s snowing！ We love snow！"'},
            {"emoji":'🤍',"bg":'white',"trigger":'打雪仗',"action":'假装搓雪球，投掷，"Snowball！"'},
            {"emoji":'⛄',"bg":'grey',"trigger":'堆雪人',"action":'从下到上描绘雪人，"Head！ Arms！ Snowman！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What did Peppa and George have to wear before going outside in the snow?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说 hat/scarf/gloves',"parent":'"YES！ Hat and scarf and gloves! It\'s very cold — must wrap up warm！"'},
                {"child":'说 boots',"parent":'"Boots too！ And hat and scarf and gloves! Lots of warm clothes！"'},
                {"child":'不说话',"parent":'假装穿很多衣服，"Hat... scarf... gloves... boots... NOW ready for snow！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What did they build in the snow?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Snowman!"',"parent":'"YES！ A snowman！ First they made the body — big round ball！ Then the head！"'},
                {"child":'说雪球',"parent":'"They made snowballs too! And threw them! But what did they BUILD?"'},
                {"child":'不说话',"parent":'从下到上描绘雪人，"Big... bigger... round... head..."'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If it snowed tomorrow, what is the FIRST thing you\'d want to do?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说打雪仗',"parent":'"Snowball fight！ Like Peppa and George！ Me vs you！"'},
                {"child":'说堆雪人',"parent":'"Build a snowman！ What would you give it for a nose？ A carrot！"'},
                {"child":'不说话',"parent":'"Me — I\'d make a snowball and throw it at Daddy Pig！ What about you？"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Has it ever snowed where you live? What was it like?"'],
            "rows":[
                {"child":'说下过雪',"parent":'"Did you go outside? Did you touch the snow? Was it cold?"'},
                {"child":'说没有下过',"parent":'"You\'ve never seen snow？ Imagine — everything white! Like a blanket!"'},
                {"child":'说喜欢雪',"parent":'"Snow is magical! Peppa and George LOVE snow！"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"It\'s snowing！ Quick！ What do we need before going outside?"'],
            "rows":[
                {"child":'说衣物',"parent":'"Hat! Scarf! Gloves! Let\'s wrap up warm! Ready？"'},
                {"child":'假装穿衣服',"parent":'"Hat on... scarf... gloves... OK ready! Let\'s go and make a snowman!"'},
                {"child":'说中文',"parent":'家长扮 Mummy："It\'s very cold! You must wrap up warm！"'},
            ],
        },
        "recast":[
            {"term":'wrap up warm',"explanation":'"Wrap up = 包裹。 Wrap up warm = 把自己裹得暖暖的"'},
            {"term":'footprints',"explanation":'"Footprint = foot（脚）+ print（印记）= 脚印！"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Wrap up warm！ Hat on！" — 假装穿很多衣服',
            '"Brrrr！ It\'s so cold！" — 抱紧自己，发抖',
            '"Make a snowball！ Throw！" — 搓球，投掷',
            '"Build a snowman！" — 从下到上描绘',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Peppa 很兴奋要出去玩雪',"L1":'L1: "Snow！"',"L2":'L2: "Can we go and play in the snow？"',"L3":'L3: "Mummy！ It\'s snowing！ Can we go outside and play？"'},
            {"scene":'Mummy 说要穿暖',"L1":'L1: "Cold！ Wrap up！"',"L2":'L2: "It\'s very cold — wrap up warm！"',"L3":'L3: "It\'s very cold outside. You must wrap up warm — hat, scarf, and gloves!"'},
            {"scene":'堆雪人',"L1":'L1: "Snowman！"',"L2":'L2: "Let\'s build a snowman！"',"L3":'L3: "First the body — big ball! Now the head! We\'re making a snowman!"'},
        ],
        },
        "bugs":{
            "rule":'说 "snowball" 得1分；说 "wrap up warm" 得2分；说 "footprints" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'snow → cold → snowball → snowman → scarf → gloves → footprints'},
            {"level":'L2 (句)',"text":'It snowed. Peppa and George wrapped up warm. They made snowballs and a snowman.'},
            {"level":'L3 (完整)',"text":"It was snowing! Peppa and George were very excited. Mummy said: it's very cold, wrap up warm! Hat, scarf, and gloves. They went outside and made footprints in the snow. Then they had a snowball fight! Then they built a snowman together. Even Daddy joined in! Snow is wonderful!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ow → /əʊ/ 长音（单词结尾）',
            "examples":['snow', 'know', 'show', 'blow', 'low'],
            "tongue_tip":'结尾 ow 发 /əʊ/，就像 "哦" 拖长音。"Snow, snow, blow in the wind!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP27 Windy Castle（风中的城堡）——" 故意停顿制造悬念',
        "next_a":'EP27 Windy Castle',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"It's very cold outside — wrap up warm!","zh":'外面很冷，穿暖和！',"usage":'每次冬天出门前'},
        {"sentence":"Don't forget your hat and scarf and gloves.","zh":'别忘了帽子围巾手套',"usage":'出门检查清单'},
        {"sentence":"Let's build a snowman!","zh":'我们来堆雪人！',"usage":'遇到雪时的第一句'},
        {"sentence":'Brrrr！ So cold！',"zh":'冷死了！',"usage":'冷天的夸张情绪表达'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 27 · Windy Castle 风中的城堡
# ═══════════════════════════════════════════════════════════════════════════════
EP27 = _ep(
    num=27, title_en='Windy Castle', title_zh='风中的城堡', color='purple',
    synopsis='全家去参观一座古老的城堡。风很大，所有东西都被吹走了！帽子、气球，甚至野餐也被风吹乱了。Daddy Pig 说他很了解历史，但大风让他的表演变得很搞笑。',
    vocab=[        {"word":'castle',"phonetic":'ˈkɑːsl',"pos":'n.',"zh":'城堡',"action":'双手向上描绘城堡的尖塔，"The castle！"'},        {"word":'windy',"phonetic":'ˈwɪndi',"pos":'adj.',"zh":'有风的',"action":'双臂伸开，做被风吹的动作'},        {"word":'knight',"phonetic":'naɪt',"pos":'n.',"zh":'骑士',"action":'假装穿盔甲，"A knight！ Brave and strong！"'},        {"word":'ancient',"phonetic":'ˈeɪnʃənt',"pos":'adj.',"zh":'古老的',"action":'手摸想象的老石头，"Ancient. Very very old."'},        {"word":'history',"phonetic":'ˈhɪstri',"pos":'n.',"zh":'历史',"action":'做出时间轴手势，"A long time ago..."'},        {"word":'expert',"phonetic":'ˈekspɜːt',"pos":'n.',"zh":'专家',"action":'指自己，"I\'m an expert on castles！"'},        {"word":'blow away',"phonetic":'bləʊ əˈweɪ',"pos":'v.ph.',"zh":'被风吹走',"action":'东西从手中飞走，"Blown away！ Gone!"'},        {"word":'magnificent',"phonetic":'mæɡˈnɪfɪsnt',"pos":'adj.',"zh":'壮丽的',"action":'张开双臂，"Magnificent！ So beautiful！"'},    ],
    patterns=[        {"pattern":'This castle is very old.',"zh":'这座城堡非常古老',"example":'This building is very old — ancient!'},        {"pattern":'I know a lot about castles.',"zh":'我对城堡很了解',"example":'I know a lot about dinosaurs!'},        {"pattern":"It's very windy today.","zh":'今天风很大',"example":"It's very rainy. It's very sunny."},        {"pattern":'Everything is being blown away!',"zh":'所有东西都被风吹走了！',"example":'The wind is blowing everything away!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第26集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🏰',"bg":'purple',"trigger":'到达古老城堡',"action":'张开双臂，"A castle！ Magnificent！"'},
            {"emoji":'💨',"bg":'blue',"trigger":'大风吹走了东西',"action":'东西从手飞走，"WHOOSH！ Blown away！"'},
            {"emoji":'⚔️',"bg":'grey',"trigger":'讲骑士历史',"action":'假装拔剑，"Charge！ Like a knight！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What happened to the picnic in the windy castle?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说被风吹走',"parent":'"YES！ The wind blew everything away！ Sandwiches, cups — all blown away！"'},
                {"child":'说吃了',"parent":'"Actually the wind came and... WHOOSH！ Blown away！"'},
                {"child":'不说话',"parent":'假装东西从手中飞走，"WHOOSH！ Gone！ The WIND!"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Was Daddy Pig really an expert on castles?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'笑着说不是',"parent":'"Haha！ He SAID he was an expert... but the wind made everything go wrong!"'},
                {"child":'"Yes!"',"parent":'"He said he was! But castles don\'t usually have that much trouble with wind..."'},
                {"child":'不说话',"parent":'假装 Daddy 专家姿态，然后被风吹乱，"I\'m an expert..." WHOOSH！'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"Would you like to live in a castle? Why or why not?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说想住',"parent":'"A castle！ So many rooms！ And knights on guard! But... very windy？"'},
                {"child":'说不想',"parent":'"Too cold？ Too old？ Or too windy?！ Like today\'s castle！"'},
                {"child":'不说话',"parent":'"I\'d like a castle with a dragon! And... not too windy. What about you？"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever been somewhere really windy?"'],
            "rows":[
                {"child":'说经历',"parent":'"Like the castle！ Did things blow away？ Your hat？ Your umbrella？"'},
                {"child":'摇头',"parent":'"Never? One day the wind will be SO strong..." 做被吹走的样子'},
                {"child":'笑了',"parent":'"WHOOSH！ What would you do if your hat blew away?"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Welcome to the ancient castle！ I am the guide — I\'m an expert！"'],
            "rows":[
                {"child":'问问题',"parent":'"When was the castle built？ Who lived here？ Were there knights？"'},
                {"child":'说 "knight!"',"parent":'"YES！ Knights lived here! In armour! With swords!" 假装拔剑'},
                {"child":'说中文',"parent":'家长扮向导："This castle is very old — ancient! And very windy!"'},
            ],
        },
        "recast":[
            {"term":'blown away',"explanation":'"Blow + away = 吹走。 Everything was blown away by the wind！"'},
            {"term":'magnificent',"explanation":'"Magnificent = 壮丽的、宏伟的。 That\'s a magnificent castle！"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Look at the castle！ Magnificent！" — 张开双臂，仰望',
            '"It\'s so windy！ Hold on！" — 假装被吹歪，抓住想象的东西',
            '"WHOOSH！ Blown away！" — 手从头顶飞过去',
            '"Like a knight！ Charge！" — 假装骑马，向前冲',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'到达城堡',"L1":'L1: "Castle！"',"L2":'L2: "What a magnificent castle！"',"L3":'L3: "This castle is very old — ancient! Knights used to live here long ago!"'},
            {"scene":'大风来了',"L1":'L1: "Wind！ Gone！"',"L2":'L2: "Everything is blown away！"',"L3":'L3: "Oh no！ The wind took our picnic! Everything is being blown away！"'},
            {"scene":'Daddy 自称专家',"L1":'L1: "Expert！"',"L2":'L2: "I\'m an expert on castles！"',"L3":'L3: "I know a lot about castles. This one is very old — perhaps the most ancient in the country!"'},
        ],
        },
        "bugs":{
            "rule":'说 "castle" 得1分；说 "blown away" 得2分；说 "magnificent" 得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'castle → windy → ancient → knight → blown away → magnificent'},
            {"level":'L2 (句)',"text":'The family visited an ancient castle. Daddy said he was an expert. It was very windy. Everything blew away.'},
            {"level":'L3 (完整)',"text":'The family visited a magnificent ancient castle! Daddy Pig said he was an expert on castles. But it was SO windy! Hats blew off. The picnic blew away. Things went flying everywhere! WHOOSH！ Maybe castles are too windy for picnics... but still magnificent!'},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 igh → /aɪ/ 长音',
            "examples":['knight', 'night', 'right', 'light', 'flight'],
            "tongue_tip":'igh 的 gh 不发音，只有 /aɪ/。"A knight at night — right?"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP28 My Cousin Chloé（表姐 Chloé）——" 故意停顿制造悬念',
        "next_a":'EP28 My Cousin Chloé',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"I'm an expert on castles.","zh":'我对城堡很了解',"usage":'任何话题都可以替换，搞笑自封专家'},
        {"sentence":'Everything is being blown away!',"zh":'所有东西都被风吹走了',"usage":'大风天气的感叹句'},
        {"sentence":'This castle is very old — ancient!',"zh":'这个城堡非常古老',"usage":'参观历史景点时用'},
        {"sentence":'Magnificent!',"zh":'壮丽的！',"usage":'看到美景时的感叹词'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 28 · My Cousin Chloé 表姐 Chloé
# ═══════════════════════════════════════════════════════════════════════════════
EP28 = _ep(
    num=28, title_en='My Cousin Chloé', title_zh='表姐 Chloé', color='pink',
    synopsis='Peppa 的大表姐 Chloé 来做客！Chloé 比 Peppa 大很多，Peppa 很崇拜她。但 Chloé 觉得 Peppa 太小了，有点看不上。最后 Chloé 的大人游戏没有 Peppa 的游戏有趣，她们成了朋友。',
    vocab=[        {"word":'cousin',"phonetic":'ˈkʌzn',"pos":'n.',"zh":'表/堂兄弟姐妹',"action":'手指两人，"Cousin — from our family!"'},        {"word":'older',"phonetic":'ˈəʊldə',"pos":'adj.',"zh":'更大/更老',"action":'双手向上，表示更高，"Older — bigger — more grown up!"'},        {"word":'grown-up',"phonetic":'ɡrəʊn ʌp',"pos":'adj./n.',"zh":'大人/成年的',"action":'挺胸站直，"I\'m almost a grown-up!"'},        {"word":'embarrassed',"phonetic":'ɪmˈbærəst',"pos":'adj.',"zh":'尴尬的',"action":'捂脸，"So embarrassed！"'},        {"word":'teenager',"phonetic":'ˈtiːneɪdʒə',"pos":'n.',"zh":'青少年',"action":'用手比出介于孩子和大人之间'},        {"word":'babysit',"phonetic":'ˈbeɪbɪsɪt',"pos":'v.',"zh":'照看孩子',"action":'假装照顾小孩，"I\'m babysitting！"'},        {"word":'boring',"phonetic":'ˈbɔːrɪŋ',"pos":'adj.',"zh":'无聊的',"action":'打哈欠，"So boring... nothing to do..."'},        {"word":'admit',"phonetic":'ədˈmɪt',"pos":'v.',"zh":'承认',"action":'低头，"OK, I admit it — it WAS fun!"'},    ],
    patterns=[        {"pattern":'Chloé is older than Peppa.',"zh":'Chloé 比 Peppa 大',"example":'My cousin is older than me.'},        {"pattern":"I'm almost a grown-up.","zh":'我快是大人了',"example":"She's almost a teenager!"},        {"pattern":'This game is for babies!',"zh":'这个游戏是小宝宝玩的！',"example":"That's for little kids!"},        {"pattern":'Admit it — that was fun!',"zh":'承认吧——那很好玩！',"example":'Come on, admit it — you enjoyed it!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第27集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'👧',"bg":'pink',"trigger":'Chloé 到达，Peppa 很崇拜',"action":'眼睛发光，"Chloé！ She\'s so grown-up！"'},
            {"emoji":'🙄',"bg":'orange',"trigger":'Chloé 觉得 Peppa 的游戏是婴儿玩的',"action":'做出不屑的表情，"That\'s for babies!"'},
            {"emoji":'😄',"bg":'green',"trigger":'Chloé 也加入了游戏，很开心',"action":'做出开心玩游戏的样子'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Was Chloé nice to Peppa at first?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Not really!"',"parent":'"No！ She thought Peppa\'s games were for babies！ But..."'},
                {"child":'"Yes!"',"parent":'"Chloé said Peppa\'s games were \'for babies\'... was that very nice?"'},
                {"child":'不说话',"parent":'做出不屑表情，"That\'s for babies！ Was that kind？"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"In the end, did Chloé enjoy playing with Peppa?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Yes!"',"parent":'"YES！ She had so much fun! She had to admit it — the game WAS fun！"'},
                {"child":'说不知道',"parent":'"At the end... she was laughing and playing！ She loved it！"'},
                {"child":'不说话',"parent":'做出开心玩游戏的样子，"She was laughing！ Having fun！ Was she enjoying it？"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"Do you have any older cousins or friends? What\'s it like?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说有',"parent":'"Like Chloé！ Do they think they\'re grown-up? Do they let you play with them?"'},
                {"child":'说没有',"parent":'"No cousins？ Imagine having a big cousin like Chloé visit!"'},
                {"child":'不说话',"parent":'"I\'d love to have a cousin who visits！ Would you?"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Has anyone ever said your games were \'for babies\'?"'],
            "rows":[
                {"child":'说有',"parent":'"How did that feel？ Like Peppa！ But Chloé\'s \'grown-up games\' weren\'t more fun after all!"'},
                {"child":'摇头',"parent":'"Good！ ALL games are good! Even jumping in muddy puddles!"'},
                {"child":'笑了',"parent":'"The best games are the ones that make you laugh!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Hi！ I\'m Chloé. I\'m almost a teenager. These games are for babies."'],
            "rows":[
                {"child":'说一个游戏',"parent":'"For babies？ Let me try... Oh! Actually that IS fun! I admit it!"'},
                {"child":'邀请 Chloé 玩',"parent":'"Maybe I\'ll try just ONCE... OK fine, it\'s actually fun!"'},
                {"child":'说中文',"parent":'家长扮 Peppa："Chloé！ Come and play！ It\'s not for babies — try it!"'},
            ],
        },
        "recast":[
            {"term":'almost a grown-up',"explanation":'"Almost = 几乎，快要了。 Almost a teenager = 快要是青少年了"'},
            {"term":'admit it',"explanation":'"Admit = 承认。 Admit it = 好吧承认吧。 Come on, admit it!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"I\'m almost a grown-up！" — 挺胸，傲娇站立',
            '"That\'s for babies！" — 做不屑眼神，摆手',
            '"Admit it！ It was fun！" — 指对方，笑',
            '"We\'re cousins！" — 指两人，做联结手势',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Chloé 到达',"L1":'L1: "Chloé！"',"L2":'L2: "My cousin Chloé is here！"',"L3":'L3: "Chloé！ She\'s so grown-up! I want to be just like her!"'},
            {"scene":'Chloé 不想玩 Peppa 的游戏',"L1":'L1: "Babies！"',"L2":'L2: "This game is for babies！"',"L3":'L3: "I\'m almost a teenager. These games are for babies. I\'d rather do grown-up things."'},
            {"scene":'Chloé 最后也很开心',"L1":'L1: "Fun！"',"L2":'L2: "Actually, that WAS fun！"',"L3":'L3: "OK, I admit it — that was actually really fun! Maybe not just for babies after all!"'},
        ],
        },
        "bugs":{
            "rule":'说 "admit" 得2分；说 "grown-up" 得1分；说 "cousin" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'cousin → older → grown-up → babies → fun → admit'},
            {"level":'L2 (句)',"text":"Peppa's big cousin Chloé visited. She thought she was too grown-up. But she ended up having fun."},
            {"level":'L3 (完整)',"text":"Peppa's cousin Chloé came to visit. Chloé was older and almost a teenager. She thought Peppa's games were for babies! But Peppa's games were actually really fun. In the end, Chloé had to admit it — she had a great time playing with Peppa!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ou → /ʌ/ 音（cousin, country）',
            "examples":['cousin', 'young', 'touch', 'trouble', 'country'],
            "tongue_tip":'ou 在某些词中发 /ʌ/，不是 /aʊ/。"My cousin is young and fun!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP29 Pancakes（薄煎饼）——" 故意停顿制造悬念',
        "next_a":'EP29 Pancakes',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"I'm almost a grown-up.","zh":'我快是大人了',"usage":'孩子觉得自己很厉害时引用'},
        {"sentence":'Admit it — that was fun!',"zh":'承认吧——很好玩！',"usage":'孩子假装不感兴趣但其实很开心时'},
        {"sentence":'My cousin Chloé is older than me.',"zh":'表姐比我大',"usage":'介绍亲戚关系的模板'},
        {"sentence":'This game is for babies!',"zh":'这是婴儿玩的游戏',"usage":'孩子用来戏弄大人的句子'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 29 · Pancakes 薄煎饼
# ═══════════════════════════════════════════════════════════════════════════════
EP29 = _ep(
    num=29, title_en='Pancakes', title_zh='薄煎饼', color='yellow',
    synopsis='今天全家做薄煎饼！Daddy Pig 展示了如何抛薄煎饼，但抛得太高，煎饼粘在了天花板上！最后大家还是吃到了美味的薄煎饼，加了很多果酱。',
    vocab=[        {"word":'pancake',"phonetic":'ˈpænkeɪk',"pos":'n.',"zh":'薄煎饼',"action":'双手做扁圆形，"A pancake！ Round and flat！"'},        {"word":'toss',"phonetic":'tɒs',"pos":'v.',"zh":'抛',"action":'手做抛东西的动作，"Toss the pancake！"'},        {"word":'flip',"phonetic":'flɪp',"pos":'v.',"zh":'翻转',"action":'手做翻转动作，"Flip！ The other side！"'},        {"word":'ceiling',"phonetic":'ˈsiːlɪŋ',"pos":'n.',"zh":'天花板',"action":'仰头，指向上方，"The ceiling — up there！"'},        {"word":'stuck',"phonetic":'stʌk',"pos":'adj.',"zh":'卡住、粘住',"action":'做出拉不下来的动作，"Stuck！ Can\'t move!"'},        {"word":'jam',"phonetic":'dʒæm',"pos":'n.',"zh":'果酱',"action":'假装涂果酱，"Strawberry jam！ Yummy！"'},        {"word":'golden',"phonetic":'ˈɡəʊldən',"pos":'adj.',"zh":'金黄色的',"action":'指想象的煎饼，"Golden！ Perfect colour！"'},        {"word":'recipe',"phonetic":'ˈresɪpi',"pos":'n.',"zh":'食谱',"action":'假装翻书，"What\'s the recipe？"'},    ],
    patterns=[        {"pattern":'Shall we make pancakes?',"zh":'我们来做薄煎饼吗？',"example":'Shall we make cookies? Shall we bake?'},        {"pattern":'You have to toss the pancake into the air.',"zh":'你得把煎饼抛到空中',"example":'Toss it up high and catch it!'},        {"pattern":"It's stuck to the ceiling!","zh":'它粘在天花板上了！',"example":'The ball is stuck on the roof!'},        {"pattern":'Perfect! Golden and delicious!',"zh":'完美！金黄色，好吃极了！',"example":'Golden brown and ready to eat!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第28集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🥞',"bg":'yellow',"trigger":'Daddy 展示抛煎饼',"action":'做出抛东西动作，越来越高'},
            {"emoji":'😱',"bg":'orange',"trigger":'煎饼粘在天花板上',"action":'仰头，"It\'s on the CEILING！"'},
            {"emoji":'🍓',"bg":'red',"trigger":'吃薄煎饼加果酱',"action":'假装涂果酱，大口吃，"Mmm！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What happened when Daddy tossed the pancake?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说粘在天花板',"parent":'"YES！ It went too HIGH and got stuck on the CEILING！ They needed a chair to get it down!"'},
                {"child":'说不知道',"parent":'"He tossed it UP and UP and UP... and it went..." 指向天花板'},
                {"child":'不说话',"parent":'做抛煎饼动作，越来越高，手停在头顶，仰头'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What did they put on the pancakes?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说 jam',"parent":'"Strawberry jam！ Red and sweet！ Mmmm！"'},
                {"child":'说其他',"parent":'"Jam！ Strawberry jam！ Peppa loves strawberry jam on her pancakes！"'},
                {"child":'不说话',"parent":'假装涂果酱，"Mmm！ What\'s this red thing？ JAM！"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you could put ANYTHING on a pancake, what would YOU choose?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说食物',"parent":'"[Food] on a pancake！ That sounds amazing! Or disgusting! Maybe both!"'},
                {"child":'说巧克力',"parent":'"CHOCOLATE！ Good choice！ Chocolate pancakes！"'},
                {"child":'不说话',"parent":'"I\'d put ice cream! And sprinkles! And... MORE ice cream!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever tried to flip something in a pan? Or watched someone cook?"'],
            "rows":[
                {"child":'说见过/试过',"parent":'"Did it work？ Or did it go on the ceiling？ Like Daddy Pig!"'},
                {"child":'摇头',"parent":'"Next time — try flipping a pancake! It\'s hard but SO satisfying!"'},
                {"child":'笑了',"parent":'"The pancake on the CEILING！ Classic Daddy Pig！"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Good morning！ Today we\'re making pancakes！ Can you be my helper?"'],
            "rows":[
                {"child":'同意',"parent":'"Great！ First — stir the batter... Now — ready to flip？ FLIP！"'},
                {"child":'假装搅拌/翻',"parent":'"Flip! Go！ AHHH it\'s on the ceiling！ How do we get it down？"'},
                {"child":'说中文',"parent":'家长扮 Daddy："The secret is to toss it high! Watch me!" 做抛动作'},
            ],
        },
        "recast":[
            {"term":'toss',"explanation":'"Toss = 把东西轻轻抛入空中。 Toss the pancake!"'},
            {"term":'stuck',"explanation":'"Stuck = 卡住了，动弹不得。 It\'s stuck on the ceiling!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Mix the batter！" — 假装搅拌',
            '"Flip the pancake！" — 做翻转动作',
            '"It\'s on the ceiling！" — 仰头，惊讶',
            '"Mmm！ Golden and delicious！" — 闭眼享受',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Daddy 演示抛煎饼',"L1":'L1: "Toss！"',"L2":'L2: "You have to toss the pancake！"',"L3":'L3: "Watch me! You toss the pancake into the air like this! Ready？ TOSS！"'},
            {"scene":'煎饼粘在天花板',"L1":'L1: "Ceiling！ Stuck！"',"L2":'L2: "The pancake is stuck to the ceiling！"',"L3":'L3: "Oh no! It went too high! It\'s stuck on the ceiling! We need a chair!"'},
            {"scene":'吃煎饼加果酱',"L1":'L1: "Jam！ Yummy！"',"L2":'L2: "Strawberry jam on my pancake！"',"L3":'L3: "Golden and perfect! With strawberry jam on top! This is the best pancake ever!"'},
        ],
        },
        "bugs":{
            "rule":'说 "toss" 或 "flip" 得1分；说 "ceiling" 得1分；说 "stuck" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'pancake → toss → flip → ceiling → stuck → jam → golden'},
            {"level":'L2 (句)',"text":'The family made pancakes. Daddy tossed one too high. It got stuck on the ceiling. They ate the others with jam.'},
            {"level":'L3 (完整)',"text":'The family decided to make pancakes! Daddy Pig said the secret is to toss them. He tossed one UP — too high! It got stuck on the CEILING! They needed a chair to get it down. But the other pancakes were golden and delicious with strawberry jam. Worth the mess!'},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ake → /eɪk/ 长音（a-e 规则）',
            "examples":['pancake', 'make', 'cake', 'lake', 'wake'],
            "tongue_tip":'a 后跟辅音+e，a 发长音 /eɪ/。"Make a cake by the lake!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP30 Babysitting（临时看孩子）——" 故意停顿制造悬念',
        "next_a":'EP30 Babysitting',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Shall we make pancakes?',"zh":'我们来做薄煎饼吗？',"usage":'周末早餐的魔法开场白'},
        {"sentence":'Toss it! Flip it!',"zh":'抛起来！翻转！',"usage":'做任何翻转动作时'},
        {"sentence":"It's stuck on the ceiling!","zh":'粘在天花板上了！',"usage":'任何东西到了够不着的地方'},
        {"sentence":'Golden and delicious!',"zh":'金黄色，好吃极了！',"usage":'夸好吃食物的句子'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 30 · Babysitting 临时看孩子
# ═══════════════════════════════════════════════════════════════════════════════
EP30 = _ep(
    num=30, title_en='Babysitting', title_zh='临时看孩子', color='orange',
    synopsis='Granny 和 Grandpa Pig 来给 Peppa 和 George 看孩子，因为 Mummy 和 Daddy 要出去。Granny 和 Grandpa 答应孩子们的要求，一起玩游戏、讲故事，累得在沙发上睡着了。',
    vocab=[        {"word":'babysitter',"phonetic":'ˈbeɪbɪsɪtə',"pos":'n.',"zh":'临时看孩子的人',"action":'假装照顾小孩，"The babysitter!"'},        {"word":'behave',"phonetic":'bɪˈheɪv',"pos":'v.',"zh":'行为举止，守规矩',"action":'坐直，双手放膝盖，"Behave！ Be good!"'},        {"word":'promise',"phonetic":'ˈprɒmɪs',"pos":'v./n.',"zh":'答应/承诺',"action":'拉小拇指，"I promise！"'},        {"word":'exhausted',"phonetic":'ɪɡˈzɔːstɪd',"pos":'adj.',"zh":'精疲力竭',"action":'耷拉着，喘气，"Exhausted！ So tired！"'},        {"word":'trick',"phonetic":'trɪk',"pos":'n.',"zh":'把戏，花招',"action":'做出偷偷摸摸的样子，"A trick！"'},        {"word":'asleep',"phonetic":'əˈsliːp',"pos":'adj.',"zh":'睡着的',"action":'合上眼，发出呼噜声，"Asleep！ Zzzzz"'},        {"word":'adventure',"phonetic":'ədˈventʃə',"pos":'n.',"zh":'冒险',"action":'举拳，"Adventure！ Exciting！"'},        {"word":'manage',"phonetic":'ˈmænɪdʒ',"pos":'v.',"zh":'应付，管理',"action":'耸肩，"I can manage！"'},    ],
    patterns=[        {"pattern":"We'll be good, Granny, we promise.","zh":'我们会听话的，Granny，我们保证',"example":"I promise I'll be good! Really!"},        {"pattern":'Granny and Grandpa are babysitting.',"zh":'Granny 和 Grandpa 在临时看孩子',"example":'Who is looking after you tonight?'},        {"pattern":"They're exhausted!","zh":'他们精疲力竭了！',"example":'Granny and Grandpa are so tired!'},        {"pattern":'Can we have one more story?',"zh":'我们可以再听一个故事吗？',"example":'Can we stay up just a little longer?'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第29集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'👴👵',"bg":'orange',"trigger":'Granny Grandpa 到来看孩子',"action":'做开心欢迎的手势'},
            {"emoji":'📖',"bg":'blue',"trigger":'讲了一个又一个故事',"action":'假装翻书，"One more story？ OK..."'},
            {"emoji":'😴',"bg":'grey',"trigger":'Granny Grandpa 在沙发上睡着了',"action":'合上眼，发出呼噜声'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Who was babysitting Peppa and George?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说 Granny/Grandpa',"parent":'"YES！ Granny and Grandpa Pig！ They said \'we can manage!\'"'},
                {"child":'说 Daddy',"parent":'"Mummy and Daddy went OUT! Granny and Grandpa came to look after them!"'},
                {"child":'不说话',"parent":'"Who was looking after Peppa？ It starts with Granny..."'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What happened to Granny and Grandpa at the end?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说睡着了',"parent":'"YES！ They fell asleep on the sofa！ All that playing and story-telling was exhausting!"'},
                {"child":'说 not sure',"parent":'"They told so many stories... played so many games... and then... Zzzzz!"'},
                {"child":'不说话',"parent":'做呼噜声，"Zzzzz！ What happened to Granny？ She\'s...?"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If Granny or Grandpa looked after you, what would you ask them to do?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说活动',"parent":'"[Activity]！ Granny and Grandpa would probably say yes to everything!"'},
                {"child":'说讲故事',"parent":'"Stories！ One story... then another... and another... until they fall asleep!"'},
                {"child":'不说话',"parent":'"Me — I\'d ask for stories AND cookies AND games AND... one more story!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have Granny or Grandpa ever looked after you? What did you do?"'],
            "rows":[
                {"child":'说经历',"parent":'"Did they say yes to everything？ Did they get tired?"'},
                {"child":'摇头',"parent":'"Never？ Imagine Granny looking after you — she might say yes to extra stories!"'},
                {"child":'笑了',"parent":'"Did they fall asleep？ Like in the show？"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"I\'m babysitting you tonight！ I\'m Granny Pig！ What shall we do？"'],
            "rows":[
                {"child":'说游戏/故事',"parent":'"One game it is！ And then... one story? And then sleep？"'},
                {"child":'说一个又一个',"parent":'"Another story？ And another？ Zzzz... I\'m so exhausted..." 假装睡着'},
                {"child":'说中文',"parent":'家长扮 Granny："I can manage！ Now — be good！ We\'ll have lots of fun！"'},
            ],
        },
        "recast":[
            {"term":'exhausted',"explanation":'"Exhausted = 精疲力竭. Much more tired than \'tired\'!"'},
            {"term":'babysitting',"explanation":'"Babysit = 临时照顾孩子（不是 babysit = 坐在婴儿身上！）"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Behave！ Be good！" — 坐直，装正经',
            '"Can we have one more story？" — 合十手势，期待眼神',
            '"I\'m exhausted！" — 耷拉下来，叹气',
            '"Zzzzz！ Asleep！" — 合上眼，发呼噜声',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Granny Grandpa 来看孩子',"L1":'L1: "Hello！"',"L2":'L2: "Granny and Grandpa are babysitting！"',"L3":'L3: "Hello, my little ones! Mummy and Daddy are going out. We\'ll look after you tonight!"'},
            {"scene":'孩子一直要更多故事',"L1":'L1: "One more！"',"L2":'L2: "Can we have one more story？"',"L3":'L3: "Please, Granny! Just one more story! We promise we\'ll sleep after this one!"'},
            {"scene":'Granny Grandpa 睡着了',"L1":'L1: "Asleep！ Zzz！"',"L2":'L2: "Granny and Grandpa are asleep！"',"L3":'L3: "They were so exhausted from all that playing! Now Granny and Grandpa are fast asleep on the sofa!"'},
        ],
        },
        "bugs":{
            "rule":'说 "exhausted" 得2分；说 "promise" 得1分；说 "one more story" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'babysitter → promise → story → exhausted → asleep'},
            {"level":'L2 (句)',"text":'Granny and Grandpa looked after Peppa and George. They promised to be good. They told lots of stories. Granny and Grandpa fell asleep.'},
            {"level":'L3 (完整)',"text":'Mummy and Daddy went out, and Granny and Grandpa came to babysit. The children promised to be good. But then: one game... one more story... one more game... one MORE story! By the end, Granny and Grandpa were totally exhausted and fell fast asleep on the sofa!'},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ere/eer → /ɪə/ 双元音',
            "examples":['here', 'deer', 'cheer', 'steer', 'career'],
            "tongue_tip":'从 /ɪ/ 滑向 /ə/，持续滑动。"Here, dear! Come here!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP31 Ballet Lesson（芭蕾课）——" 故意停顿制造悬念',
        "next_a":'EP31 Ballet Lesson',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"We'll be good, we promise!","zh":'我们会听话的，我们保证',"usage":'孩子想做某事时的经典承诺'},
        {"sentence":'Can we have one more story?',"zh":'可以再讲一个故事吗？',"usage":'睡前万能句'},
        {"sentence":"They're exhausted!","zh":'他们精疲力竭了！',"usage":'大人累了时的形容词'},
        {"sentence":'I can manage!',"zh":'我能应付！',"usage":'自信面对挑战时'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 31 · Ballet Lesson 芭蕾课
# ═══════════════════════════════════════════════════════════════════════════════
EP31 = _ep(
    num=31, title_en='Ballet Lesson', title_zh='芭蕾课', color='pink',
    synopsis='Peppa 去上芭蕾课，George 也想去，Madame Gazelle 欢迎所有人。George 在芭蕾课上转圈转得最好，连老师都夸他！',
    vocab=[        {"word":'ballet',"phonetic":'ˈbæleɪ',"pos":'n.',"zh":'芭蕾',"action":'踮起脚尖，转圈，"Ballet！"'},        {"word":'tutu',"phonetic":'ˈtuːtuː',"pos":'n.',"zh":'芭蕾裙',"action":'做出蓬蓬裙的形状，"A tutu！ Pretty!"'},        {"word":'graceful',"phonetic":'ˈɡreɪsfl',"pos":'adj.',"zh":'优雅的',"action":'缓缓挥动双臂，"Graceful. Like a swan!"'},        {"word":'balance',"phonetic":'ˈbæləns',"pos":'v./n.',"zh":'保持平衡',"action":'单脚站立，双臂展开，"Balance！"'},        {"word":'spin',"phonetic":'spɪn',"pos":'v.',"zh":'旋转',"action":'原地转圈，"Spin! Round and round!"'},        {"word":'rehearse',"phonetic":'rɪˈhɜːs',"pos":'v.',"zh":'排练',"action":'认真做动作，"Rehearse — practice before the show!"'},        {"word":'positions',"phonetic":'pəˈzɪʃnz',"pos":'n.',"zh":'芭蕾姿势',"action":'做出不同的芭蕾姿势'},        {"word":'twirl',"phonetic":'twɜːl',"pos":'v.',"zh":'旋转跳舞',"action":'手向上，转圈，"Twirl!"'},    ],
    patterns=[        {"pattern":'Ballet is for everyone.',"zh":'芭蕾舞是所有人的',"example":'Sport is for everyone. Music is for everyone.'},        {"pattern":'Can you stand on one leg?',"zh":'你能单脚站立吗？',"example":'Can you balance on one foot?'},        {"pattern":'George is very good at spinning.',"zh":'George 转圈转得非常好',"example":"You're very good at dancing!"},        {"pattern":'Everyone is different.',"zh":'每个人都不一样',"example":"Everyone has something they're good at."},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第30集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🩰',"bg":'pink',"trigger":'孩子们换上芭蕾鞋',"action":'踮起脚尖，"Ballet shoes on！"'},
            {"emoji":'💃',"bg":'blue',"trigger":'Madame Gazelle 教芭蕾姿势',"action":'做出芭蕾站姿，双臂优雅'},
            {"emoji":'🌀',"bg":'purple',"trigger":'George 转圈转得最好',"action":'原地快速转圈，"Spin！ So fast！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Who was best at spinning in the ballet class?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"George!"',"parent":'"YES！ George！ He spun round and round and was the BEST！ Even better than Peppa!"'},
                {"child":'说 Peppa',"parent":'"Peppa was good! But who was BEST at spinning? George kept going and going!"'},
                {"child":'不说话',"parent":'原地转圈，"Who was spinning the most？ Who was dizziest？ George！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Did ballet make George happy or sad?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Happy!"',"parent":'"VERY happy！ He got to spin and Madame Gazelle said he was BRILLIANT!"'},
                {"child":'说 sad',"parent":'"Actually George loved ballet! He was the star of the class!"'},
                {"child":'不说话',"parent":'做出开心转圈的动作，"Did George look... happy or sad?"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you had a ballet class, what would you want to learn first?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说旋转/跳跃',"parent":'"Spinning！ Like George！ Or jumping！ En pointe！"'},
                {"child":'说其他',"parent":'"Any move is great！ Ballet takes lots of practice！"'},
                {"child":'不说话',"parent":'踮起脚尖，单脚站，"Can YOU balance？ That\'s the first thing!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever danced or done any kind of performance?"'],
            "rows":[
                {"child":'说过',"parent":'"Like Peppa at ballet！ Did you wear special shoes？"'},
                {"child":'摇头',"parent":'"Never? Let\'s dance RIGHT NOW!" 开始随意跳舞'},
                {"child":'笑了',"parent":'"The best dancer isn\'t always the most graceful — sometimes the most enthusiastic!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Welcome to ballet class！ I am Madame Gazelle！ First position！"'],
            "rows":[
                {"child":'做芭蕾姿势',"parent":'"Beautiful！ Now can you spin？ Round and round!"'},
                {"child":'转圈',"parent":'"WONDERFUL！ Just like George！ You\'re a natural！"'},
                {"child":'说中文',"parent":'家长扮 Madame Gazelle："Ballet is for everyone！ First position！"'},
            ],
        },
        "recast":[
            {"term":'graceful',"explanation":'"Graceful = 优雅的，动作流畅而美丽"'},
            {"term":'balance',"explanation":'"Balance = 保持平衡。 Can you balance on one foot?"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"First position！" — 双脚外开，双手下垂',
            '"Spin！ Round and round！" — 原地转圈',
            '"Balance on one foot！" — 单脚站立，双臂展开',
            '"Graceful！ Like a swan！" — 缓缓挥动双臂',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Madame Gazelle 开始上课',"L1":'L1: "Ballet！"',"L2":'L2: "Welcome to ballet class！"',"L3":'L3: "First position, everyone! Ballet is for everyone — even George!"'},
            {"scene":'George 转圈最厉害',"L1":'L1: "Spin！"',"L2":'L2: "George is very good at spinning！"',"L3":'L3: "George can spin! Round and round and round! He\'s brilliant at ballet!"'},
            {"scene":'Madame Gazelle 表扬 George',"L1":'L1: "Well done！"',"L2":'L2: "Well done, George！"',"L3":'L3: "George, that was magnificent! You\'re a natural ballet dancer!"'},
        ],
        },
        "bugs":{
            "rule":'说 "spin" 得1分；说 "graceful" 得2分；做出单脚站立并说 "balance" 得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'ballet → spin → tutu → graceful → balance → twirl'},
            {"level":'L2 (句)',"text":'Peppa went to ballet class. George came too. George was best at spinning.'},
            {"level":'L3 (完整)',"text":"Peppa and George went to ballet class with Madame Gazelle. George wasn't sure at first. But when they started spinning... George kept going round and round and round! He was the best in the class! Madame Gazelle said he was brilliant. Ballet is for everyone!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母 ll → /l/ 音（双写但只发一次）',
            "examples":['ballet', 'well', 'ball', 'bell', 'full'],
            "tongue_tip":'ll 只发一个 /l/，不用发两次。"Ballet is well done！"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP32 Thunderstorm（雷阵雨）——" 故意停顿制造悬念',
        "next_a":'EP32 Thunderstorm',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Ballet is for everyone.',"zh":'芭蕾舞是所有人的',"usage":'打破性别/年龄刻板印象'},
        {"sentence":'George is very good at spinning.',"zh":'George 转圈转得很好',"usage":'夸孩子某项技能'},
        {"sentence":'Can you balance on one foot?',"zh":'你能单脚站立吗？',"usage":'任何地方的小挑战'},
        {"sentence":'Graceful! Like a swan!',"zh":'优雅！像天鹅一样！',"usage":'动作优雅时的赞美'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 32 · Thunderstorm 雷阵雨
# ═══════════════════════════════════════════════════════════════════════════════
EP32 = _ep(
    num=32, title_en='Thunderstorm', title_zh='雷阵雨', color='slate',
    synopsis='打雷了，George 很害怕！Daddy 解释打雷是云碰撞发出的声音，并不危险。Peppa 每次听到雷声都数数来让 George 平静下来。最后全家一起数雷声，把害怕变成了游戏。',
    vocab=[        {"word":'thunder',"phonetic":'ˈθʌndə',"pos":'n.',"zh":'雷',"action":'做出轰隆声，"Thunder！ BOOM！"'},        {"word":'lightning',"phonetic":'ˈlaɪtnɪŋ',"pos":'n.',"zh":'闪电',"action":'手做闪电形状，"Lightning！ FLASH！"'},        {"word":'storm',"phonetic":'stɔːm',"pos":'n.',"zh":'暴风雨',"action":'双臂展开，模拟风雨，"Storm！"'},        {"word":'scared',"phonetic":'skeəd',"pos":'adj.',"zh":'害怕的',"action":'缩起来，"Scared！ Very scared!"'},        {"word":'explain',"phonetic":'ɪkˈspleɪn',"pos":'v.',"zh":'解释',"action":'做出解释的手势，"Let me explain..."'},        {"word":'count',"phonetic":'kaʊnt',"pos":'v.',"zh":'数数',"action":'"One... two... three..." 数数'},        {"word":'closer',"phonetic":'ˈkləʊsə',"pos":'adj.',"zh":'更近',"action":'渐渐靠近，"Coming closer!"'},        {"word":'brilliant',"phonetic":'ˈbrɪliənt',"pos":'adj.',"zh":'极好的',"action":'竖大拇指，"Brilliant！ Great！"'},    ],
    patterns=[        {"pattern":"Don't be scared, George.","zh":'别害怕，George',"example":"There's nothing to be scared of!"},        {"pattern":'Thunder is just clouds bumping together.',"zh":'雷声只是云朵互相碰撞',"example":"It's just a natural thing — nothing dangerous!"},        {"pattern":'Count the seconds between the lightning and the thunder.',"zh":'数闪电和雷声之间的秒数',"example":'If you count the seconds, you know how far away the storm is.'},        {"pattern":'The closer the storm, the smaller the count.',"zh":'暴风雨越近，数字越小',"example":'The storm is moving away — the count is getting bigger!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第31集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'⚡',"bg":'yellow',"trigger":'闪电出现',"action":'手做闪电状，"Flash！ Lightning！"'},
            {"emoji":'💥',"bg":'grey',"trigger":'雷声响起，George 害怕',"action":'缩起来，"BOOM！ Thunder！"'},
            {"emoji":'🔢',"bg":'blue',"trigger":'Peppa 教 George 数数',"action":'"One... two... three... BOOM！ Count!"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Why was George scared?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说雷声',"parent":'"Thunder！ The BOOM BOOM sound！ George thought it was dangerous. But Daddy explained..."'},
                {"child":'说闪电',"parent":'"The lightning too! But Daddy said: thunder is just clouds bumping together!"'},
                {"child":'不说话',"parent":'做出轰隆声，"George heard THIS！ Was he scared？"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"How did Peppa help George with the thunder?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说数数',"parent":'"COUNT！ Count the seconds between lightning and thunder! It makes it into a game!"'},
                {"child":'说不知道',"parent":'"She counted! One... two... BOOM! And the count tells you if the storm is close!"'},
                {"child":'不说话',"parent":'"One... two..." 停顿，"BOOM！ Counting!"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"Are you scared of anything like loud sounds or darkness?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说害怕的东西',"parent":'"Like George with thunder！ What helps you feel less scared？"'},
                {"child":'说不害怕',"parent":'"Brave！ Can you help George not be scared？ Tell him: thunder is just clouds!"'},
                {"child":'不说话',"parent":'"Everyone is scared of something. Even Daddy Pig... sometimes!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Do you like thunderstorms — yes or no? Why?"'],
            "rows":[
                {"child":'说喜欢',"parent":'"Thunder is exciting！ All that power! Like a nature show!"'},
                {"child":'说不喜欢',"parent":'"Too loud？ Like George！ But once you know it\'s just clouds bumping..."'},
                {"child":'不说话',"parent":'做出闪电和雷声，"FLASH... then BOOM! Exciting or scary?"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"George, there\'s a thunderstorm! Don\'t be scared! I\'ll explain!"'],
            "rows":[
                {"child":'做害怕状',"parent":'"Don\'t be scared! Thunder is just clouds bumping together!"'},
                {"child":'说 "scared!"',"parent":'"I know！ But let\'s count! One... two... BOOM！ See? We can count the storm!"'},
                {"child":'说中文',"parent":'家长扮 George，孩子解释："Tell George why thunder isn\'t scary!"'},
            ],
        },
        "recast":[
            {"term":'thunder is just clouds bumping together',"explanation":'"Just = 只是。 It\'s just clouds! Nothing dangerous!"'},
            {"term":'count the seconds',"explanation":'"Count the seconds = 数间隔的秒数。 This tells you how far away the storm is!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"FLASH！ Lightning！" — 手做闪电形状',
            '"BOOM！ Thunder！" — 做出轰隆声，手拍桌',
            '"Don\'t be scared！" — 伸出手安慰，"It\'s OK!"',
            '"Count！ One, two, three..." — 倒数，等雷声',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'雷声响起，George 害怕',"L1":'L1: "Thunder！ Scared！"',"L2":'L2: "George is scared of thunder！"',"L3":'L3: "BOOM! There\'s thunder! Poor George — he\'s very scared! Don\'t cry, George!"'},
            {"scene":'Daddy 解释雷声',"L1":'L1: "Clouds！ Bump！"',"L2":'L2: "Thunder is clouds bumping together！"',"L3":'L3: "Don\'t be scared, George! Thunder is just big clouds bumping into each other!"'},
            {"scene":'数闪电和雷声间隔',"L1":'L1: "Count！ One, two..."',"L2":'L2: "Count between lightning and thunder！"',"L3":'L3: "One... two... BOOM! The count tells us how close the storm is. If it\'s big, it\'s far away!"'},
        ],
        },
        "bugs":{
            "rule":'说 "thunder" 得1分；说 "scared" 得1分；说出 "Thunder is just clouds" 得3分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'thunder → lightning → storm → scared → count → closer'},
            {"level":'L2 (句)',"text":'There was a thunderstorm. George was scared. Daddy explained. Peppa counted the seconds.'},
            {"level":'L3 (完整)',"text":"There was a big thunderstorm! George was very scared of the thunder — BOOM！ But Daddy explained: thunder is just clouds bumping together! And Peppa showed George how to count between the lightning and thunder. One... two... BOOM！ The smaller the count, the closer the storm. Counting made it into a game, and George wasn't scared anymore!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 oun → /aʊn/ 音',
            "examples":['count', 'sound', 'round', 'ground', 'found'],
            "tongue_tip":'"COUNTDOWN！ The storm makes a sound that POUNDS the ground!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP33 Cleaning the Car（洗汽车）——" 故意停顿制造悬念',
        "next_a":'EP33 Cleaning the Car',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Thunder is just clouds bumping together.',"zh":'雷声只是云朵碰撞',"usage":'孩子害怕雷声时解释'},
        {"sentence":"Don't be scared.","zh":'别害怕',"usage":'安慰害怕孩子的开场'},
        {"sentence":'Count the seconds.',"zh":'数秒数',"usage":'把恐怖变成游戏的技巧'},
        {"sentence":'The closer the storm, the smaller the count.',"zh":'暴风雨越近，数字越小',"usage":'生活中的逻辑推理练习'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 33 · Cleaning the Car 洗汽车
# ═══════════════════════════════════════════════════════════════════════════════
EP33 = _ep(
    num=33, title_en='Cleaning the Car', title_zh='洗汽车', color='blue',
    synopsis='Daddy Pig 的车很脏了，需要洗车。全家人一起帮忙洗车，用水管、海绵、水桶。结果 Daddy 搞得到处是水，反倒把车洗干净了，但自己湿透了。',
    vocab=[        {"word":'dirty',"phonetic":'ˈdɜːti',"pos":'adj.',"zh":'脏的',"action":'皱眉，摸想象的脏东西，"Dirty! Ewww!"'},        {"word":'sponge',"phonetic":'spʌndʒ',"pos":'n.',"zh":'海绵',"action":'假装用海绵擦，"Sponge! Squish!"'},        {"word":'bucket',"phonetic":'ˈbʌkɪt',"pos":'n.',"zh":'水桶',"action":'假装端重物，"A bucket of water!"'},        {"word":'hose',"phonetic":'həʊz',"pos":'n.',"zh":'水管',"action":'假装拿水管，喷水，"Hose! Spray!"'},        {"word":'scrub',"phonetic":'skrʌb',"pos":'v.',"zh":'用力擦洗',"action":'双手用力擦，"Scrub scrub scrub!"'},        {"word":'spray',"phonetic":'spreɪ',"pos":'v.',"zh":'喷射',"action":'手做喷水动作，"Spray! Whoosh!"'},        {"word":'sparkling',"phonetic":'ˈspɑːklɪŋ',"pos":'adj.',"zh":'闪闪发光的',"action":'双手向外比，眼睛发光，"Sparkling clean!"'},        {"word":'soaking wet',"phonetic":'ˈsəʊkɪŋ wet',"pos":'adj.ph.',"zh":'湿透了',"action":'假装被淋湿，"Soaking wet! Dripping!"'},    ],
    patterns=[        {"pattern":'The car is very dirty.',"zh":'这辆车非常脏',"example":'These shoes are very dirty!'},        {"pattern":"Let's wash the car together.","zh":'我们一起洗车吧',"example":"Let's clean the house together."},        {"pattern":'Scrub scrub scrub!',"zh":'使劲擦！',"example":'Rub rub rub! Wash wash wash!'},        {"pattern":"Now it's sparkling clean!","zh":'现在亮晶晶的干净啦！',"example":'Look how clean! Sparkling!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第32集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🚗',"bg":'brown',"trigger":'脏车需要洗',"action":'皱眉，"This car is VERY dirty！"'},
            {"emoji":'🪣',"bg":'blue',"trigger":'拿水桶和海绵开始洗',"action":'假装端水桶，很重，"Heavy！"'},
            {"emoji":'💦',"bg":'blue',"trigger":'水管乱喷',"action":'假装水管失控，"Whoosh！ SPRAY！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Why did Daddy\'s car need washing?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说太脏了',"parent":'"Very dirty！ Muddy，grimy，no longer shiny!"'},
                {"child":'说 not sure',"parent":'"It was covered in mud and dirt! Not clean at all!"'},
                {"child":'不说话',"parent":'假装摸脏的东西，皱眉，"Ewww！ Dirty！ Like this!"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Did the car get clean at the end?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Yes！ Sparkling!"',"parent":'"Sparkling clean！ But what happened to Daddy Pig? He got... soaking wet！"'},
                {"child":'说 yes',"parent":'"The car was sparkling clean! But Daddy was totally drenched!"'},
                {"child":'不说话',"parent":'做出闪亮车的手势，"Sparkling！ But Daddy..." 假装湿透'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"What\'s the messiest job in your house?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说某个任务',"parent":'"Like washing the car！ Or washing dishes？ Does it end with everyone wet？"'},
                {"child":'说洗车',"parent":'"Washing the car! Will it go wrong like Daddy\'s？ SPRAY！"'},
                {"child":'不说话',"parent":'"In our house — the messiest job is..." 假装思考，"...feeding you！"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever helped wash something — a car, dishes, yourself?"'],
            "rows":[
                {"child":'说有',"parent":'"Did you get wet？ Did you use a sponge or a hose？"'},
                {"child":'摇头',"parent":'"Never？ Let\'s plan a car wash！ Well... when we get a car!"'},
                {"child":'笑了',"parent":'"The hose always sprays the wrong way！"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Our car is filthy！ Let\'s wash it！ You take the sponge — I\'ll get the hose!"'],
            "rows":[
                {"child":'假装洗车',"parent":'"Scrub scrub scrub！ Now spray!" 做水管喷水动作'},
                {"child":'说 "Spray!"',"parent":'"WHOOSH！ Oh no！ I\'m soaking wet！ But the car is sparkling！"'},
                {"child":'说中文',"parent":'家长扮 Daddy Pig："Soaking wet！ But the car is clean！ Worth it!"'},
            ],
        },
        "recast":[
            {"term":'soaking wet',"explanation":'"Soaking = 浸透的。 Soaking wet = 浑身湿透了"'},
            {"term":'sparkling clean',"explanation":'"Sparkling = 闪闪发光。 Sparkling clean = 干净得闪光！"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Scrub scrub scrub！" — 双手用力擦圆圈',
            '"SPRAY！" — 假装水管喷水',
            '"Soaking wet！" — 假装浑身湿透，滴水',
            '"Sparkling clean！" — 双手展示发光的车',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Daddy 看到脏车',"L1":'L1: "Dirty！"',"L2":'L2: "The car is very dirty！"',"L3":'L3: "Oh no! Look at the car! It\'s covered in mud! We need to wash it today!"'},
            {"scene":'全家洗车',"L1":'L1: "Scrub！ Clean！"',"L2":'L2: "Let\'s wash the car together！"',"L3":'L3: "Sponge! Bucket! Hose! Everyone help! Scrub scrub scrub!"'},
            {"scene":'Daddy 被水淋湿但车干净了',"L1":'L1: "Wet！ Clean！"',"L2":'L2: "Daddy is soaking wet but the car is clean！"',"L3":'L3: "Oh! The hose went the wrong way! But look — the car is sparkling clean! Worth it!"'},
        ],
        },
        "bugs":{
            "rule":'说 "scrub" 得1分；说 "sparkling clean" 得2分；说 "soaking wet" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'dirty → sponge → bucket → hose → scrub → spray → sparkling → soaking wet'},
            {"level":'L2 (句)',"text":"Daddy's car was dirty. The family washed it together. Daddy got soaking wet. The car was sparkling clean."},
            {"level":'L3 (完整)',"text":"Daddy Pig's car was very dirty — covered in mud! The whole family helped wash it. Peppa had the sponge, George had the bucket, and Daddy had the hose. But the hose sprayed everywhere! WHOOSH！ Daddy got soaking wet! But in the end, the car was sparkling clean. Worth getting wet for！"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ub → /ʌb/ 音',
            "examples":['scrub', 'rub', 'tub', 'club', 'hub'],
            "tongue_tip":'短促 /ʌ/ 音。"Scrub the tub in the club!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP34 Lunch（午餐）——" 故意停顿制造悬念',
        "next_a":'EP34 Lunch',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'The car is very dirty!',"zh":'这车太脏了！',"usage":'形容任何脏东西'},
        {"sentence":'Scrub scrub scrub!',"zh":'使劲擦！',"usage":'鼓励做家务时'},
        {"sentence":'Soaking wet!',"zh":'湿透了！',"usage":'淋雨或洗澡时'},
        {"sentence":'Sparkling clean!',"zh":'亮晶晶的干净！',"usage":'清洁完毕的满足感'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 34 · Lunch 午餐
# ═══════════════════════════════════════════════════════════════════════════════
EP34 = _ep(
    num=34, title_en='Lunch', title_zh='午餐', color='green',
    synopsis='Peppa 去 Suzy Sheep 家吃午饭。Suzy 的妈妈做了菠菜和胡萝卜，Peppa 不想吃蔬菜。但最后为了能吃到甜点，Peppa 吃完了所有蔬菜。',
    vocab=[        {"word":'spinach',"phonetic":'ˈspɪnɪtʃ',"pos":'n.',"zh":'菠菜',"action":'假装一大碗绿色蔬菜，皱眉，"Spinach！"'},        {"word":'carrot',"phonetic":'ˈkærət',"pos":'n.',"zh":'胡萝卜',"action":'用手比出长长的橙色，"Carrot！"'},        {"word":'vegetables',"phonetic":'ˈvedʒtəblz',"pos":'n.',"zh":'蔬菜',"action":'做出各种蔬菜形状'},        {"word":'dessert',"phonetic":'dɪˈzɜːt',"pos":'n.',"zh":'甜点',"action":'做出圆蛋糕形状，眼睛发光，"Dessert！"'},        {"word":'finish',"phonetic":'ˈfɪnɪʃ',"pos":'v.',"zh":'吃完、完成',"action":'做完成动作，"Finish your plate!"'},        {"word":'guest',"phonetic":'ɡest',"pos":'n.',"zh":'客人',"action":'做出欢迎手势，"Welcome, guest!"'},        {"word":'polite',"phonetic":'pəˈlaɪt',"pos":'adj.',"zh":'礼貌的',"action":'点头微笑，"Be polite! Manners!"'},        {"word":'refuse',"phonetic":'rɪˈfjuːz',"pos":'v.',"zh":'拒绝',"action":'摇头，"I refuse to eat spinach!"'},    ],
    patterns=[        {"pattern":'Can I have some more, please?',"zh":'请问我可以再要一点吗？',"example":'Can I have some more cake, please?'},        {"pattern":'You must eat your vegetables.',"zh":'你必须吃蔬菜',"example":'You must eat your greens before dessert!'},        {"pattern":'If you finish your lunch, you can have dessert.',"zh":'如果你吃完午饭，就可以吃甜点',"example":'If you eat your vegetables, you can have dessert.'},        {"pattern":"Be polite when you're a guest.","zh":'做客的时候要有礼貌',"example":'Say please and thank you — be polite!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第33集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🥦',"bg":'green',"trigger":'Mummy Sheep 端上蔬菜午餐',"action":'皱鼻子，"Vegetables！ Hmm..."'},
            {"emoji":'🥕',"bg":'orange',"trigger":'Peppa 不想吃菠菜',"action":'摇头，"Spinach！ I don\'t want spinach!"'},
            {"emoji":'🍨',"bg":'pink',"trigger":'甜点来了',"action":'眼睛发光，立刻吃完蔬菜'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What did Suzy\'s mummy make for lunch?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说蔬菜/菠菜胡萝卜',"parent":'"Spinach and carrots！ Very healthy！ But Peppa didn\'t want to eat them!"'},
                {"child":'说不知道',"parent":'"Spinach! Green and leafy! And carrots! Peppa was NOT happy about it!"'},
                {"child":'不说话',"parent":'做出皱鼻子表情，"What was on the plate？ Something green..."'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Why did Peppa eat all her vegetables in the end?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说为了甜点',"parent":'"DESSERT！ If you finish your vegetables, you can have dessert！ Brilliant motivation!"'},
                {"child":'说她饿了',"parent":'"Actually... it was the DESSERT! Peppa really wanted the ice cream!"'},
                {"child":'不说话',"parent":'指向想象的甜点，眼睛发光，"What was coming AFTER vegetables？ Dessert！"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"Is there any food you really don\'t like eating?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说蔬菜名',"parent":'"Like Peppa! Is there a dessert that would make you eat it?"'},
                {"child":'说没有',"parent":'"You eat everything？ Like George with his vegetables！ Amazing!"'},
                {"child":'不说话',"parent":'"Me — I don\'t like..." 故意说孩子喜欢的东西，等孩子纠正'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever had to eat something you didn\'t like at someone\'s house?"'],
            "rows":[
                {"child":'说过',"parent":'"Like Peppa at Suzy\'s! Did you finish it? Were you polite?"'},
                {"child":'摇头',"parent":'"Never? You\'re very lucky! Or very good at hiding food under the plate..."'},
                {"child":'笑了',"parent":'"Hide the spinach under the bread... classic trick!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Lunch is ready！ Please sit down！ Today we have... spinach！"'],
            "rows":[
                {"child":'假装不想吃',"parent":'"I know! It\'s not your favourite! But if you finish... there\'s DESSERT！"'},
                {"child":'说 "Dessert?!"',"parent":'"YES！ Ice cream! Finish your spinach first, please!"'},
                {"child":'说中文',"parent":'家长扮 Mummy Sheep："Please eat your vegetables！ Then dessert!"'},
            ],
        },
        "recast":[
            {"term":'if you finish... you can have',"explanation":'"If + condition = 条件句。 If you eat vegetables, you can have dessert!"'},
            {"term":'polite',"explanation":'"Polite = 有礼貌。 Be polite = 举止有礼貌"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Eat your vegetables！" — 假装吃蔬菜，夸张嚼',
            '"Dessert！" — 眼睛发光，双手合十',
            '"Be polite！ Say please！" — 点头微笑，"Please!"',
            '"Finish your plate！" — 做完成手势',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'午饭是蔬菜',"L1":'L1: "Spinach！ Ewww！"',"L2":'L2: "I don\'t want to eat spinach！"',"L3":'L3: "Mummy Sheep made spinach and carrots! But I don\'t like spinach!"'},
            {"scene":'不吃完不给甜点',"L1":'L1: "Finish！ Dessert！"',"L2":'L2: "If you finish, you can have dessert！"',"L3":'L3: "Eat your vegetables please! If you finish your lunch, you can have dessert!"'},
            {"scene":'Peppa 吃完了蔬菜',"L1":'L1: "Finished！"',"L2":'L2: "I finished all my vegetables！"',"L3":'L3: "All done! I finished every bit! Now can I have my dessert please? The ice cream?"'},
        ],
        },
        "bugs":{
            "rule":'说 "polite" 得1分；说 "please" 得1分；说 "If I finish... I can have" 得3分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'spinach → carrots → vegetables → dessert → polite → finish'},
            {"level":'L2 (句)',"text":"Peppa had lunch at Suzy's house. The food was spinach and carrots. Peppa didn't want to eat them. She ate them for the dessert."},
            {"level":'L3 (完整)',"text":"Peppa was a guest at Suzy's house for lunch. Suzy's mummy made spinach and carrots. Peppa did NOT want to eat them! But then she heard: if you finish your lunch, you can have dessert. Ice cream! Suddenly the spinach didn't seem so bad. Peppa ate every last bit — and got her ice cream!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ert → /ɜːt/ 音',
            "examples":['dessert', 'alert', 'concert', 'insert', 'expert'],
            "tongue_tip":'注意 desert（沙漠）只有一个 s，dessert（甜点）有两个 s！"The dessert is in the desert!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP35 Camping（野营）——" 故意停顿制造悬念',
        "next_a":'EP35 Camping',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'You must eat your vegetables.',"zh":'你必须吃蔬菜',"usage":'每顿饭都可以用'},
        {"sentence":'If you finish your lunch, you can have dessert.',"zh":'吃完午饭才能吃甜点',"usage":'世界上最强的条件句'},
        {"sentence":"Be polite when you're a guest.","zh":'做客要有礼貌',"usage":'去别人家吃饭前叮嘱'},
        {"sentence":'Can I have some more, please?',"zh":'我可以再要一点吗？',"usage":'示范礼貌请求'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 35 · Camping 野营
# ═══════════════════════════════════════════════════════════════════════════════
EP35 = _ep(
    num=35, title_en='Camping', title_zh='野营', color='green',
    synopsis='全家去野营！他们搭帐篷，在户外做晚餐，听各种奇怪的声音。Daddy 说他知道所有动物的叫声，结果被揭穿——那些都是普通的声音。',
    vocab=[        {"word":'camping',"phonetic":'ˈkæmpɪŋ',"pos":'n.',"zh":'野营',"action":'假装搭帐篷，"Camping！ Outdoors!"'},        {"word":'tent',"phonetic":'tent',"pos":'n.',"zh":'帐篷',"action":'双手在头顶做帐篷形状'},        {"word":'campfire',"phonetic":'ˈkæmpfaɪə',"pos":'n.',"zh":'营火',"action":'双手向中间合拢，做火焰形状，"Crackle!"'},        {"word":'torch',"phonetic":'tɔːtʃ',"pos":'n.',"zh":'手电筒',"action":'假装拿手电筒照射，"Shine the torch！"'},        {"word":'owl',"phonetic":'aʊl',"pos":'n.',"zh":'猫头鹰',"action":'"Twit-twoo！ An owl！"'},        {"word":'rustle',"phonetic":'ˈrʌsl',"pos":'v./n.',"zh":'沙沙声',"action":'轻轻摩擦手，"Rustle... what\'s that sound？"'},        {"word":'sleeping bag',"phonetic":'ˈsliːpɪŋ bæɡ',"pos":'n.',"zh":'睡袋',"action":'假装爬进袋子，拉拉链，"Sleeping bag！"'},        {"word":'identify',"phonetic":'aɪˈdentɪfaɪ',"pos":'v.',"zh":'识别',"action":'假装听声音，点头，"I can identify that sound!"'},    ],
    patterns=[        {"pattern":'Are you ready for camping?',"zh":'你准备好野营了吗？',"example":'Are you ready for the adventure?'},        {"pattern":"Listen! What's that sound?","zh":'听！那是什么声音？',"example":'Listen carefully — can you hear something?'},        {"pattern":"That's a [animal] — I'm certain of it!","zh":'那肯定是[动物]——我确定！',"example":"That's definitely a fox. I'm certain!"},        {"pattern":"Let's put up the tent.","zh":'我们来搭帐篷吧',"example":'First we put up the tent, then we can sleep!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第34集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'⛺',"bg":'green',"trigger":'搭帐篷',"action":'假装撑起帐篷杆，"Up！ The tent!"'},
            {"emoji":'🔦',"bg":'yellow',"trigger":'夜晚用手电筒照',"action":'假装拿手电筒，"Flash！"'},
            {"emoji":'🦉',"bg":'purple',"trigger":'听到奇怪声音，Daddy 解释',"action":'"Twit-twoo！ That\'s an OWL！ I\'m certain!"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What did the family sleep in when camping?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说帐篷/睡袋',"parent":'"A TENT and sleeping bags！ All cosy together under the stars!"'},
                {"child":'说 not sure',"parent":'"A tent！ And sleeping bags！ All zipped up and cosy!"'},
                {"child":'不说话',"parent":'假装爬进睡袋，拉拉链，"Zip! Sleeping bag！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Was Daddy really an expert on animal sounds?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'笑着说不是',"parent":'"Haha！ He SAID he was！ But the \'owl\' might have been Mummy Pig\'s snoring..."'},
                {"child":'说是',"parent":'"He thought he was！ \'I\'m certain of it!\' But he was... not always right!"'},
                {"child":'不说话',"parent":'做出 Daddy 自信姿态，"I\'m certain！" 然后耸肩'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you went camping, what ONE thing would you bring with you?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说物品',"parent":'"A [item]！ Smart choice! Camping needs [item]!"'},
                {"child":'说手电筒',"parent":'"A torch！ Essential! You need to shine it when you hear scary noises!"'},
                {"child":'不说话',"parent":'"Me — I\'d bring... hot chocolate. And marshmallows. And... a very good tent!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever slept anywhere other than your own bed?"'],
            "rows":[
                {"child":'说过',"parent":'"Like camping！ Did you hear any strange sounds? What were they?"'},
                {"child":'摇头',"parent":'"Never？ Your own bed is very cosy！ But camping is special — stars above you..."'},
                {"child":'笑了',"parent":'"Strange noises! What\'s that sound？ An owl? Or Daddy snoring?"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Welcome to Camping Night！ First — put up the tent! Let\'s go!"'],
            "rows":[
                {"child":'假装搭帐篷',"parent":'"Great！ Now light the campfire！ And listen — what\'s that sound？"'},
                {"child":'说某种声音',"parent":'"That\'s a..." 假装听，"An owl！ I\'m certain of it！"'},
                {"child":'说中文',"parent":'家长扮 Daddy："I\'m an expert on camping！ First things first — the tent！"'},
            ],
        },
        "recast":[
            {"term":"I'm certain of it","explanation":'"Certain = 确定的。 I\'m certain = 我确定。 Daddy was... not always certain!"'},
            {"term":'rustle',"explanation":'"Rustle = 沙沙声，轻微摩擦声。 The leaves rustle in the wind."'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Put up the tent！" — 假装撑帐篷',
            '"Listen！ What\'s that sound？" — 手放耳边，侧耳',
            '"Shine the torch！" — 假装手电筒',
            '"I\'m certain of it！" — 自信指向，点头',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'到达营地',"L1":'L1: "Camping！"',"L2":'L2: "We\'re going camping！"',"L3":'L3: "Here we are! Time to put up the tent and make a campfire!"'},
            {"scene":'听到奇怪声音',"L1":'L1: "What\'s that？"',"L2":'L2: "Listen! What\'s that sound？"',"L3":'L3: "Shhh! Listen! What\'s that sound? Is that an owl? Or something else?"'},
            {"scene":'Daddy 自信识别声音',"L1":'L1: "Owl！ Certain！"',"L2":'L2: "That\'s an owl — I\'m certain！"',"L3":'L3: "That rustle? That\'s a fox. That sound? An owl. I\'m an expert — I\'m certain of it!"'},
        ],
        },
        "bugs":{
            "rule":'说 "I\'m certain of it" 得3分；说 "camping" 得1分；说出任何动物叫声得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'camping → tent → campfire → torch → owl → sleeping bag → certain'},
            {"level":'L2 (句)',"text":'The family went camping. They put up a tent. At night they heard strange sounds. Daddy said he knew what they were.'},
            {"level":'L3 (完整)',"text":"The Pig family went camping! They put up the tent, made a campfire, and had a wonderful outdoor dinner. When night fell, they heard strange sounds. Daddy said he was an expert: 'That's an owl! That's a fox! I'm certain of it!' But the sounds turned out to be much more ordinary..."},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ight → /aɪt/ 音',
            "examples":['night', 'light', 'right', 'tight', 'campsite'],
            "tongue_tip":'igh 的 gh 不发音，只有 /aɪ/。"At night, we need a light!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP36 The Sleepy Princess（爱睡觉的公主）——" 故意停顿制造悬念',
        "next_a":'EP36 The Sleepy Princess',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"I'm certain of it!","zh":'我确定！',"usage":'说完以后假装 Daddy Pig，然后等事情出错'},
        {"sentence":"Listen! What's that sound?","zh":'听！那是什么声音？',"usage":'一起注意环境声音'},
        {"sentence":"Let's put up the tent.","zh":'我们来搭帐篷吧',"usage":'任何搭建/组装活动前'},
        {"sentence":'Are you ready for the adventure?',"zh":'你准备好冒险了吗？',"usage":'出发前的仪式感'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 36 · The Sleepy Princess 爱睡觉的公主
# ═══════════════════════════════════════════════════════════════════════════════
EP36 = _ep(
    num=36, title_en='The Sleepy Princess', title_zh='爱睡觉的公主', color='purple',
    synopsis='Daddy 给 Peppa 讲了一个关于公主的故事——公主太爱睡觉了，连重要时刻都睡着。Peppa 却说她不想当那种公主，她想当一个会骑马打仗的公主！',
    vocab=[        {"word":'princess',"phonetic":'ˈprɪnses',"pos":'n.',"zh":'公主',"action":'头戴想象王冠，"I am a princess！"'},        {"word":'knight',"phonetic":'naɪt',"pos":'n.',"zh":'骑士',"action":'假装穿盔甲，"A brave knight！"'},        {"word":'dragon',"phonetic":'ˈdræɡən',"pos":'n.',"zh":'龙',"action":'做出恐龙吼声，双臂张开，"A fire-breathing dragon！"'},        {"word":'castle',"phonetic":'ˈkɑːsl',"pos":'n.',"zh":'城堡',"action":'双手向上描绘尖塔'},        {"word":'asleep',"phonetic":'əˈsliːp',"pos":'adj.',"zh":'睡着的',"action":'合上眼，发出轻轻鼾声'},        {"word":'adventure',"phonetic":'ədˈventʃə',"pos":'n.',"zh":'冒险',"action":'举拳，"Adventure！ Excitement！"'},        {"word":'wake up',"phonetic":'weɪk ʌp',"pos":'v.ph.',"zh":'醒来',"action":'假装推开眼皮，"Wake up！ Time to go！"'},        {"word":'brave',"phonetic":'breɪv',"pos":'adj.',"zh":'勇敢的',"action":'挺胸，"Brave！ Courageous！"'},    ],
    patterns=[        {"pattern":'Once upon a time...',"zh":'从前有一次...',"example":'Once upon a time, there was a little pig...'},        {"pattern":'The princess fell asleep.',"zh":'公主睡着了',"example":"She just couldn't stay awake!"},        {"pattern":'I want to be a brave princess.',"zh":'我想当一个勇敢的公主',"example":'I want to go on adventures!'},        {"pattern":'The dragon is coming!',"zh":'龙来了！',"example":'Run! The dragon is coming!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第35集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'👸',"bg":'purple',"trigger":'Daddy 讲公主故事',"action":'假装讲故事，"Once upon a time..."'},
            {"emoji":'😴',"bg":'grey',"trigger":'公主又睡着了',"action":'合上眼，鼾声'},
            {"emoji":'⚔️',"bg":'gold',"trigger":'Peppa 说要当勇敢的公主',"action":'挺胸，"Brave princess！ Adventure！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What was special about the princess in Daddy\'s story?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说太爱睡觉',"parent":'"She kept falling asleep! At the worst moments! Even when the dragon came!"'},
                {"child":'说不知道',"parent":'"She loved sleeping! Any time, anywhere — even on adventures!"'},
                {"child":'不说话',"parent":'合上眼，假装睡着，"Zzzzz... even when the dragon arrives!"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What kind of princess does Peppa want to be?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说勇敢的',"parent":'"A BRAVE princess！ Not the sleepy one！ She wants adventures！"'},
                {"child":'说不知道',"parent":'"Peppa wants to go on adventures, fight dragons, ride horses!"'},
                {"child":'不说话',"parent":'做出骑马、挥剑动作，"That\'s Peppa\'s kind of princess!"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you were in a fairy tale, would you rather be the princess or the knight?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说公主',"parent":'"The princess！ The brave kind — like Peppa! Adventures and dragons!"'},
                {"child":'说骑士',"parent":'"A knight！ In shining armour！ Brave and strong!"'},
                {"child":'不说话',"parent":'"Me — I\'d be the dragon. ROAR！ Everyone is scared of me!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"What\'s your favourite kind of story?"'],
            "rows":[
                {"child":'说冒险',"parent":'"Adventures！ Knights and dragons and brave heroes!"'},
                {"child":'说公主/童话',"parent":'"Fairy tales！ Like Daddy\'s story! But with a BRAVE princess!"'},
                {"child":'不说话',"parent":'"My favourite story starts: Once upon a time, there was a very clever child..."'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Once upon a time, there was a brave princess... that\'s YOU！ What happens next?"'],
            "rows":[
                {"child":'说故事',"parent":'"And then...？ Does the princess fight the dragon？ Does she win？"'},
                {"child":'做动作',"parent":'"ROAR！ The dragon comes！ What does the brave princess do？"'},
                {"child":'说中文',"parent":'家长扮故事里的角色，等孩子当公主'},
            ],
        },
        "recast":[
            {"term":'once upon a time',"explanation":'"Once upon a time = 从前有一次。 Every fairy tale starts like this!"'},
            {"term":'fell asleep',"explanation":'"Fall asleep = 睡着了（不是主动睡觉，是自然睡过去了）"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Once upon a time！" — 讲故事的声音，庄重地',
            '"The dragon is coming！" — 做出龙来了的恐慌',
            '"The princess fell asleep！" — 合眼，鼾声',
            '"Brave princess！ Charge！" — 骑马向前冲',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Daddy 讲故事开头',"L1":'L1: "Story！"',"L2":'L2: "Once upon a time..."',"L3":'L3: "Once upon a time there was a princess. She lived in a beautiful castle. But she had a problem..."'},
            {"scene":'公主又睡着了',"L1":'L1: "Asleep！"',"L2":'L2: "The princess fell asleep！"',"L3":'L3: "And at the most important moment... the princess... fell... asleep. Again!"'},
            {"scene":'Peppa 说要当勇敢公主',"L1":'L1: "Brave！"',"L2":'L2: "I want to be a brave princess！"',"L3":'L3: "I don\'t want to be a sleepy princess! I want to be brave and go on adventures!"'},
        ],
        },
        "bugs":{
            "rule":'说 "Once upon a time" 得3分；说 "brave" 得1分；说 "dragon" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'princess → knight → dragon → asleep → brave → adventure → castle'},
            {"level":'L2 (句)',"text":'Daddy told a story about a sleepy princess. Peppa said she wants to be a brave princess instead.'},
            {"level":'L3 (完整)',"text":"Daddy told Peppa a bedtime story about a princess who kept falling asleep at the worst moments! Even when the dragon came — she fell asleep! Peppa said: that's not the kind of princess I want to be! I want to go on adventures, fight dragons, and ride horses! A brave princess!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ce/se → /s/ 清音结尾',
            "examples":['princess', 'once', 'dance', 'prince', 'fence'],
            "tongue_tip":'结尾的 ce/se 发 /s/ 清音，不振动声带。"The princess danced once in the palace!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP37 The Tree House（树屋）——" 故意停顿制造悬念',
        "next_a":'EP37 The Tree House',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Once upon a time...',"zh":'从前有一次...',"usage":'讲故事必备开场白'},
        {"sentence":'I want to be a brave princess!',"zh":'我想当一个勇敢的公主',"usage":'让孩子描述自己想成为的角色'},
        {"sentence":'The dragon is coming!',"zh":'龙来了！',"usage":'制造戏剧性张力'},
        {"sentence":'Wake up！ Adventure awaits！',"zh":'醒来！冒险在等着！',"usage":'早上叫孩子起床的专属句'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 37 · The Tree House 树屋
# ═══════════════════════════════════════════════════════════════════════════════
EP37 = _ep(
    num=37, title_en='The Tree House', title_zh='树屋', color='green',
    synopsis='Grandpa Pig 用木头为 Peppa 和 George 搭建了一个树屋！搭建过程中 Daddy 也来帮忙，但弄得乱七八糟。最后树屋完成了，大家都爱上了这个属于孩子们的秘密基地。',
    vocab=[        {"word":'tree house',"phonetic":'triː haʊs',"pos":'n.',"zh":'树屋',"action":'双手向上，描绘树上的小屋'},        {"word":'build',"phonetic":'bɪld',"pos":'v.',"zh":'建造',"action":'假装钉钉子，"Build！ Hammer! Nail!"'},        {"word":'hammer',"phonetic":'ˈhæmə',"pos":'n./v.',"zh":'锤子/敲打',"action":'假装用锤子敲，"Hammer！ BANG!"'},        {"word":'nail',"phonetic":'neɪl',"pos":'n.',"zh":'钉子',"action":'拇指和食指夹住想象的小钉子'},        {"word":'wood',"phonetic":'wʊd',"pos":'n.',"zh":'木头',"action":'假装扛着厚重木板，"Heavy wood!"'},        {"word":'ladder',"phonetic":'ˈlædə',"pos":'n.',"zh":'梯子',"action":'手做爬梯子动作'},        {"word":'secret',"phonetic":'ˈsiːkrɪt',"pos":'adj.',"zh":'秘密的',"action":'手指放嘴前，"Shhh! Secret!"'},        {"word":'cosy',"phonetic":'ˈkəʊzi',"pos":'adj.',"zh":'舒适温馨的',"action":'抱紧自己，"Cosy! Warm and comfortable!"'},    ],
    patterns=[        {"pattern":'Grandpa is building a tree house.',"zh":'爷爷在建树屋',"example":'Daddy is building a shelf. Grandpa is building a tree house.'},        {"pattern":'Can we help?',"zh":'我们可以帮忙吗？',"example":'Can we help you build it?'},        {"pattern":"It's our secret place.","zh":'这是我们的秘密基地',"example":'This is our special secret place!'},        {"pattern":'Bang! Bang! Hammer the nail.',"zh":'咚！咚！敲钉子',"example":'Hammer the nail in — bang bang bang!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第36集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🌳',"bg":'green',"trigger":'Grandpa 开始建树屋',"action":'假装钉钉子，"BANG！ BANG！"'},
            {"emoji":'🔨',"bg":'brown',"trigger":'Daddy 来帮忙但搞乱了',"action":'做出笨手笨脚的样子'},
            {"emoji":'🏠',"bg":'green',"trigger":'树屋完成，大家上去玩',"action":'攀爬，然后兴奋地向下张望'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Who built the tree house?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说 Grandpa',"parent":'"YES！ Grandpa Pig! He\'s brilliant at building things! BANG BANG!"'},
                {"child":'说 Daddy',"parent":'"Daddy tried to help! But Grandpa was the real builder here!"'},
                {"child":'不说话',"parent":'假装用锤子，"BANG！ Who was doing this？ Grandpa！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Did Peppa and George like the tree house?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Yes! Loved it!"',"parent":'"YES！ They LOVED it！ Their own secret place up in the tree！"'},
                {"child":'说不确定',"parent":'"They climbed up and looked around... and said: this is OUR secret place!"'},
                {"child":'不说话',"parent":'假装向上攀爬，到顶，然后向四周张望，惊喜表情'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you could have any secret place, what would it be like?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说树屋',"parent":'"A tree house！ High up！ You can see everything from there!"'},
                {"child":'说洞穴/地下室',"parent":'"A secret cave！ Dark and mysterious! Only YOU know where it is!"'},
                {"child":'不说话',"parent":'"My secret place would be... a library island where nobody else can find me!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Do you have a favourite secret spot at home?"'],
            "rows":[
                {"child":'说地方',"parent":'"Like the tree house! Your own special place!"'},
                {"child":'摇头',"parent":'"Let\'s find one！ Behind the sofa? Under the stairs? Under the bed?"'},
                {"child":'笑了',"parent":'"Show me after! I\'ll promise not to tell anyone!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Grandpa is building something in the garden! Shall we go and see？"'],
            "rows":[
                {"child":'假装观看',"parent":'"BANG BANG! Grandpa, what are you building?"'},
                {"child":'说树屋',"parent":'"A TREE HOUSE？! Amazing！ Can we help？ Can we go up when it\'s done?"'},
                {"child":'说中文',"parent":'家长扮 Grandpa："I\'m building you a tree house！ A secret place！"'},
            ],
        },
        "recast":[
            {"term":'tree house',"explanation":'"Tree house = tree（树）+ house（房子）= 树屋！"'},
            {"term":'secret place',"explanation":'"Secret = 秘密的。 Secret place = 只有我们知道的地方！"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Build it！ BANG！ BANG！" — 假装用锤子',
            '"Climb the ladder！" — 做爬梯子动作',
            '"It\'s our secret place！ Shhh！" — 指向树屋，手指嘴唇',
            '"So cosy！" — 抱紧自己，满足地点头',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Grandpa 建树屋',"L1":'L1: "Build！ Tree house！"',"L2":'L2: "Grandpa is building a tree house！"',"L3":'L3: "Bang! Bang! Grandpa is hammering nails! He\'s building a tree house for Peppa and George!"'},
            {"scene":'树屋完工',"L1":'L1: "Done！ Finished！"',"L2":'L2: "The tree house is finished！"',"L3":'L3: "It\'s done! The tree house is ready! Let\'s climb up! It\'s our secret place!"'},
            {"scene":'孩子们在树屋里',"L1":'L1: "Our place！"',"L2":'L2: "This is our secret place！"',"L3":'L3: "We can see everything from up here! This is our cosy secret tree house!"'},
        ],
        },
        "bugs":{
            "rule":'说 "secret place" 得2分；说 "build" 得1分；说出 "BANG BANG！" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'tree house → build → hammer → nail → ladder → secret → cosy'},
            {"level":'L2 (句)',"text":'Grandpa built a tree house. Daddy helped. The tree house was finished. Peppa and George loved it.'},
            {"level":'L3 (完整)',"text":"Grandpa Pig decided to build Peppa and George a tree house in the garden! He hammered nails and fixed boards — BANG BANG！ Daddy helped too, though he made a few mistakes. Finally the tree house was ready! Peppa and George climbed the ladder and looked around. 'This is our secret place!' they said. So cosy!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ould → /ʊd/ 音（could, would, should）',
            "examples":['could', 'would', 'should', 'wood', 'good'],
            "tongue_tip":'ould 的 l 不发音，读作 /ʊd/。"Could you build a tree house? Would you? Should you?"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP38 Fancy Dress Party（化装派对）——" 故意停顿制造悬念',
        "next_a":'EP38 Fancy Dress Party',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Grandpa is building a tree house!',"zh":'爷爷在建树屋！',"usage":'建筑/搭建类活动'},
        {"sentence":'This is our secret place.',"zh":'这是我们的秘密基地',"usage":'任何孩子的专属空间'},
        {"sentence":'Can we help?',"zh":'我们可以帮忙吗？',"usage":'培养孩子参与感'},
        {"sentence":'Bang! Bang!',"zh":'咚！咚！',"usage":'任何敲打声的拟声词'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 38 · Fancy Dress Party 化装派对
# ═══════════════════════════════════════════════════════════════════════════════
EP38 = _ep(
    num=38, title_en='Fancy Dress Party', title_zh='化装派对', color='orange',
    synopsis='Peppa 和朋友们参加化装派对！大家穿着各种有趣的服装：太空人、公主、海盗、蜘蛛侠……George 来了一个完美的惊喜——他穿着恐龙服装！',
    vocab=[        {"word":'fancy dress',"phonetic":'ˈfænsi dres',"pos":'n.',"zh":'化装服',"action":'展示想象的奇特服装，"Fancy dress！"'},        {"word":'costume',"phonetic":'ˈkɒstjuːm',"pos":'n.',"zh":'服装、戏服',"action":'假装穿上特殊服装，"In costume！"'},        {"word":'astronaut',"phonetic":'ˈæstrənɔːt',"pos":'n.',"zh":'宇航员',"action":'假装飞翔，"Astronaut！ In space!"'},        {"word":'pirate',"phonetic":'ˈpaɪrət',"pos":'n.',"zh":'海盗',"action":'双手叉腰，"Ahoy！ I\'m a pirate!"'},        {"word":'witch',"phonetic":'wɪtʃ',"pos":'n.',"zh":'女巫',"action":'假装拿扫帚，"Cackle! I\'m a witch!"'},        {"word":'disguise',"phonetic":'dɪsˈɡaɪz',"pos":'n.',"zh":'伪装',"action":'假装戴假鼻子，"Disguise！ Nobody knows it\'s me！"'},        {"word":'recognise',"phonetic":'ˈrekəɡnaɪz',"pos":'v.',"zh":'认出',"action":'指向人，"I recognise you！ You\'re Peppa!"'},        {"word":'brilliant',"phonetic":'ˈbrɪliənt',"pos":'adj.',"zh":'很棒的',"action":'竖大拇指，"Brilliant！ Great costume!"'},    ],
    patterns=[        {"pattern":'What are you dressed up as?',"zh":'你扮的是什么？',"example":'What are you dressed up as? A witch?'},        {"pattern":"I'm dressed up as an astronaut.","zh":'我扮的是宇航员',"example":"I'm dressed up as a princess today!"},        {"pattern":"I didn't recognise you!","zh":'我没认出你！',"example":"You look so different — I didn't recognise you!"},        {"pattern":'What a brilliant costume!',"zh":'真是个精彩的服装！',"example":'What a brilliant disguise!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第37集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🎭',"bg":'orange',"trigger":'派对开始，各种服装亮相',"action":'做各种角色动作：宇航员、海盗、女巫'},
            {"emoji":'🦕',"bg":'green',"trigger":'George 以恐龙服装出现',"action":'做恐龙吼声，"GRRR！"'},
            {"emoji":'🏆',"bg":'gold',"trigger":'大家评选最佳服装',"action":'假装颁奖，"The winner is..."'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What was George dressed up as at the fancy dress party?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Dinosaur!"',"parent":'"YES！ A DINOSAUR！ Of course！ His favourite! GRRR！"'},
                {"child":'说其他',"parent":'"George has ONE favourite thing... starts with D... Dino..."'},
                {"child":'不说话',"parent":'做出恐龙动作，"GRRR！ Was George dressed as THIS?"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What costume would YOU want to wear to a fancy dress party?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说服装',"parent":'"A [costume]！ Brilliant！ What would you say or do in that costume?"'},
                {"child":'说恐龙',"parent":'"Just like George！ GRRR！ Great minds think alike!"'},
                {"child":'不说话',"parent":'"Me — I\'d go as Daddy Pig. With a big tummy and glasses. Very realistic!"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"Have you ever worn a costume or dressed up?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说过',"parent":'"What did you wear？ Did anyone recognise you？"'},
                {"child":'摇头',"parent":'"Never dressed up？ Let\'s plan one RIGHT NOW！ What would you be？"'},
                {"child":'笑了',"parent":'"Did you say GRRR like George？ Was your costume scary？"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"What\'s the cleverest costume you\'ve ever seen?"'],
            "rows":[
                {"child":'说某个服装',"parent":'"[Costume]！ What a brilliant idea！ Did they make it or buy it？"'},
                {"child":'说不知道',"parent":'"George\'s dinosaur is pretty brilliant! Simple but perfect!"'},
                {"child":'笑了',"parent":'"The most surprising costume is always the one you don\'t expect!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Welcome to the fancy dress party！ Who are you dressed up as？"'],
            "rows":[
                {"child":'做角色',"parent":'"[Character]！ Brilliant costume！ What\'s your character\'s special move？"'},
                {"child":'说恐龙',"parent":'"GRRR！ A dinosaur！ Like George！ GRRR back at you！"'},
                {"child":'说中文',"parent":'家长扮派对主持人："What are YOU dressed as？ Tell me！"'},
            ],
        },
        "recast":[
            {"term":'fancy dress',"explanation":'"Fancy dress = 化装服。 Not fancy clothes, but COSTUMES!"'},
            {"term":"I didn't recognise you","explanation":'"Recognise = 认出。 I didn\'t recognise you = 我没认出你来！"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Dressed up as a pirate！ Ahoy！" — 海盗姿态',
            '"Dressed up as a witch！ Cackle！" — 假装拿扫帚飞',
            '"I didn\'t recognise you！" — 夸张后退，惊讶',
            '"What a brilliant costume！" — 指向对方，竖大拇指',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Peppa 到达派对',"L1":'L1: "Party！ Costumes！"',"L2":'L2: "Welcome to the fancy dress party！"',"L3":'L3: "Look at everyone\'s costumes! What are you dressed up as? I\'m a fairy princess!"'},
            {"scene":'George 的恐龙服装',"L1":'L1: "Dinosaur！ GRRR！"',"L2":'L2: "George is dressed up as a dinosaur！"',"L3":'L3: "GRRR！ It\'s George！ He\'s dressed up as a dinosaur — of course！ What a brilliant costume!"'},
            {"scene":'认出乔装的人',"L1":'L1: "I see you！"',"L2":'L2: "I recognise you — you\'re [name]！"',"L3":'L3: "Wait! I didn\'t recognise you at first! What a brilliant disguise! But now I know it\'s you!"'},
        ],
        },
        "bugs":{
            "rule":'说 "fancy dress" 得1分；说 "I didn\'t recognise you" 得2分；说 "brilliant" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'fancy dress → costume → pirate → witch → recognise → brilliant'},
            {"level":'L2 (句)',"text":'Peppa and friends had a fancy dress party. Everyone wore costumes. George wore a dinosaur costume.'},
            {"level":'L3 (完整)',"text":'It was a fancy dress party！ Everyone came in brilliant costumes. There was an astronaut, a pirate, a witch, a princess. And George? He came as a DINOSAUR！ GRRR！ Of course! It was the most perfect costume at the party. Nobody was surprised — everyone knew how much George loves dinosaurs!'},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ise/ize → /aɪz/ 音',
            "examples":['disguise', 'recognise', 'surprise', 'realise', 'prize'],
            "tongue_tip":'结尾 -ise 发 /aɪz/。"What a surprise! I didn\'t recognise you in that disguise!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP39 The Museum（博物馆）——" 故意停顿制造悬念',
        "next_a":'EP39 The Museum',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'What are you dressed up as?',"zh":'你扮的是什么？',"usage":'化装游戏时'},
        {"sentence":"I didn't recognise you!","zh":'我没认出你！',"usage":'孩子换服装时'},
        {"sentence":'What a brilliant costume!',"zh":'真是个精彩的服装！',"usage":'夸任何创意'},
        {"sentence":"I'm dressed up as...","zh":'我扮的是...',"usage":'孩子介绍自己角色时'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 39 · The Museum 博物馆
# ═══════════════════════════════════════════════════════════════════════════════
EP39 = _ep(
    num=39, title_en='The Museum', title_zh='博物馆', color='purple',
    synopsis='全家去参观博物馆。博物馆里有很多关于历史的展品，包括一副真正的恐龙骨架！George 非常兴奋。Daddy 解释了各种展品，但总是说错。',
    vocab=[        {"word":'museum',"phonetic":'mjuːˈziːəm',"pos":'n.',"zh":'博物馆',"action":'做出参观、四处张望的样子'},        {"word":'exhibit',"phonetic":'ɪɡˈzɪbɪt',"pos":'n.',"zh":'展品',"action":'指向想象的展柜，"An exhibit！"'},        {"word":'skeleton',"phonetic":'ˈskelɪtən',"pos":'n.',"zh":'骨架',"action":'身体歪歪扭扭，"Bones！ Skeleton！"'},        {"word":'ancient',"phonetic":'ˈeɪnʃənt',"pos":'adj.',"zh":'古老的',"action":'手抚摸想象的古老东西，"Ancient..."'},        {"word":'gallery',"phonetic":'ˈɡæləri',"pos":'n.',"zh":'画廊、展览馆',"action":'做出欣赏画的姿态'},        {"word":'fascinating',"phonetic":'ˈfæsɪneɪtɪŋ',"pos":'adj.',"zh":'令人着迷的',"action":'眼神发光，"Fascinating！ So interesting！"'},        {"word":'whisper',"phonetic":'ˈwɪspə',"pos":'v.',"zh":'低声说',"action":'凑近耳边，用耳语声说话'},        {"word":'enormous',"phonetic":'ɪˈnɔːməs',"pos":'adj.',"zh":'巨大的',"action":'双手向外展开，"Enormous！ HUGE！"'},    ],
    patterns=[        {"pattern":'This is a museum.',"zh":'这是一个博物馆',"example":'In a museum, you can see many things from the past.'},        {"pattern":"Please don't touch the exhibits.","zh":'请不要触碰展品',"example":"In a museum, please don't touch things!"},        {"pattern":"That's an enormous dinosaur skeleton!","zh":'那是一副巨大的恐龙骨架！',"example":'What an enormous dinosaur!'},        {"pattern":'Fascinating! I find this fascinating.',"zh":'太迷人了！',"example":'This is absolutely fascinating!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第38集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🏛️',"bg":'purple',"trigger":'到达博物馆，肃静',"action":'故意压低声音，"We\'re in a museum！ Whisper!"'},
            {"emoji":'🦕',"bg":'green',"trigger":'恐龙骨架展览',"action":'张开双臂，"ENORMOUS！ A dinosaur skeleton！"'},
            {"emoji":'🎨',"bg":'blue',"trigger":'参观其他展品',"action":'做出欣赏艺术品的样子'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What was George\'s favourite thing in the museum?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说恐龙骨架',"parent":'"YES！ The dinosaur skeleton！ ENORMOUS！ George couldn\'t believe it!"'},
                {"child":'说其他',"parent":'"George loves dinosaurs — so the HUGE dinosaur skeleton was his favourite!"'},
                {"child":'不说话',"parent":'张开双臂，"ENORMOUS！ A skeleton made of bones! George\'s favourite animal!"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What are the rules in a museum?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说不能碰/小声',"parent":'"Don\'t touch the exhibits！ And whisper！ Museums are quiet places!"'},
                {"child":'说不知道',"parent":'"Please don\'t touch the exhibits! And speak quietly!"'},
                {"child":'不说话',"parent":'假装伸手去触碰，然后摇头，"In a museum... No!"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you could put ONE thing in a museum, what would it be?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说物品',"parent":'"A [item]！ In a museum! People would come to look at it!"'},
                {"child":'说玩具/书',"parent":'"[Item]！ Future children would find it fascinating!"'},
                {"child":'不说话',"parent":'"Me — I\'d put in Daddy Pig\'s enormous belly. It\'s truly a museum piece!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever been to a museum? What did you like best?"'],
            "rows":[
                {"child":'说去过',"parent":'"What was the most fascinating thing？ Did you find anything enormous？"'},
                {"child":'摇头',"parent":'"Never？ We should go！ Imagine seeing a real dinosaur skeleton!"'},
                {"child":'笑了',"parent":'"In a museum, you have to whisper! That\'s very hard for Daddy Pig!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Welcome to the museum！ Please don\'t touch anything! What would you like to see？"'],
            "rows":[
                {"child":'说展品',"parent":'"This way please！ The [exhibit] is just over here！"'},
                {"child":'说恐龙',"parent":'"The dinosaur gallery！ And there\'s an ENORMOUS skeleton！ Follow me!"'},
                {"child":'说中文',"parent":'家长扮导游："Whisper please！ This is the ancient exhibit!"'},
            ],
        },
        "recast":[
            {"term":'enormous',"explanation":'"Enormous = 巨大的。 Bigger than big! ENORMOUS！"'},
            {"term":'fascinating',"explanation":'"Fascinating = 令人着迷的。 I find this absolutely fascinating!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Shhh！ Whisper in the museum！" — 食指放嘴唇',
            '"Don\'t touch the exhibits！" — 摆手，严肃',
            '"ENORMOUS！" — 双臂展开尽可能宽',
            '"Fascinating！" — 眼神发光，靠近感兴趣的东西',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'进入博物馆',"L1":'L1: "Museum！ Quiet！"',"L2":'L2: "We\'re in the museum！ Please whisper！"',"L3":'L3: "Welcome to the museum! Please don\'t touch the exhibits and please speak quietly!"'},
            {"scene":'George 看到恐龙骨架',"L1":'L1: "Dinosaur！ HUGE！"',"L2":'L2: "An enormous dinosaur skeleton！"',"L3":'L3: "GRRR！ George loves it! That enormous skeleton is the most fascinating thing here!"'},
            {"scene":'Daddy 解释展品',"L1":'L1: "Ancient！ Old！"',"L2":'L2: "This exhibit is very old — ancient！"',"L3":'L3: "This fascinating exhibit is from ancient times! I find it absolutely fascinating!"'},
        ],
        },
        "bugs":{
            "rule":'说 "enormous" 得2分；说 "fascinating" 得2分；说 "don\'t touch" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'museum → exhibit → skeleton → ancient → enormous → fascinating → whisper'},
            {"level":'L2 (句)',"text":'The family went to the museum. They saw many exhibits. George loved the enormous dinosaur skeleton.'},
            {"level":'L3 (完整)',"text":"The Pig family visited the museum! There were fascinating exhibits everywhere. Daddy explained everything — though not always correctly! The highlight for George was the ENORMOUS dinosaur skeleton. He couldn't believe how big it was! In museums, you must whisper and not touch the exhibits. George was very good at following those rules."},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 eum → /ɪəm/ 音结尾',
            "examples":['museum', 'aquarium', 'gymnasium', 'stadium'],
            "tongue_tip":'结尾 -eum/-ium 发 /ɪəm/，轻声结尾。"The museum has an aquarium!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP40 Very Hot Day（很热的一天）——" 故意停顿制造悬念',
        "next_a":'EP40 Very Hot Day',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"Please don't touch the exhibits.","zh":'请不要触碰展品',"usage":'教孩子博物馆规则'},
        {"sentence":'Fascinating!',"zh":'令人着迷的！',"usage":'孩子发现有趣的东西时'},
        {"sentence":"That's enormous!","zh":'那太巨大了！',"usage":'形容任何很大的东西'},
        {"sentence":'In a museum, you must whisper.',"zh":'在博物馆要低声说话',"usage":'规则教育的轻松方式'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 40 · Very Hot Day 很热的一天
# ═══════════════════════════════════════════════════════════════════════════════
EP40 = _ep(
    num=40, title_en='Very Hot Day', title_zh='很热的一天', color='red',
    synopsis='天气超级热！全家人想尽办法降温：风扇、冰淇淋、喷水玩……最后 Daddy 决定用花园水管给大家降温，结果大家全都湿透了，但很开心！',
    vocab=[        {"word":'hot',"phonetic":'hɒt',"pos":'adj.',"zh":'热的',"action":'用手扇自己，"So hot！ Phew!"'},        {"word":'cool down',"phonetic":'kuːl daʊn',"pos":'v.ph.',"zh":'降温',"action":'假装凉快下来，"Ahhh！ Cool!"'},        {"word":'fan',"phonetic":'fæn',"pos":'n.',"zh":'风扇',"action":'假装电风扇吹来，头发飘动'},        {"word":'ice cream',"phonetic":'aɪs kriːm',"pos":'n.',"zh":'冰淇淋',"action":'假装舔冰淇淋，"Mmm！ Ice cream！"'},        {"word":'shade',"phonetic":'ʃeɪd',"pos":'n.',"zh":'阴凉处',"action":'走到想象的树荫下，"Ahh! Shade！"'},        {"word":'sprinkler',"phonetic":'ˈsprɪŋklə',"pos":'n.',"zh":'喷水器',"action":'做出转圈喷水的动作'},        {"word":'sizzling',"phonetic":'ˈsɪzlɪŋ',"pos":'adj.',"zh":'炽热的',"action":'咝咝声，"Sizzling hot！ Like a frying pan！"'},        {"word":'refresh',"phonetic":'rɪˈfreʃ',"pos":'v.',"zh":'使清爽',"action":'假装喝冷水，"Refreshing！ Ahhh!"'},    ],
    patterns=[        {"pattern":"It's very hot today.","zh":'今天非常热',"example":"It's very cold today. It's very hot!"},        {"pattern":'We need to cool down.',"zh":'我们需要降温',"example":"Let's find some shade and cool down!"},        {"pattern":'What a sizzling hot day!',"zh":'多热的天啊！',"example":'What a scorching, sizzling hot day!'},        {"pattern":'Ice cream will cool us down.',"zh":'冰淇淋能让我们凉快',"example":'A cold drink will cool you down!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第39集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'☀️',"bg":'red',"trigger":'超热的天气，大家在喘气',"action":'用手扇自己，"Phew！ So hot！"'},
            {"emoji":'🍦',"bg":'yellow',"trigger":'吃冰淇淋降温',"action":'假装舔冰淇淋，"Mmm！ Cold!"'},
            {"emoji":'💧',"bg":'blue',"trigger":'花园水管喷水降温',"action":'被水淋到，全身颤抖，"Cold！ But refreshing！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"How did the family cool down on the very hot day?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说冰淇淋/水管',"parent":'"Ice cream! And the garden hose! SPLASH! Cold water everywhere!"'},
                {"child":'说不知道',"parent":'"They tried a fan first... then ice cream... then the garden hose!"'},
                {"child":'不说话',"parent":'假装舔冰淇淋，然后被水管喷到，"SPLASH！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Did everyone get wet at the end?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Yes! All wet!"',"parent":'"YES！ Daddy\'s hose sprayed everyone! Wet and happy!"'},
                {"child":'说不确定',"parent":'"The garden hose went everywhere! SPLASH! Soaking wet but cool!"'},
                {"child":'不说话',"parent":'做出被喷到的动作，"AH！ Cold！ But... so refreshing!"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"On a very hot day, what is YOUR best way to cool down?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说冰淇淋/冷饮',"parent":'"Ice cream！ The best！ What flavour?"'},
                {"child":'说游泳/水',"parent":'"Swimming！ Or a garden hose like Daddy！ SPLASH!"'},
                {"child":'不说话',"parent":'"Me — ice lolly! Or a cold bath. Or... staying indoors with a fan!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"What\'s the hottest day you can remember? What did you do?"'],
            "rows":[
                {"child":'说经历',"parent":'"How hot was it？ Like today in the show？ Sizzling?"'},
                {"child":'说不记得',"parent":'"Was there a day when you just couldn\'t cool down?"'},
                {"child":'笑了',"parent":'"Did you find shade? Did you eat ice cream? Were you sizzling?"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Phew！ It\'s SO hot today！ What shall we do to cool down？"'],
            "rows":[
                {"child":'说冰淇淋',"parent":'"Ice cream！ Yes！ But we\'ll need to eat it fast before it melts!"'},
                {"child":'说水/游泳',"parent":'"Let\'s get the hose! Ready？" 假装拿水管 "SPRAY!"'},
                {"child":'说中文',"parent":'家长扮 Mummy Pig："This heat is unbearable! We NEED to cool down！"'},
            ],
        },
        "recast":[
            {"term":'cool down',"explanation":'"Cool down = 降温，冷静下来。 物理上冷（hot day）和情绪上冷（calm down）都可用"'},
            {"term":'sizzling',"explanation":'"Sizzling = 发出滋滋声（如煎肉）→ 引申为炽热的"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Phew！ It\'s so hot！" — 用手扇自己，擦汗',
            '"Ice cream！ Cool down！" — 假装舔冰淇淋，叹一口气',
            '"SPLASH！ Cold water！" — 假装被水淋到，颤抖',
            '"Ahh！ Refreshing！" — 凉快下来，放松',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'超热天气',"L1":'L1: "Hot！ Phew！"',"L2":'L2: "What a very hot day！"',"L3":'L3: "Phew! It\'s sizzling today! We need to do something to cool down!"'},
            {"scene":'吃冰淇淋',"L1":'L1: "Ice cream！ Cold！"',"L2":'L2: "Ice cream will cool us down！"',"L3":'L3: "Ice cream! Cold and refreshing! This is exactly what we need on a hot day!"'},
            {"scene":'水管喷大家',"L1":'L1: "Wet！ Cold！"',"L2":'L2: "The hose splashed everyone！"',"L3":'L3: "SPLASH! Oh no! But... it\'s so refreshing! Cold water! Everyone\'s cool now!"'},
        ],
        },
        "bugs":{
            "rule":'说 "cool down" 得2分；说 "sizzling" 得2分；说 "refreshing" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'hot → cool down → ice cream → fan → shade → hose → sizzling → refreshing'},
            {"level":'L2 (句)',"text":'It was a very hot day. The family needed to cool down. They ate ice cream. Daddy used the hose. Everyone got wet.'},
            {"level":'L3 (完整)',"text":'It was a sizzling hot summer day! The Pig family tried everything to cool down. First a fan — too slow! Then ice cream — delicious but not enough! Finally Daddy got the garden hose... and sprayed EVERYONE! SPLASH! Cold and wet and refreshing! The best way to cool down!'},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 oo → /uː/ 长音',
            "examples":['cool', 'pool', 'moon', 'school', 'too'],
            "tongue_tip":'嘴唇向前圆成O形，发 /uː/ 持续音。"Cool pool! School is cool too!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP41 Chloé\'s Puppet Show（Chloé 的木偶剧）——" 故意停顿制造悬念',
        "next_a":"EP41 Chloé's Puppet Show",
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'What a sizzling hot day!',"zh":'多热的天啊！',"usage":'夏天的情绪表达'},
        {"sentence":'We need to cool down!',"zh":'我们需要降温！',"usage":'热天的行动号令'},
        {"sentence":'Ice cream will cool us down.',"zh":'冰淇淋能让我们凉快',"usage":'行动建议'},
        {"sentence":"Phew！ It's so hot！","zh":'哇，好热啊！',"usage":'日常热天感叹'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 41 · Chloé's Puppet Show Chloé 的木偶剧
# ═══════════════════════════════════════════════════════════════════════════════
EP41 = _ep(
    num=41, title_en="Chloé's Puppet Show", title_zh='Chloé 的木偶剧', color='purple',
    synopsis='表姐 Chloé 来表演木偶剧！她准备了精心的木偶节目，但 Peppa 和 George 不停打扰。最后小家伙们反而成了最受欢迎的演员。',
    vocab=[        {"word":'puppet',"phonetic":'ˈpʌpɪt',"pos":'n.',"zh":'木偶',"action":'手做木偶动作'},        {"word":'show',"phonetic":'ʃəʊ',"pos":'n.',"zh":'演出',"action":'张开双臂，"Show time！"'},        {"word":'performance',"phonetic":'pəˈfɔːməns',"pos":'n.',"zh":'表演',"action":'鞠躬，"What a performance!"'},        {"word":'audience',"phonetic":'ˈɔːdiəns',"pos":'n.',"zh":'观众',"action":'指向前方，"The audience watches!"'},        {"word":'stage',"phonetic":'steɪdʒ',"pos":'n.',"zh":'舞台',"action":'踩上想象的台，"On stage！"'},        {"word":'rehearsal',"phonetic":'rɪˈhɜːsl',"pos":'n.',"zh":'排练',"action":'认真做动作，"Rehearsal!"'},        {"word":'character',"phonetic":'ˈkærɪktə',"pos":'n.',"zh":'角色',"action":'指自己，"I\'m playing this character!"'},        {"word":'curtain',"phonetic":'ˈkɜːtn',"pos":'n.',"zh":'幕布',"action":'做拉开窗帘动作，"And the curtain rises!"'},    ],
    patterns=[        {"pattern":'Ladies and gentlemen, welcome to the show!',"zh":'女士们先生们，欢迎来看表演！',"example":'Ladies and gentlemen — the show begins!'},        {"pattern":'The show must go on.',"zh":'演出必须继续',"example":'No matter what happens, the show goes on!'},        {"pattern":'Take a bow!',"zh":'谢幕！',"example":'Everyone take a bow!'},        {"pattern":'What a wonderful performance!',"zh":'多精彩的表演啊！',"example":'What a brilliant show!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第40集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🎭',"bg":'purple',"trigger":'Chloé 准备木偶剧',"action":'做木偶动作'},
            {"emoji":'👥',"bg":'blue',"trigger":'观众就座',"action":'假装坐进观众席'},
            {"emoji":'🌟',"bg":'gold',"trigger":'演出大成功',"action":'鼓掌，"Bravo！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What was Chloé putting on?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"A puppet show!"',"parent":'"YES！ A puppet show！ With characters and a stage！"'},
                {"child":'说不知道',"parent":'"A puppet show! Chloé was the director!"'},
                {"child":'不说话',"parent":'做木偶动作，"What is Chloé doing？"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Did the show go well?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Yes!"',"parent":'"Despite the chaos, yes! The show went on！"'},
                {"child":'说不知道',"parent":'"It was a bit chaotic... but the show must go on!"'},
                {"child":'不说话',"parent":'"Ladies and gentlemen... the show was a...?"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you put on a show, what story would you perform?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说故事',"parent":'"[Story]！ You\'d be the director AND the star！"'},
                {"child":'说不知道',"parent":'"Any story！ A princess？ A dragon？ A funny pig?"'},
                {"child":'不说话',"parent":'"I\'d do the story of George and the dinosaur!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever put on a show or performance?"'],
            "rows":[
                {"child":'说过',"parent":'"Were you nervous？ Did you take a bow？"'},
                {"child":'摇头',"parent":'"Let\'s put on a show！ Right now！"'},
                {"child":'笑了',"parent":'"The show must go on — even when things go wrong!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Ladies and gentlemen! Welcome to our show！"'],
            "rows":[
                {"child":'配合',"parent":'"What\'s the show about？ Who are the characters？"'},
                {"child":'做动作',"parent":'"Take a bow! Bravo！"'},
                {"child":'说中文',"parent":'家长扮 Chloé："Take your places！ The show is about to begin！"'},
            ],
        },
        "recast":[
            {"term":'The show must go on',"explanation":'"Must go on = 必须继续。 No matter what happens!"'},
            {"term":'take a bow',"explanation":'"Take a bow = 谢幕（向观众鞠躬）"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Ladies and gentlemen！" — 做出宣告姿势',
            '"Take a bow！" — 鞠躬',
            '"Bravo！" — 鼓掌',
            '"The curtain rises！" — 做拉幕布动作',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Chloé 宣布表演',"L1":'L1: "Show time！"',"L2":'L2: "Ladies and gentlemen，welcome！"',"L3":'L3: "Ladies and gentlemen! Welcome to Chloé\'s Puppet Show! The curtain rises!"'},
            {"scene":'演出',"L1":'L1: "Characters！"',"L2":'L2: "The puppets are performing！"',"L3":'L3: "Watch the puppets! Each character has their own voice and personality!"'},
            {"scene":'谢幕',"L1":'L1: "Bravo！"',"L2":'L2: "Take a bow！"',"L3":'L3: "What a wonderful performance! Take a bow, everyone！"'},
        ],
        },
        "bugs":{
            "rule":'说 "take a bow" 得2分；说 "the show must go on" 得3分；说 "Bravo" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'puppet → show → stage → audience → bow → curtain → bravo'},
            {"level":'L2 (句)',"text":'Chloé put on a puppet show. Everyone watched. They took a bow at the end.'},
            {"level":'L3 (完整)',"text":'Cousin Chloé prepared an amazing puppet show! She had characters, a stage, and a proper curtain. But Peppa and George kept interrupting! Yet the show must go on — and in the end, everyone loved it. Bravo, Chloé!'},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ow → /əʊ/ 或 /aʊ/ （语境区分）',
            "examples":['show', 'bow (谢幕)', 'cow', 'now', 'flow'],
            "tongue_tip":'show /əʊ/，bow when curtain falls /baʊ/，bow in hair /bəʊ/。Context decides!',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP42 Daddy Gets Fit（爸爸减肥）——" 故意停顿制造悬念',
        "next_a":'EP42 Daddy Gets Fit',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Ladies and gentlemen, welcome!',"zh":'女士们先生们，欢迎！',"usage":'任何活动的开场白'},
        {"sentence":'The show must go on.',"zh":'演出必须继续',"usage":'困难时的激励'},
        {"sentence":'Take a bow!',"zh":'谢幕！',"usage":'完成任何任务后'},
        {"sentence":'What a wonderful performance!',"zh":'多精彩的表演！',"usage":'夸奖孩子'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 42 · Daddy Gets Fit 爸爸减肥
# ═══════════════════════════════════════════════════════════════════════════════
EP42 = _ep(
    num=42, title_en='Daddy Gets Fit', title_zh='爸爸减肥', color='orange',
    synopsis='Dr Brown Bear 建议 Daddy Pig 多锻炼。Daddy 决定开始跑步、骑车、做操。但每次都累到气喘吁吁。最后 Daddy 发现跑步其实很难，但没有放弃。',
    vocab=[        {"word":'exercise',"phonetic":'ˈeksəsaɪz',"pos":'n./v.',"zh":'锻炼',"action":'做运动动作，"Exercise！ Move！"'},        {"word":'fit',"phonetic":'fɪt',"pos":'adj.',"zh":'健康的、强壮的',"action":'拍肌肉，"Fit！ Strong!"'},        {"word":'jogging',"phonetic":'ˈdʒɒɡɪŋ',"pos":'n.',"zh":'慢跑',"action":'原地小跑，"Jogging！"'},        {"word":'breathless',"phonetic":'ˈbreθləs',"pos":'adj.',"zh":'上气不接下气',"action":'喘气，"Breathless！ Out of breath！"'},        {"word":'healthy',"phonetic":'ˈhelθi',"pos":'adj.',"zh":'健康的',"action":'竖大拇指，"Healthy！ Good for you!"'},        {"word":'cycling',"phonetic":'ˈsaɪklɪŋ',"pos":'n.',"zh":'骑自行车',"action":'假装踩踏板，"Cycling！"'},        {"word":'effort',"phonetic":'ˈefət',"pos":'n.',"zh":'努力',"action":'做用力的样子，"Great effort！"'},        {"word":'encourage',"phonetic":'ɪnˈkʌrɪdʒ',"pos":'v.',"zh":'鼓励',"action":'做出鼓励手势，"You can do it！"'},    ],
    patterns=[        {"pattern":'Daddy needs more exercise.',"zh":'爸爸需要多锻炼',"example":"You need more exercise — let's go for a walk!"},        {"pattern":"I'm fit as a fiddle!","zh":'我健壮得很！',"example":"I'm fit! Ready for anything!"},        {"pattern":"Keep going! Don't give up!","zh":'继续！不要放弃！',"example":"You're almost there! Keep going!"},        {"pattern":'Exercise is good for you.',"zh":'锻炼对你有好处',"example":'Vegetables and exercise are good for you!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第41集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🏃',"bg":'orange',"trigger":'Daddy 开始慢跑',"action":'原地小跑，"Jogging！ Very healthy！"'},
            {"emoji":'😤',"bg":'red',"trigger":'Daddy 气喘吁吁',"action":'喘气，扶膝盖，"So... breathless..."'},
            {"emoji":'💪',"bg":'yellow',"trigger":'孩子们鼓励 Daddy',"action":'"Keep going！ You can do it！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Why did Daddy Pig start exercising?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说医生建议',"parent":'"Dr Brown Bear said Daddy needed more exercise！ So he started jogging!"'},
                {"child":'说不知道',"parent":'"Dr Brown Bear suggested Daddy needed to get fit!"'},
                {"child":'不说话',"parent":'假装医生，"You need more exercise！ Jogging！ Cycling！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Was Daddy fit and fast at jogging?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'笑着说不',"parent":'"NOT at first！ He was breathless very quickly! But he kept going!"'},
                {"child":'说是',"parent":'"He said he was fit as a fiddle... but he was quite breathless!"'},
                {"child":'不说话',"parent":'假装跑步，越来越慢，越来越喘'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"What exercise do YOU like doing?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说运动',"parent":'"[Sport]！ Good choice！ Does it make you breathless?"'},
                {"child":'说不喜欢运动',"parent":'"Like Daddy！ But exercise is good for you — even small amounts!"'},
                {"child":'不说话',"parent":'"Me — I like swimming. What about you?"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Has a doctor ever told you or someone in your family to do more exercise?"'],
            "rows":[
                {"child":'说过',"parent":'"Like Daddy！ Did they do it？ Was it hard?"'},
                {"child":'摇头',"parent":'"Lucky! But exercise keeps you fit and healthy!"'},
                {"child":'笑了',"parent":'"Daddy said he was fit as a fiddle... then got very breathless!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Right！ Time for exercise！ Let\'s jog！ Ready？"'],
            "rows":[
                {"child":'跑起来',"parent":'"Great！ Keep going！ Don\'t give up！ You\'re fit！"'},
                {"child":'气喘',"parent":'"Breathless！ But you\'re doing so well！ Exercise is good for you！"'},
                {"child":'说中文',"parent":'家长扮 Dr Brown Bear："You need more exercise, Daddy Pig!"'},
            ],
        },
        "recast":[
            {"term":'fit as a fiddle',"explanation":'"Fit as a fiddle = 身体非常健壮（fiddle = 小提琴）"'},
            {"term":'breathless',"explanation":'"Breathless = 上气不接下气。 Out of breath!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Jog！ Jog！ Jog！" — 原地小跑',
            '"Keep going！ Don\'t stop！" — 做鼓励手势',
            '"Breathless！" — 喘气，扶膝盖',
            '"Fit！ Strong！" — 拍肌肉',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Doctor 建议运动',"L1":'L1: "Exercise！"',"L2":'L2: "Daddy needs more exercise！"',"L3":'L3: "Dr Brown Bear said: Daddy Pig, you need to get fit! More exercise!"'},
            {"scene":'Daddy 开始慢跑',"L1":'L1: "Jogging！"',"L2":'L2: "I\'m going jogging！ I\'m fit！"',"L3":'L3: "I\'m fit as a fiddle! Watch me jog! One, two, one, two..."'},
            {"scene":'Daddy 气喘吁吁',"L1":'L1: "Breathless！"',"L2":'L2: "Daddy is very breathless！"',"L3":'L3: "I\'m... very... breathless... But exercise is... good for you..."'},
        ],
        },
        "bugs":{
            "rule":'说 "fit as a fiddle" 得3分；说 "breathless" 得1分；说 "keep going" 得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'exercise → fit → jogging → breathless → healthy → cycling → encourage'},
            {"level":'L2 (句)',"text":'Daddy needed more exercise. He went jogging. He was very breathless. But he kept going.'},
            {"level":'L3 (完整)',"text":"Dr Brown Bear told Daddy Pig he needed more exercise. So Daddy started jogging! He said he was fit as a fiddle. But he got breathless very quickly! Peppa and George encouraged him: keep going, Daddy! And Daddy kept going. Exercise is hard, but Daddy didn't give up!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ise → /aɪz/ 音',
            "examples":['exercise', 'surprise', 'realise', 'advertise', 'comprise'],
            "tongue_tip":'结尾 -ise 发 /aɪz/。"I realise I need to exercise!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP43 Tidying Up（整理房间）——" 故意停顿制造悬念',
        "next_a":'EP43 Tidying Up',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Daddy needs more exercise.',"zh":'爸爸需要多锻炼',"usage":'真实场景的幽默版'},
        {"sentence":"Keep going！ Don't give up！","zh":'继续！不要放弃！',"usage":'鼓励任何坚持中的人'},
        {"sentence":"I'm fit as a fiddle!","zh":'我健壮得很！',"usage":'自嘲或真心鼓励'},
        {"sentence":'Exercise is good for you.',"zh":'锻炼对你有好处',"usage":'健康教育的基本句'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 43 · Tidying Up 整理房间
# ═══════════════════════════════════════════════════════════════════════════════
EP43 = _ep(
    num=43, title_en='Tidying Up', title_zh='整理房间', color='pink',
    synopsis='Mummy Pig 叫 Peppa 整理自己的玩具房间。Peppa 找到了各种久违的玩具，玩得不亦乐乎，却忘记了要整理。最后大家一起帮忙整理。',
    vocab=[        {"word":'tidy',"phonetic":'ˈtaɪdi',"pos":'v./adj.',"zh":'整理/整洁的',"action":'整理想象的乱东西，"Tidy up！"'},        {"word":'messy',"phonetic":'ˈmesi',"pos":'adj.',"zh":'乱的',"action":'双手摊开，"Messy！ Such a mess！"'},        {"word":'put away',"phonetic":'pʊt əˈweɪ',"pos":'v.ph.',"zh":'收好、放好',"action":'做收纳手势，"Put it away！"'},        {"word":'sort',"phonetic":'sɔːt',"pos":'v.',"zh":'分类整理',"action":'把东西分成堆，"Sort it out！"'},        {"word":'cupboard',"phonetic":'ˈkʌbəd',"pos":'n.',"zh":'橱柜',"action":'做打开柜门的动作'},        {"word":'drawer',"phonetic":'drɔː',"pos":'n.',"zh":'抽屉',"action":'做拉开抽屉的动作'},        {"word":'belong',"phonetic":'bɪˈlɒŋ',"pos":'v.',"zh":'属于、归位',"action":'指某处，"This belongs here!"'},        {"word":'discovered',"phonetic":'dɪˈskʌvəd',"pos":'v.',"zh":'发现了（已久遗忘的东西）',"action":'惊喜表情，"I discovered it！"'},    ],
    patterns=[        {"pattern":'Tidy up your toys, please.',"zh":'请整理你的玩具',"example":'Tidy up! Put your things away!'},        {"pattern":'Everything has its place.',"zh":'每样东西都有它的地方',"example":'This goes here. That goes there. Everything has its place.'},        {"pattern":"I'd forgotten all about that toy!","zh":'我完全忘了这个玩具！',"example":"I'd forgotten this even existed!"},        {"pattern":"Let's sort it out together.","zh":'我们一起整理吧',"example":"Let's sort it all out together!"},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第42集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🧸',"bg":'pink',"trigger":'Peppa 找到久违的玩具',"action":'做惊喜发现的样子'},
            {"emoji":'📦',"bg":'blue',"trigger":'整理玩具到收纳箱',"action":'做分类收纳动作'},
            {"emoji":'😊',"bg":'green',"trigger":'房间整理好了',"action":'双手展示整洁的空间'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Why wasn\'t Peppa tidying her room?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说玩玩具了',"parent":'"She kept finding toys and playing with them instead of putting them away!"'},
                {"child":'说忘了',"parent":'"She got distracted！ Every toy she found, she wanted to play with!"'},
                {"child":'不说话',"parent":'假装找到玩具，立刻开始玩，"Ooh！ This one！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Did the room get tidy in the end?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Yes!"',"parent":'"YES！ With everyone helping！ Together it was much faster!"'},
                {"child":'说不确定',"parent":'"Eventually yes! Everyone helped and it was sorted out!"'},
                {"child":'不说话',"parent":'做出整洁房间的手势，"Everything in its place!"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"Is your room tidy right now?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说很整洁',"parent":'"Wow！ Very organised！ Everything in its place?"'},
                {"child":'说很乱',"parent":'"Like Peppa\'s! Let\'s sort it out together！ What\'s the messiest part?"'},
                {"child":'不说话',"parent":'"If I opened your bedroom door right now... what would I see?"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever found an old toy you\'d forgotten about?"'],
            "rows":[
                {"child":'说有',"parent":'"Like Peppa！ What was it？ Did you stop tidying to play with it?"'},
                {"child":'摇头',"parent":'"Never? Your toys are all well remembered! Very organised!"'},
                {"child":'笑了',"parent":'"Finding an old toy is like finding treasure!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Peppa, it\'s time to tidy your room！ Put everything in its place！"'],
            "rows":[
                {"child":'假装整理',"parent":'"Good! But wait — don\'t play with that! Put it AWAY！"'},
                {"child":'拿起玩具玩',"parent":'"Peppa！ That goes in the box！ Not time to play!"'},
                {"child":'说中文',"parent":'家长扮 Mummy："Tidy up, Peppa! Everything has its place！"'},
            ],
        },
        "recast":[
            {"term":'put away',"explanation":'"Put away = 放好，归位。 Put your toys away = 把玩具收好"'},
            {"term":'everything has its place',"explanation":'"Every thing has its place = 每样东西都有它归位的地方"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Tidy up！" — 做收拾动作',
            '"Put it away！" — 把东西放进想象的盒子',
            '"Messy！ Such a mess！" — 双手摊开，皱眉',
            '"All done！ Tidy！" — 双手展示整洁',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Mummy 叫整理',"L1":'L1: "Tidy！"',"L2":'L2: "Tidy up your room please, Peppa！"',"L3":'L3: "Peppa！ Your room is very messy！ Please put all your toys away!"'},
            {"scene":'Peppa 发现旧玩具',"L1":'L1: "Found it！"',"L2":'L2: "I\'d forgotten about this toy！"',"L3":'L3: "Oh！ My old bear! I\'d forgotten all about him! He goes... wait, I\'ll just play for a minute..."'},
            {"scene":'大家一起整理',"L1":'L1: "Sort it！"',"L2":'L2: "Let\'s sort it out together！"',"L3":'L3: "Everything has its place! Toys in the box, books on the shelf, all sorted!"'},
        ],
        },
        "bugs":{
            "rule":'说 "tidy" 得1分；说 "put away" 得1分；说 "everything has its place" 得3分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'tidy → messy → put away → sort → toys → discovered → together'},
            {"level":'L2 (句)',"text":'Mummy told Peppa to tidy her room. Peppa kept finding old toys and playing. In the end they tidied together.'},
            {"level":'L3 (完整)',"text":"Mummy Pig told Peppa to tidy her room — it was very messy! But every toy Peppa found, she wanted to play with. 'I'd forgotten all about this one!' Eventually Mummy helped. They sorted everything out together. Everything in its place — tidy at last!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 idy → /aɪdi/ 音',
            "examples":['tidy', 'tidy up', 'untidy', 'idyllic', 'tiny'],
            "tongue_tip":'"tidy" 中 i 发长音 /aɪ/，就像 "my"。"Tiny tidy mice tidied!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP44 The Playground（游乐场）——" 故意停顿制造悬念',
        "next_a":'EP44 The Playground',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Tidy up your toys please.',"zh":'请整理你的玩具',"usage":'每天都可以用'},
        {"sentence":'Everything has its place.',"zh":'每样东西都有它的地方',"usage":'整理东西时的哲学'},
        {"sentence":"I'd forgotten all about that!","zh":'我完全忘了这个！',"usage":'发现久违东西时'},
        {"sentence":"Let's sort it out together.","zh":'我们一起整理吧',"usage":'共同完成任务'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 44 · The Playground 游乐场
# ═══════════════════════════════════════════════════════════════════════════════
EP44 = _ep(
    num=44, title_en='The Playground', title_zh='游乐场', color='yellow',
    synopsis='Peppa 和朋友们在游乐场玩，有秋千、滑梯、跷跷板。大家轮流玩，Peppa 和 Danny Dog 一起玩跷跷板，最后大家都玩到精疲力竭为止。',
    vocab=[        {"word":'playground',"phonetic":'ˈpleɪɡraʊnd',"pos":'n.',"zh":'游乐场',"action":'双手展示，"The playground！"'},        {"word":'swing',"phonetic":'swɪŋ',"pos":'n./v.',"zh":'秋千/荡',"action":'假装坐秋千，身体前后摆动'},        {"word":'slide',"phonetic":'slaɪd',"pos":'n./v.',"zh":'滑梯/滑',"action":'做出从高处滑下的动作，"Wheee！"'},        {"word":'seesaw',"phonetic":'ˈsiːsɔː',"pos":'n.',"zh":'跷跷板',"action":'手掌做上下跷板动作，"Seesaw！ Up down！"'},        {"word":'take turns',"phonetic":'teɪk tɜːnz',"pos":'v.ph.',"zh":'轮流',"action":'指向不同人，"Your turn! My turn!"'},        {"word":'push',"phonetic":'pʊʃ',"pos":'v.',"zh":'推',"action":'做推的动作，"Push！ Higher!"'},        {"word":'wait',"phonetic":'weɪt',"pos":'v.',"zh":'等待',"action":'做等待手势，"Wait your turn!"'},        {"word":'wheee',"phonetic":'wiː',"pos":'interj.',"zh":'象声词（玩耍的欢呼）',"action":'滑下时欢呼，"Wheee！"'},    ],
    patterns=[        {"pattern":"Let's go to the playground!","zh":'我们去游乐场吧！',"example":"Let's go to the park! To the playground!"},        {"pattern":"It's my turn on the swing!","zh":'轮到我荡秋千了！',"example":"It's my turn! I'm next!"},        {"pattern":'Higher! Push me higher!',"zh":'更高！推我更高！',"example":'Swing higher! Push more!'},        {"pattern":'We all take turns.',"zh":'我们都要轮流',"example":'Wait your turn — we all take turns.'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第43集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'\U0001f6dd',"bg":'yellow',"trigger":'到达游乐场，大家冲向各种设施',"action":'兴奋奔跑状'},
            {"emoji":'🔄',"bg":'blue',"trigger":'学习轮流',"action":'"Your turn！ Now my turn！"'},
            {"emoji":'😄',"bg":'green',"trigger":'大家一起玩跷跷板',"action":'手掌做上下动作，"Up! Down!"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What did Peppa play on at the playground?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说秋千/滑梯/跷跷板',"parent":'"Swing, slide, seesaw！ Peppa loves the playground!"'},
                {"child":'说不知道',"parent":'"Swing！ Slide！ Seesaw！ All of them!"'},
                {"child":'不说话',"parent":'做出三种游乐设施动作，"Swing... slide... seesaw!"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Did everyone take turns nicely?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说是',"parent":'"YES！ They waited and took turns! Everyone got a go!"'},
                {"child":'说不一定',"parent":'"Sometimes it\'s hard to wait! But they tried to take turns!"'},
                {"child":'不说话',"parent":'"Your turn! My turn! Did they take turns?"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"What\'s your favourite thing to do at a playground?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说设施',"parent":'"[Equipment]！ Do you like to go high？ Or fast？ Or both？"'},
                {"child":'说秋千',"parent":'"The swing！ Higher and higher！ Push me higher！"'},
                {"child":'不说话',"parent":'"Me — the slide! Wheee！ What about you?"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"What\'s the best playground you\'ve ever been to?"'],
            "rows":[
                {"child":'说地方',"parent":'"What made it special？ Tall slide？ Special equipment？"'},
                {"child":'说学校',"parent":'"The school playground！ You\'re there every day！ Do you have a favourite spot?"'},
                {"child":'笑了',"parent":'"Wheee！ The sound of everyone sliding!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Welcome to the playground！ What shall we play on first？"'],
            "rows":[
                {"child":'说设施',"parent":'"[Equipment] first！ And then we\'ll take turns on the others!"'},
                {"child":'说秋千',"parent":'"Swing! OK！ I\'ll push you！ Ready？ Wheee！"'},
                {"child":'说中文',"parent":'家长扮友伴："My turn！ Now YOUR turn！ Take turns!"'},
            ],
        },
        "recast":[
            {"term":'take turns',"explanation":'"Take turns = 轮流。 Each person gets a fair go!"'},
            {"term":'seesaw',"explanation":'"Seesaw = 跷跷板。 See-saw, up and down!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Swing！ Higher！" — 假装荡秋千，越来越高',
            '"Wheee！" — 滑下来，挥手欢呼',
            '"Seesaw！ Up! Down!" — 手做上下动作',
            '"Take turns！ Wait！" — 做等待手势',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'到达游乐场',"L1":'L1: "Playground！"',"L2":'L2: "Let\'s go to the playground！"',"L3":'L3: "The playground！ Swing, slide, seesaw — I love it all!"'},
            {"scene":'荡秋千',"L1":'L1: "Swing！ Higher！"',"L2":'L2: "Push me higher！"',"L3":'L3: "Push me！ Higher! I want to go as high as the sky!"'},
            {"scene":'跷跷板',"L1":'L1: "Up! Down！"',"L2":'L2: "Seesaw！ Up and down！"',"L3":'L3: "I\'m up! Now you\'re up! Seesaw is the most fun when you take turns!"'},
        ],
        },
        "bugs":{
            "rule":'说 "take turns" 得2分；说 "Wheee！" 得1分；说 "higher" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'playground → swing → slide → seesaw → turns → push → wheee'},
            {"level":'L2 (句)',"text":'Peppa and friends went to the playground. They played on swings, slides, and seesaws. They took turns.'},
            {"level":'L3 (完整)',"text":"The friends went to the playground! There were swings, slides, and a seesaw. Peppa loved the swing — 'push me higher!' She went on the slide — wheee！ And the seesaw was great fun with friends! They all took turns and played until they were exhausted."},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ay/ai → /eɪ/ 长音',
            "examples":['play', 'wait', 'say', 'train', 'mail'],
            "tongue_tip":'"Play！ Wait your turn! The playground today!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP45 Daddy Puts up a Picture（爸爸挂画）——" 故意停顿制造悬念',
        "next_a":'EP45 Daddy Puts up a Picture',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"Let's go to the playground!","zh":'我们去游乐场吧！',"usage":'外出时的活动提议'},
        {"sentence":'Take turns！',"zh":'轮流！',"usage":'教孩子分享和等待'},
        {"sentence":'Push me higher!',"zh":'推我更高！',"usage":'荡秋千时的真实语境'},
        {"sentence":'Wheee！',"zh":'快乐的象声词',"usage":'任何滑动/飞翔时'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 45 · Daddy Puts up a Picture 爸爸挂画
# ═══════════════════════════════════════════════════════════════════════════════
EP45 = _ep(
    num=45, title_en='Daddy Puts up a Picture', title_zh='爸爸挂画', color='blue',
    synopsis='Daddy Pig 要在墙上挂一幅画。他宣称自己是专家，但敲钉子时敲歪了，洞打大了，还把管道打穿了，水喷出来！最后请来了专业工人修理。',
    vocab=[        {"word":'picture',"phonetic":'ˈpɪktʃə',"pos":'n.',"zh":'图画',"action":'假装举起一幅画，"A picture！"'},        {"word":'nail',"phonetic":'neɪl',"pos":'n.',"zh":'钉子',"action":'拇指和食指夹住小钉子'},        {"word":'hammer',"phonetic":'ˈhæmə',"pos":'n.',"zh":'锤子',"action":'假装挥锤，"Bang！"'},        {"word":'hang',"phonetic":'hæŋ',"pos":'v.',"zh":'悬挂',"action":'假装把东西挂在墙上'},        {"word":'wall',"phonetic":'wɔːl',"pos":'n.',"zh":'墙',"action":'用手拍墙，"The wall！"'},        {"word":'pipe',"phonetic":'paɪp',"pos":'n.',"zh":'管道',"action":'双臂做管道形状，"Water pipe！"'},        {"word":'leak',"phonetic":'liːk',"pos":'v./n.',"zh":'漏水',"action":'做出水漏出来的动作'},        {"word":'disaster',"phonetic":'dɪˈzɑːstə',"pos":'n.',"zh":'灾难',"action":'双手摊开，"Disaster！ Oh no！"'},    ],
    patterns=[        {"pattern":"I'm an expert at putting up pictures.","zh":'我最擅长挂画了',"example":"I'm an expert at everything! (Daddy Pig)"},        {"pattern":'Bang! Bang! Bang!',"zh":'咚！咚！咚！',"example":'Hammer the nail — bang bang bang!'},        {"pattern":"Oh dear, there's a water leak!","zh":'哦不，有水在漏了！',"example":"There's a leak! Call someone!"},        {"pattern":"I'll call a plumber.","zh":'我去叫水管工',"example":"We need a professional! I'll call someone!"},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第44集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🖼️',"bg":'blue',"trigger":'Daddy 要挂画',"action":'假装举起一幅重画'},
            {"emoji":'🔨',"bg":'yellow',"trigger":'敲钉子敲歪了',"action":'做出 oops 表情，斜着的钉子'},
            {"emoji":'💧',"bg":'blue',"trigger":'管道破了，水喷出来',"action":'做水喷的动作，"Disaster！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What went wrong when Daddy was putting up the picture?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说管道破了/水漏',"parent":'"He hit a water pipe! Water everywhere! Disaster!"'},
                {"child":'说钉子敲歪',"parent":'"The nail went in crooked... and then hit a pipe!"'},
                {"child":'不说话',"parent":'做出水喷出来的动作，"SPLASH！ What happened？"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Was Daddy really an expert?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'笑着说不',"parent":'"He SAID he was! But hitting a water pipe is... not expert behaviour!"'},
                {"child":'说是',"parent":'"He tried his best！ But the pipe disagreed!"'},
                {"child":'不说话',"parent":'做出专家姿态，然后耸肩，"I\'m an expert... oops!"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"Do you think you\'re good at doing DIY (fixing things at home)?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说好',"parent":'"Like Daddy! Or maybe better than Daddy..."'},
                {"child":'说不好',"parent":'"Honest！ Sometimes calling a professional is the smartest thing!"'},
                {"child":'不说话',"parent":'"I\'m an expert... at calling the plumber!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Has anything ever gone wrong with a simple home repair?"'],
            "rows":[
                {"child":'说过',"parent":'"Like Daddy！ Water everywhere？ Or something else？"'},
                {"child":'摇头',"parent":'"Lucky! Daddy\'s small picture became a BIG disaster!"'},
                {"child":'笑了',"parent":'"One nail. One wall. One pipe. One disaster. Classic Daddy Pig!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"I\'m going to hang this picture! Stand back — I\'m an expert！"'],
            "rows":[
                {"child":'假装让路',"parent":'"Ready？ BANG！ Oh... the nail is crooked..."'},
                {"child":'说 "Be careful!"',"parent":'"I AM careful! I\'m an... oh. Oh no. Is that water?"'},
                {"child":'说中文',"parent":'家长扮 Daddy："I\'m an expert！ BANG！ DISASTER！"'},
            ],
        },
        "recast":[
            {"term":'expert',"explanation":'"I\'m an expert = 我是专家。 Daddy says this often... and is often wrong!"'},
            {"term":'disaster',"explanation":'"Disaster = 灾难。 It was a disaster！ Everything went wrong!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Hang the picture！ Bang！" — 假装挂画，敲钉',
            '"Oh dear！ Water leak！" — 假装水喷出来，惊慌',
            '"I\'m an expert！" — 自信姿态',
            '"Disaster！" — 双手摊开，无奈',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Daddy 宣布挂画',"L1":'L1: "Picture！ Expert！"',"L2":'L2: "I\'m an expert at putting up pictures！"',"L3":'L3: "Stand back, everyone! I\'m going to hang this picture! I\'m an expert!"'},
            {"scene":'打穿管道',"L1":'L1: "Water！ Leak！"',"L2":'L2: "Oh dear！ Water is leaking！"',"L3":'L3: "BANG! Oh! There\'s water coming out of the wall! I think I hit a pipe!"'},
            {"scene":'叫专业工人',"L1":'L1: "Plumber！"',"L2":'L2: "We need a plumber！"',"L3":'L3: "This has become a disaster! I\'ll call the plumber immediately！"'},
        ],
        },
        "bugs":{
            "rule":'说 "I\'m an expert" 得1分（模仿 Daddy）；说 "disaster" 得2分；说 "I\'ll call a plumber" 得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'picture → hammer → nail → wall → pipe → leak → disaster → plumber'},
            {"level":'L2 (句)',"text":'Daddy wanted to hang a picture. He said he was an expert. He hit a water pipe. Water leaked everywhere.'},
            {"level":'L3 (完整)',"text":"Daddy Pig decided to hang a picture on the wall. 'I'm an expert!' he said. BANG！ The nail went in — but also went through a water pipe! Water sprayed everywhere! What a disaster! They had to call a plumber to fix it. Daddy Pig's simple task became quite an adventure!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ang → /æŋ/ 鼻音',
            "examples":['bang', 'hang', 'sang', 'rang', 'gang'],
            "tongue_tip":'"ang" 结尾有鼻音 /ŋ/。"Bang! Hang the picture with a bang!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP46 At the Beach（在海边）——" 故意停顿制造悬念',
        "next_a":'EP46 At the Beach',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"I'm an expert at that.","zh":'我最擅长这个了',"usage":'用于任何即将失败的挑战'},
        {"sentence":'Oh dear! Disaster!',"zh":'哦不！灾难！',"usage":'任何事情出错时'},
        {"sentence":"Stand back — I'm going to...","zh":'退后——我要...',"usage":'宣布某个动作前'},
        {"sentence":"I'll call the plumber.","zh":'我去叫水管工',"usage":'解决问题的幽默式'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 46 · At the Beach 在海边
# ═══════════════════════════════════════════════════════════════════════════════
EP46 = _ep(
    num=46, title_en='At the Beach', title_zh='在海边', color='blue',
    synopsis='全家去海边度假！Peppa 和 George 在沙滩上捡贝壳、建沙堡、玩浪花。Daddy 晒太阳晒着晒着睡着了，被涨潮的海浪打湿了脚！',
    vocab=[        {"word":'beach',"phonetic":'biːtʃ',"pos":'n.',"zh":'海滩',"action":'假装踩沙子，"The beach！ Sand and sea!"'},        {"word":'sand',"phonetic":'sænd',"pos":'n.',"zh":'沙子',"action":'用手指假装过细沙，"Sand！ Soft and fine!"'},        {"word":'castle',"phonetic":'ˈkɑːsl',"pos":'n.',"zh":'城堡（沙堡）',"action":'做出建城堡的动作，"Sand castle！"'},        {"word":'shells',"phonetic":'ʃelz',"pos":'n.',"zh":'贝壳',"action":'假装捡起贝壳，"Shells on the beach！"'},        {"word":'waves',"phonetic":'weɪvz',"pos":'n.',"zh":'海浪',"action":'双臂做波浪运动，"Waves! Whoosh!"'},        {"word":'sunbathe',"phonetic":'ˈsʌnbeɪð',"pos":'v.',"zh":'晒太阳',"action":'假装平躺，脸向太阳，"Sunbathing！"'},        {"word":'tide',"phonetic":'taɪd',"pos":'n.',"zh":'潮汐',"action":'手做潮起潮落，"The tide is coming in!"'},        {"word":'seaside',"phonetic":'ˈsiːsaɪd',"pos":'n.',"zh":'海边',"action":'"The seaside！ Sand, sea, sun!"'},    ],
    patterns=[        {"pattern":"We're going to the beach!","zh":'我们去海边了！',"example":"We're going to the beach! Hurray!"},        {"pattern":'Can you hear the waves?',"zh":'你能听到海浪声吗？',"example":'Listen! Can you hear the waves?'},        {"pattern":"Let's build a sandcastle!","zh":'我们来建沙堡吧！',"example":"Let's build a sandcastle before the tide comes in!"},        {"pattern":'The tide is coming in!',"zh":'潮水涨上来了！',"example":'The tide is coming in — quick!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第45集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🏖️',"bg":'blue',"trigger":'到达海滩，沙滩上玩',"action":'假装踩沙子，"Soft sand！"'},
            {"emoji":'🐚',"bg":'yellow',"trigger":'捡贝壳',"action":'假装捡贝壳，"A shell！ Pretty！"'},
            {"emoji":'🌊',"bg":'blue',"trigger":'海浪打湿了 Daddy',"action":'假装海浪来了，"The tide！ SPLASH！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What did Peppa and George do at the beach?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说建沙堡/捡贝壳',"parent":'"Build a sandcastle and collect shells！ Perfect beach day!"'},
                {"child":'说不知道',"parent":'"They collected shells, built a sandcastle, and played in the waves!"'},
                {"child":'不说话',"parent":'做出建沙堡动作，"Building..."'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What happened to Daddy Pig at the beach?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说被海浪打湿',"parent":'"He was sunbathing and fell asleep... and the TIDE came in! Wet feet! Classic Daddy!"'},
                {"child":'说不知道',"parent":'"Daddy fell asleep in the sun... and the tide came in..."'},
                {"child":'不说话',"parent":'假装平躺睡着，然后假装被水喷到，"SPLASH！"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"What\'s your favourite thing to do at the beach?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说活动',"parent":'"[Activity]！ The beach is so fun!"'},
                {"child":'说游泳',"parent":'"Swimming！ In the sea! Are the waves big?"'},
                {"child":'不说话',"parent":'"Me — I collect shells! Each one is different!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever been to the beach? What was it like?"'],
            "rows":[
                {"child":'说去过',"parent":'"Did you build a sandcastle? Get buried in the sand? Swim?"'},
                {"child":'摇头',"parent":'"Never？ Imagine — sand between your toes! Waves crashing!"'},
                {"child":'笑了',"parent":'"Did you eat ice cream at the seaside? It always tastes better at the beach!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"We\'re at the beach！ What shall we do first？"'],
            "rows":[
                {"child":'说建沙堡',"parent":'"Sandcastle！ Find some wet sand! Build the walls first!"'},
                {"child":'假装捡贝壳',"parent":'"A shell！ Oh！ Another one！ Let\'s collect them all!"'},
                {"child":'说中文',"parent":'家长扮 Mummy："The seaside! Can you hear the waves? Whoosh!"'},
            ],
        },
        "recast":[
            {"term":'the tide is coming in',"explanation":'"Tide = 潮汐。 Coming in = 涨潮，海水向岸边涌来"'},
            {"term":'sunbathe',"explanation":'"Sunbathe = sun（太阳）+ bathe（沐浴）= 晒太阳"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Soft sand！" — 用手指假装过细沙',
            '"Build a sandcastle！" — 做堆沙建城堡动作',
            '"Waves coming！ WHOOSH！" — 双臂做海浪',
            '"Sunbathing！ Ahh..." — 假装平躺，脸迎太阳',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'到达海边',"L1":'L1: "Beach！ Sand！"',"L2":'L2: "We\'re at the beach！"',"L3":'L3: "The seaside! I can hear the waves! Can you feel the sand between your toes?"'},
            {"scene":'建沙堡',"L1":'L1: "Castle！"',"L2":'L2: "Let\'s build a sandcastle！"',"L3":'L3: "We need wet sand for the walls! And shells for decoration! Build it before the tide comes!"'},
            {"scene":'Daddy 被潮水打湿',"L1":'L1: "Wet！ Tide！"',"L2":'L2: "The tide came in！ Daddy\'s wet！"',"L3":'L3: "Daddy was sunbathing and fell asleep! The tide came in and... SPLASH! Wet feet Daddy!"'},
        ],
        },
        "bugs":{
            "rule":'说 "sandcastle" 得1分；说 "the tide is coming" 得2分；说 "seaside" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'beach → sand → sandcastle → shells → waves → sunbathe → tide → seaside'},
            {"level":'L2 (句)',"text":'The family went to the beach. They collected shells and built a sandcastle. Daddy sunbathed and got wet.'},
            {"level":'L3 (完整)',"text":'The Pig family had a day at the seaside! Peppa and George collected shells and built a beautiful sandcastle before the tide could wash it away. Daddy Pig lay down to sunbathe... and fell asleep! The tide came in... SPLASH！ Wet feet! The beach is wonderful!'},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 each/ach → /iːtʃ/ 音',
            "examples":['beach', 'teach', 'reach', 'peach', 'each'],
            "tongue_tip":'"Beach, peach, each reach — teach me!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP47 Mister Skinnylegs（细腿先生）——" 故意停顿制造悬念',
        "next_a":'EP47 Mister Skinnylegs',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"We're going to the beach!","zh":'我们去海边了！',"usage":'出发去海边时的仪式感'},
        {"sentence":"Let's build a sandcastle!","zh":'我们来建沙堡！',"usage":'沙滩必做活动'},
        {"sentence":'The tide is coming in!',"zh":'潮水涨上来了！',"usage":'制造紧迫感'},
        {"sentence":'Can you hear the waves?',"zh":'你能听到海浪声吗？',"usage":'感官体验引导'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 47 · Mister Skinnylegs 细腿先生
# ═══════════════════════════════════════════════════════════════════════════════
EP47 = _ep(
    num=47, title_en='Mister Skinnylegs', title_zh='细腿先生', color='purple',
    synopsis='Peppa 在浴室发现了一只蜘蛛！蜘蛛有八条细细的长腿，Peppa 叫它 Mister Skinnylegs。Daddy 假装不怕，但实际上非常害怕蜘蛛，最后还是 Mummy 帮忙把蜘蛛放回了花园。',
    vocab=[        {"word":'spider',"phonetic":'ˈspaɪdə',"pos":'n.',"zh":'蜘蛛',"action":'八指张开，做爬行动作，"Spider！"'},        {"word":'legs',"phonetic":'leɡz',"pos":'n.',"zh":'腿',"action":'指腿，"Legs！ Eight legs for a spider！"'},        {"word":'frightened',"phonetic":'ˈfraɪtnd',"pos":'adj.',"zh":'害怕的',"action":'做出害怕、后退的样子'},        {"word":'brave',"phonetic":'breɪv',"pos":'adj.',"zh":'勇敢的',"action":'挺胸，假装不怕'},        {"word":'pretend',"phonetic":'prɪˈtend',"pos":'v.',"zh":'假装',"action":'做出假装的动作，"Pretend — it\'s not real!"'},        {"word":'gently',"phonetic":'ˈdʒentli',"pos":'adv.',"zh":'轻轻地',"action":'缓慢、小心地移动，"Gently, carefully!"'},        {"word":'tiny',"phonetic":'ˈtaɪni',"pos":'adj.',"zh":'微小的',"action":'大拇指和食指几乎相触，"So tiny!"'},        {"word":'harmless',"phonetic":'ˈhɑːmləs',"pos":'adj.',"zh":'无害的',"action":'摆手，"Harmless！ It won\'t hurt you!"'},    ],
    patterns=[        {"pattern":"It's only a tiny spider.","zh":'只是一只小蜘蛛',"example":"It's only a little thing — harmless!"},        {"pattern":"Daddy isn't frightened of spiders.","zh":'爸爸不怕蜘蛛',"example":"He says he isn't frightened. But look at his face!"},        {"pattern":'Put it down gently.',"zh":'轻轻地把它放下来',"example":"Gently! Don't scare it!"},        {"pattern":'Spiders are actually quite harmless.',"zh":'蜘蛛其实是无害的',"example":'Most spiders are completely harmless!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第46集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🕷️',"bg":'purple',"trigger":'Peppa 发现蜘蛛',"action":'做出惊讶但好奇的表情'},
            {"emoji":'😱',"bg":'red',"trigger":'Daddy 假装不怕但其实很怕',"action":'做出 Daddy 硬撑的样子，"I\'m not frightened!"'},
            {"emoji":'🌿',"bg":'green',"trigger":'Mummy 把蜘蛛放回花园',"action":'轻轻地，小心翼翼地'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Was Daddy really not frightened of the spider?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'笑着说不',"parent":'"He SAID he wasn\'t frightened! But his face told a different story!"'},
                {"child":'说是',"parent":'"He claimed not to be! But he kept backing away..."'},
                {"child":'不说话',"parent":'做出 Daddy 假装勇敢但其实害怕的样子'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What did Mummy do with the spider?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说放回花园',"parent":'"She put it outside in the garden! Gently! Spiders belong in nature!"'},
                {"child":'说不知道',"parent":'"Mummy picked it up very gently and took it to the garden!"'},
                {"child":'不说话',"parent":'假装用杯子盖住蜘蛛，然后小心带到门口'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"Are you scared of spiders?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说怕',"parent":'"Like Daddy！ Most people are！ But they\'re harmless!"'},
                {"child":'说不怕',"parent":'"Brave！ Like Mummy！ She picked it up gently!"'},
                {"child":'不说话',"parent":'"Me... let\'s just say I\'m not as brave as Mummy Pig!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever found an insect or animal inside the house?"'],
            "rows":[
                {"child":'说过',"parent":'"What was it？ Were you frightened？ What did you do with it?"'},
                {"child":'摇头',"parent":'"Lucky! Peppa found a spider — with eight skinny legs!"'},
                {"child":'笑了',"parent":'"A spider with eight long skinny legs! Mister Skinnylegs!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Ahh！ There\'s a spider！ What should we do？"'],
            "rows":[
                {"child":'说捉走它',"parent":'"But gently！ It\'s harmless！ Can you catch it in a cup?"'},
                {"child":'说不要怕',"parent":'"It\'s only tiny！ Mister Skinnylegs won\'t hurt you!"'},
                {"child":'说中文',"parent":'家长扮 Daddy："I\'m not frightened! It\'s just a tiny harmless spider!" （然后跳开）'},
            ],
        },
        "recast":[
            {"term":'frightened',"explanation":'"Frightened = 害怕的。 Frightened of = 对...感到害怕"'},
            {"term":'harmless',"explanation":'"Harmless = harm（伤害）+ less（没有）= 无害的"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Eek！ A spider！" — 假装惊讶后退',
            '"Eight skinny legs！" — 八指张开，慢慢爬行',
            '"I\'m not frightened！" — 挺胸，假装勇敢',
            '"Put it outside gently！" — 小心翼翼端着想象的杯子',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'发现蜘蛛',"L1":'L1: "Spider！"',"L2":'L2: "There\'s a spider！ Eek！"',"L3":'L3: "Look! A spider! It has eight long skinny legs! Hello, Mister Skinnylegs!"'},
            {"scene":'Daddy 假装不怕',"L1":'L1: "Not scared！"',"L2":'L2: "I\'m not frightened of spiders！"',"L3":'L3: "I\'m not frightened of spiders at all! They\'re completely harmless! I\'ll just... stand over here."'},
            {"scene":'Mummy 放走蜘蛛',"L1":'L1: "Gently！"',"L2":'L2: "Mummy put the spider outside gently！"',"L3":'L3: "Hold still, little spider! Gently into the cup... and now outside to the garden! There you go!"'},
        ],
        },
        "bugs":{
            "rule":'说 "Mister Skinnylegs" 得3分；说 "harmless" 得2分；说 "frightened" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'spider → legs → frightened → brave → harmless → gently → tiny'},
            {"level":'L2 (句)',"text":"Peppa found a spider in the bathroom. Daddy said he wasn't frightened. But he was. Mummy put the spider outside."},
            {"level":'L3 (完整)',"text":"Peppa found a spider with eight long skinny legs! She called it Mister Skinnylegs. Daddy said he wasn't frightened of spiders at all — but he really was! In the end, brave Mummy picked up the spider very gently and put it outside in the garden. Spiders are harmless!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ight → /aɪt/ 音',
            "examples":['frightened', 'right', 'night', 'bright', 'tight'],
            "tongue_tip":'igh 的 gh 不发音，只有 /aɪ/。"Frightened at night — but it was alright!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP48 Grandpa Pig\'s Boat（爷爷的小船）——" 故意停顿制造悬念',
        "next_a":"EP48 Grandpa Pig's Boat",
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"It's only a tiny spider.","zh":'只是一只小蜘蛛',"usage":'安慰对小生物过度害怕的人'},
        {"sentence":'Spiders are harmless.',"zh":'蜘蛛是无害的',"usage":'科学教育句'},
        {"sentence":'Put it down gently.',"zh":'轻轻地把它放下来',"usage":'处理任何小生物时'},
        {"sentence":"I'm not frightened!","zh":'我不害怕！',"usage":'孩子学 Daddy 说，然后大家笑'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 48 · Grandpa Pig's Boat 爷爷的小船
# ═══════════════════════════════════════════════════════════════════════════════
EP48 = _ep(
    num=48, title_en="Grandpa Pig's Boat", title_zh='爷爷的小船', color='blue',
    synopsis='Grandpa Pig 有一艘小船！全家人登上小船在河上玩耍。Grandpa 介绍各种航海知识，但发动机出了问题。最后 Daddy Pig 来修，越修越糟，最后靠 Grandpa 解决了。',
    vocab=[        {"word":'boat',"phonetic":'bəʊt',"pos":'n.',"zh":'船',"action":'双手做船形，"A boat！ On the water!"'},        {"word":'sail',"phonetic":'seɪl',"pos":'v./n.',"zh":'航行/帆',"action":'假装拉帆，"Sail！ Full sail ahead!"'},        {"word":'anchor',"phonetic":'ˈæŋkə',"pos":'n.',"zh":'锚',"action":'做出抛锚的动作，"Drop the anchor!"'},        {"word":'captain',"phonetic":'ˈkæptɪn',"pos":'n.',"zh":'船长',"action":'双手叉腰，"I am the captain!"'},        {"word":'engine',"phonetic":'ˈendʒɪn',"pos":'n.',"zh":'引擎',"action":'做出引擎轰鸣声，"Engine on！ Vroom!"'},        {"word":'wave',"phonetic":'weɪv',"pos":'n.',"zh":'波浪',"action":'双臂做波浪运动'},        {"word":'row',"phonetic":'rəʊ',"pos":'v.',"zh":'划桨',"action":'做划桨动作，"Row row row your boat!"'},        {"word":'ahoy',"phonetic":'əˈhɔɪ',"pos":'interj.',"zh":'海盗式打招呼',"action":'大声，"Ahoy！"'},    ],
    patterns=[        {"pattern":'All aboard!',"zh":'大家上船！',"example":'All aboard！ The boat is leaving!'},        {"pattern":'Drop the anchor!',"zh":'抛锚！',"example":"Drop the anchor here! We'll stop!"},        {"pattern":'Captain Grandpa to the rescue!',"zh":'船长 Grandpa 来救援！',"example":'The captain knows what to do!'},        {"pattern":'Row, row, row your boat.',"zh":'划呀划呀划小船',"example":'Row! Row! Row your boat gently!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第47集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'⛵',"bg":'blue',"trigger":'登上 Grandpa 的小船',"action":'假装踏上不稳的船，"Woah！"'},
            {"emoji":'⚓',"bg":'navy',"trigger":'Grandpa 示范航海',"action":'双手叉腰，"Captain of the ship！"'},
            {"emoji":'🔧',"bg":'yellow',"trigger":'引擎出问题',"action":'皱眉，"Engine not working!"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Whose boat did the family go on?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Grandpa\'s!"',"parent":'"YES！ Grandpa Pig\'s boat！ He was the captain!"'},
                {"child":'说 Daddy',"parent":'"Daddy tried to help — but it was GRANDPA\'S boat!"'},
                {"child":'不说话',"parent":'"Whose boat? It belongs to...?" 指向想象的 Grandpa'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What went wrong on the boat trip?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说引擎坏了',"parent":'"The engine stopped working! And Daddy tried to fix it..."'},
                {"child":'说不知道',"parent":'"The engine had a problem! They needed to fix it to get home!"'},
                {"child":'不说话',"parent":'假装发动机停止，"Putt... putt... silence. Hmm!"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"Would you like to go on a boat trip? Where would you go?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说地方',"parent":'"To [place]！ By boat！ Ahoy！"'},
                {"child":'说不想',"parent":'"Not a boat person？ The waves can be scary!"'},
                {"child":'不说话',"parent":'"I\'d sail to... an island with treasure! Ahoy!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever been on a boat?"'],
            "rows":[
                {"child":'说去过',"parent":'"What kind of boat？ Did it rock in the waves?"'},
                {"child":'摇头',"parent":'"Never？ Grandpa Pig\'s boat is the perfect first boat!"'},
                {"child":'笑了',"parent":'"Row row row your boat — gently down the stream!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"All aboard！ This is Grandpa\'s boat！ I am the captain！"'],
            "rows":[
                {"child":'上船',"parent":'"Welcome aboard！ Hold on — the waves might rock us!"'},
                {"child":'说 "Ahoy!"',"parent":'"Ahoy！ Sail away！ Which direction？"'},
                {"child":'说中文',"parent":'家长扮 Grandpa："All aboard！ Drop the anchor!"'},
            ],
        },
        "recast":[
            {"term":'all aboard',"explanation":'"All aboard = 大家都上船（火车/船出发时说的）"'},
            {"term":'captain',"explanation":'"Captain = 船长、机长、队长。 The captain is in charge!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"All aboard！" — 做踏上船的动作',
            '"Drop the anchor！" — 做抛锚动作',
            '"Row! Row! Row!" — 做划桨动作',
            '"Ahoy！" — 大声打招呼',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'登船',"L1":'L1: "Boat！ Ahoy！"',"L2":'L2: "All aboard Grandpa\'s boat！"',"L3":'L3: "All aboard! Grandpa Pig\'s boat is ready! I am the captain!"'},
            {"scene":'引擎出问题',"L1":'L1: "Engine！ Broken！"',"L2":'L2: "The engine stopped working！"',"L3":'L3: "Oh dear! The engine has stopped! We need to fix it to get home!"'},
            {"scene":'唱划船歌',"L1":'L1: "Row row row！"',"L2":'L2: "Row your boat gently！"',"L3":'L3: "Row, row, row your boat, gently down the stream! Merrily, merrily..."'},
        ],
        },
        "bugs":{
            "rule":'说 "All aboard" 得2分；说 "Ahoy" 得1分；唱划船歌得3分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'boat → sail → anchor → captain → engine → waves → row → ahoy'},
            {"level":'L2 (句)',"text":'Grandpa had a boat. The family went on a boat trip. The engine broke. Grandpa fixed it.'},
            {"level":'L3 (完整)',"text":'Grandpa Pig had a wonderful boat! All aboard! The family sailed on the river. Grandpa was the captain. But the engine stopped working! Daddy tried to fix it — and made it worse! Finally Grandpa fixed it himself. What a great boat trip!'},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 oat → /əʊt/ 音',
            "examples":['boat', 'coat', 'float', 'throat', 'goat'],
            "tongue_tip":'"The goat in the coat floated on the boat!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP49 Shopping（购物）——" 故意停顿制造悬念',
        "next_a":'EP49 Shopping',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'All aboard!',"zh":'大家上船！',"usage":'任何出发活动开始时'},
        {"sentence":'Ahoy!',"zh":'嗨！（海盗式）',"usage":'有趣的打招呼方式'},
        {"sentence":'Drop the anchor!',"zh":'抛锚！',"usage":'到达目的地时'},
        {"sentence":'Row row row your boat.',"zh":'划呀划呀划小船',"usage":'经典儿歌用途'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 49 · Shopping 购物
# ═══════════════════════════════════════════════════════════════════════════════
EP49 = _ep(
    num=49, title_en='Shopping', title_zh='购物', color='pink',
    synopsis='全家去超市购物！Mummy 给了每个人一个任务：Peppa 找某样东西，George 找另一样。Daddy 被叮嘱只买清单上的东西。但 Daddy 被美食区吸引，拿了很多额外的东西！',
    vocab=[        {"word":'shopping',"phonetic":'ˈʃɒpɪŋ',"pos":'n.',"zh":'购物',"action":'推想象的购物车，"Shopping！"'},        {"word":'supermarket',"phonetic":'ˈsuːpəmɑːkɪt',"pos":'n.',"zh":'超市',"action":'双手展示，"The supermarket！"'},        {"word":'list',"phonetic":'lɪst',"pos":'n.',"zh":'清单',"action":'假装看清单，"Shopping list！"'},        {"word":'trolley',"phonetic":'ˈtrɒli',"pos":'n.',"zh":'购物车',"action":'推想象的大车，"Trolley!"'},        {"word":'aisle',"phonetic":'aɪl',"pos":'n.',"zh":'货架通道',"action":'走在两排货架间，"Down the aisle!"'},        {"word":'bargain',"phonetic":'ˈbɑːɡɪn',"pos":'n.',"zh":'特价品',"action":'眼睛发光，"A bargain！ So cheap!"'},        {"word":'queue',"phonetic":'kjuː',"pos":'v./n.',"zh":'排队',"action":'排成一队，"Queue up! Wait your turn!"'},        {"word":'receipt',"phonetic":'rɪˈsiːt',"pos":'n.',"zh":'收据',"action":'假装拿一张长纸，"The receipt！"'},    ],
    patterns=[        {"pattern":'Can I have that, please?',"zh":'我可以要那个吗？',"example":'Can I have some biscuits please?'},        {"pattern":"Only what's on the list!","zh":'只买清单上的东西！',"example":"Daddy！ Only what's on the list!"},        {"pattern":"That's a bargain!","zh":'那真是特价品！',"example":'Two for one! What a bargain!'},        {"pattern":"We've got everything on the list.","zh":'我们买完清单上所有的东西了',"example":'All done — we have everything!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第48集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🛒',"bg":'pink',"trigger":'推着购物车进超市',"action":'推车，"Shopping！"'},
            {"emoji":'📋',"bg":'yellow',"trigger":'Mummy 分配购物任务',"action":'假装看清单，"You get this, I\'ll get that"'},
            {"emoji":'🍰',"bg":'red',"trigger":'Daddy 被美食吸引',"action":'眼睛发光，"Ooh！ That looks nice！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Who kept putting extra things in the trolley?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Daddy!"',"parent":'"YES！ Daddy！ He saw things he liked and... they went in the trolley!"'},
                {"child":'说 Peppa',"parent":'"Peppa tried to focus! It was DADDY who kept adding things!"'},
                {"child":'不说话',"parent":'做出偷偷把东西放进购物车的动作'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What was Mummy\'s rule for shopping?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说清单',"parent":'"Only buy what\'s on the list！ No extras！"'},
                {"child":'说不知道',"parent":'"Only what\'s on the LIST! Daddy kept forgetting that rule!"'},
                {"child":'不说话',"parent":'假装拿清单，严肃点头，"The RULE: only what\'s on the list!"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you could add ONE extra thing to the shopping trolley, what would it be?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说食物',"parent":'"[Food]！ Like Daddy would! Into the trolley!"'},
                {"child":'说玩具',"parent":'"A toy！ Would Mummy let you keep it? Or put it back?"'},
                {"child":'不说话',"parent":'"Me — chocolate biscuits. Every time. Into the trolley!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Do you like going shopping? Why or why not?"'],
            "rows":[
                {"child":'说喜欢',"parent":'"Like exploring！ Each aisle has different things!"'},
                {"child":'说不喜欢',"parent":'"Boring？ Unless you get to choose something!"'},
                {"child":'笑了',"parent":'"The best part is finding bargains! Or biscuits!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Welcome to the supermarket！ Do you have your shopping list？"'],
            "rows":[
                {"child":'假装看清单',"parent":'"Good！ What\'s first？ Down which aisle?"'},
                {"child":'说想要的东西',"parent":'"Is that on the list？ Or is it like Daddy — an extra?"'},
                {"child":'说中文',"parent":'家长扮 Mummy："Only what\'s on the list！ Daddy！"'},
            ],
        },
        "recast":[
            {"term":"only what's on the list","explanation":'"Only = 只、仅仅。 Only what\'s on the list = 只买清单上的"'},
            {"term":'bargain',"explanation":'"Bargain = 特价品，便宜货。 What a bargain!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Push the trolley！" — 推想象的购物车',
            '"Check the list！" — 假装看清单',
            '"Only what\'s on the list！" — 举手指，严肃地',
            '"What a bargain！" — 眼睛发光，快速拿起',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'全家进超市',"L1":'L1: "Shopping！"',"L2":'L2: "We\'re going shopping！"',"L3":'L3: "Welcome to the supermarket! Mummy has a list — we only buy what\'s on the list!"'},
            {"scene":'Daddy 偷放额外东西',"L1":'L1: "Nice！ In!"',"L2":'L2: "Daddy is adding extra things！"',"L3":'L3: "Ooh! That looks delicious! Just this one... and that... and maybe this..."'},
            {"scene":'结账',"L1":'L1: "Queue！ Pay！"',"L2":'L2: "Queue up to pay！"',"L3":'L3: "Queue up at the checkout! Did we get everything on the list? And only the list?"'},
        ],
        },
        "bugs":{
            "rule":'说 "only what\'s on the list" 得3分；说 "bargain" 得1分；说 "queue" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'shopping → supermarket → list → trolley → aisle → bargain → queue → receipt'},
            {"level":'L2 (句)',"text":'The family went shopping. Mummy had a list. They must only buy things on the list. Daddy kept adding extras.'},
            {"level":'L3 (完整)',"text":"The Pig family went to the supermarket! Mummy had a shopping list and the rule was: only what's on the list! But Daddy Pig kept seeing things he liked and putting them in the trolley. Cakes! Biscuits! Cheese! Mummy kept putting them back! In the end, they bought everything on the list — and maybe a few extras!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ue → /juː/ 音',
            "examples":['queue', 'clue', 'blue', 'true', 'argue'],
            "tongue_tip":'"Queue? It\'s true — the clue is blue!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP50 My Birthday Party（我的生日派对）——" 故意停顿制造悬念',
        "next_a":'EP50 My Birthday Party',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":"Only what's on the list!","zh":'只买清单上的！',"usage":'购物时的纪律句'},
        {"sentence":'What a bargain!',"zh":'真是特价品！',"usage":'发现优惠时用'},
        {"sentence":'Can I have that, please?',"zh":'我可以要那个吗？',"usage":'礼貌请求'},
        {"sentence":"We've got everything on the list.","zh":'清单上的东西都买了',"usage":'完成任务时确认'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 50 · My Birthday Party 我的生日派对
# ═══════════════════════════════════════════════════════════════════════════════
EP50 = _ep(
    num=50, title_en='My Birthday Party', title_zh='我的生日派对', color='pink',
    synopsis='今天是 Peppa 的生日！所有朋友都来参加她的生日派对。大家唱歌、玩游戏、吃蛋糕。Peppa 得到了很多礼物！',
    vocab=[        {"word":'birthday party',"phonetic":'ˈbɜːθdeɪ ˈpɑːti',"pos":'n.',"zh":'生日派对',"action":'做出派对欢呼的样子，"Party！"'},        {"word":'invite',"phonetic":'ɪnˈvaɪt',"pos":'v.',"zh":'邀请',"action":'张开双臂，"You\'re invited！"'},        {"word":'gift',"phonetic":'ɡɪft',"pos":'n.',"zh":'礼物',"action":'假装接过包装礼物'},        {"word":'wrap',"phonetic":'ræp',"pos":'v.',"zh":'包装',"action":'假装缠绕包装纸'},        {"word":'balloon',"phonetic":'bəˈluːn',"pos":'n.',"zh":'气球',"action":'双手做气球形状，"Balloon！"'},        {"word":'celebrate',"phonetic":'ˈselɪbreɪt',"pos":'v.',"zh":'庆祝',"action":'举拳欢呼，"Celebrate!"'},        {"word":'special',"phonetic":'ˈspeʃl',"pos":'adj.',"zh":'特别的',"action":'微笑，"Special — only for today!"'},        {"word":'ribbon',"phonetic":'ˈrɪbən',"pos":'n.',"zh":'丝带',"action":'做出拉丝带的动作，"Ribbon!"'},    ],
    patterns=[        {"pattern":'Happy birthday to you!',"zh":'祝你生日快乐！',"example":'Happy birthday, dear Peppa!'},        {"pattern":"It's my birthday today!","zh":'今天是我的生日！',"example":'Today is a special day — my birthday!'},        {"pattern":'Can I open my presents now?',"zh":'我现在可以打开礼物吗？',"example":'Please can I open them now?'},        {"pattern":'Thank you for coming to my party.',"zh":'谢谢你来参加我的派对',"example":'Thank you for coming!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第49集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🎉',"bg":'pink',"trigger":'派对开始，朋友们到来',"action":'做开心欢迎动作'},
            {"emoji":'🎁',"bg":'yellow',"trigger":'开礼物',"action":'假装撕包装纸，"What\'s inside?"'},
            {"emoji":'🎂',"bg":'red',"trigger":'唱生日歌，吹蜡烛',"action":'唱歌，吹蜡烛'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"Whose birthday party was it?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"Peppa\'s!"',"parent":'"YES！ It was Peppa\'s birthday！ All her friends came to celebrate!"'},
                {"child":'说不知道',"parent":'"Peppa Pig\'s birthday party！ Everyone was there!"'},
                {"child":'不说话',"parent":'"Whose birthday？ Happy birthday to...?"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"What do you do at a birthday party?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说蛋糕/歌/礼物',"parent":'"YES！ Cake, singing, presents! That\'s a birthday party!"'},
                {"child":'说一样',"parent":'"And also [说没提到的]！ Peppa\'s party had all of it!"'},
                {"child":'不说话',"parent":'"Party! What happens？ Food？ Cake？ Presents？ Games？"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"What\'s the best present you\'ve ever received?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说礼物',"parent":'"[Present]！ Better than a [something funny]?"'},
                {"child":'说不知道',"parent":'"What would be the PERFECT birthday present for you?"'},
                {"child":'不说话',"parent":'"My best present was... actually the party itself! What about you?"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"What do you like most about birthday parties?"'],
            "rows":[
                {"child":'说食物/游戏',"parent":'"The [thing]！ Same as Peppa!"'},
                {"child":'说朋友来了',"parent":'"Friends！ That\'s what makes a party!"'},
                {"child":'笑了',"parent":'"Singing Happy Birthday is the most fun when everyone sings together!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Happy birthday！ It\'s YOUR party！ What shall we do first？"'],
            "rows":[
                {"child":'说游戏',"parent":'"[Game] first！ Let\'s all play!"'},
                {"child":'说礼物',"parent":'"Open the presents！ What did you get?"'},
                {"child":'说中文',"parent":'家长扮客人："Happy birthday！ This is for you！" 假装递礼物'},
            ],
        },
        "recast":[
            {"term":'celebrate',"explanation":'"Celebrate = 庆祝。 We celebrate birthdays, achievements, good news!"'},
            {"term":'invite',"explanation":'"Invite = 邀请。 You are invited = 你被邀请来了！"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Happy birthday！" — 鼓掌，唱生日歌开头',
            '"Blow out the candles！" — 深吸气，用力吹',
            '"Open the presents！" — 假装撕包装纸',
            '"Thank you for coming！" — 鞠躬，微笑',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'朋友们到达派对',"L1":'L1: "Party！"',"L2":'L2: "Happy birthday, Peppa！"',"L3":'L3: "Happy birthday, Peppa！ It\'s your special day! All your friends are here to celebrate!"'},
            {"scene":'开礼物',"L1":'L1: "Present！ Open！"',"L2":'L2: "Can I open my presents now？"',"L3":'L3: "What\'s inside this one? Let me tear the paper... Oh! It\'s wonderful!"'},
            {"scene":'吹蜡烛',"L1":'L1: "Wish！ Blow！"',"L2":'L2: "Make a wish and blow！"',"L3":'L3: "Happy birthday to you! Now make a wish... and blow out all the candles!"'},
        ],
        },
        "bugs":{
            "rule":'说 "Happy birthday" 得1分；说 "celebrate" 得2分；说 "Thank you for coming" 得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'birthday party → invite → celebrate → gift → balloon → cake → wish → ribbon'},
            {"level":'L2 (句)',"text":"It was Peppa's birthday party. All her friends came. They sang and ate cake. Peppa opened her presents."},
            {"level":'L3 (完整)',"text":"It was Peppa's birthday! All her friends came to celebrate. They played games, sang Happy Birthday, and blew out the candles. Peppa made a wish. Then came the presents! Peppa was so happy to have all her friends there. The best birthday ever!"},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ir → /ɜː/ 音',
            "examples":['birthday', 'bird', 'girl', 'first', 'shirt'],
            "tongue_tip":'嘴微圆，舌头不动，发 /ɜː/。"The birthday girl wore a shirt!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP51 Daddy\'s Movie Camera（爸爸的摄像机）——" 故意停顿制造悬念',
        "next_a":"EP51 Daddy's Movie Camera",
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Happy birthday!',"zh":'生日快乐！',"usage":'每年生日必用'},
        {"sentence":"It's a special day!","zh":'今天是特别的一天！',"usage":'任何重要日子'},
        {"sentence":'Thank you for coming.',"zh":'谢谢你来',"usage":'教孩子做主人时'},
        {"sentence":'Can I open my presents now?',"zh":'我现在可以打开礼物吗？',"usage":'适当时机使用'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 51 · Daddy's Movie Camera 爸爸的摄像机
# ═══════════════════════════════════════════════════════════════════════════════
EP51 = _ep(
    num=51, title_en="Daddy's Movie Camera", title_zh='爸爸的摄像机', color='orange',
    synopsis='Daddy Pig 得到了一台摄像机，到处拍摄！他把所有人说的话和做的事都录下来，大家都觉得很烦。最后他们一起观看录像，大家都笑了。',
    vocab=[        {"word":'camera',"phonetic":'ˈkæmərə',"pos":'n.',"zh":'摄像机',"action":'做出举摄像机的动作'},        {"word":'film',"phonetic":'fɪlm',"pos":'v.',"zh":'拍摄',"action":'假装对准镜头，"Action！ Filming!"'},        {"word":'record',"phonetic":'rɪˈkɔːd',"pos":'v.',"zh":'录制',"action":'按录制按钮，"Recording！"'},        {"word":'action',"phonetic":'ˈækʃn',"pos":'interj.',"zh":'开拍',"action":'导演手势，"ACTION！"'},        {"word":'embarrassing',"phonetic":'ɪmˈbærəsɪŋ',"pos":'adj.',"zh":'令人尴尬的',"action":'捂脸，"So embarrassing！"'},        {"word":'documentary',"phonetic":'ˌdɒkjʊˈmentri',"pos":'n.',"zh":'纪录片',"action":'假装摄影师，严肃解说'},        {"word":'director',"phonetic":'dɪˈrektə',"pos":'n.',"zh":'导演',"action":'双手做框框，"I\'m the director!"'},        {"word":'playback',"phonetic":'ˈpleɪbæk',"pos":'n.',"zh":'回放',"action":'假装按回放，看屏幕'},    ],
    patterns=[        {"pattern":'Lights, camera, action!',"zh":'灯光，摄像，开拍！',"example":'Lights, camera, action — the movie begins!'},        {"pattern":"I'm making a documentary.","zh":'我在拍纪录片',"example":'Daddy is making a family documentary!'},        {"pattern":"Don't point the camera at me!","zh":'不要把摄像机对着我！',"example":'Stop filming me!'},        {"pattern":"Let's watch the playback!","zh":'我们来看回放吧！',"example":"Let's watch what we filmed!"},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第50集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🎥',"bg":'orange',"trigger":'Daddy 到处拍摄',"action":'做举摄像机的动作，"Action！"'},
            {"emoji":'😤',"bg":'red',"trigger":'大家被烦到了',"action":'做出被镜头对准时的不自在'},
            {"emoji":'📺',"bg":'blue',"trigger":'一起看录像，大家都笑了',"action":'假装看屏幕，大笑'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What was Daddy Pig doing all day?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'说拍摄',"parent":'"Filming everyone！ EVERYWHERE！ With his new camera!"'},
                {"child":'说不知道',"parent":'"He had a movie camera and was filming everything — a family documentary!"'},
                {"child":'不说话',"parent":'做出举摄像机的动作，"Action！"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"How did everyone feel about being filmed all the time?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'说不喜欢',"parent":'"A bit embarrassing! Nobody likes a camera pointing at them all day!"'},
                {"child":'说不知道',"parent":'"They said \'Don\'t point the camera at me!\' It was a bit much!"'},
                {"child":'不说话',"parent":'做出被镜头对准时的不自在样子'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you had a camera for a day, what would you film?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说主题',"parent":'"A documentary about [thing]！ You\'d be the director!"'},
                {"child":'说家人',"parent":'"A family documentary! Like Daddy! But maybe ask permission first!"'},
                {"child":'不说话',"parent":'"Me — I\'d film the funniest things! Then watch the playback!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever been filmed in a video? What was it like?"'],
            "rows":[
                {"child":'说过',"parent":'"Were you embarrassed？ Or a natural movie star?"'},
                {"child":'摇头',"parent":'"Never on camera? Let\'s film something RIGHT NOW!"'},
                {"child":'笑了',"parent":'"Watching yourself on video is always funny — or embarrassing!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"Lights, camera, action！ I\'m making a documentary about YOU！"'],
            "rows":[
                {"child":'配合',"parent":'"Tell me — what\'s a normal day in your life？"'},
                {"child":'说话',"parent":'"Excellent！ You\'re a natural! Now show me your best action!"'},
                {"child":'说中文',"parent":'家长扮 Daddy："Say hello to the camera！ Action!"'},
            ],
        },
        "recast":[
            {"term":'documentary',"explanation":'"Documentary = 纪录片，拍摄真实生活的电影"'},
            {"term":'action',"explanation":'"Action！ = 开拍！ The director shouts this when filming starts!"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Lights, camera, action！" — 导演手势',
            '"Don\'t point that at me！" — 挡住脸',
            '"We\'re filming！" — 假装举摄像机',
            '"Watch the playback！" — 假装按播放，看屏幕',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'Daddy 宣布拍摄',"L1":'L1: "Camera！ Film！"',"L2":'L2: "I\'m making a documentary！"',"L3":'L3: "Lights, camera, action! I\'m going to film a documentary about our family!"'},
            {"scene":'大家不想被拍',"L1":'L1: "Stop！ Camera！"',"L2":'L2: "Don\'t point the camera at me！"',"L3":'L3: "Daddy！ Stop filming me! It\'s embarrassing! Point it somewhere else!"'},
            {"scene":'看回放大家都笑了',"L1":'L1: "Playback！ Funny！"',"L2":'L2: "Let\'s watch the playback！"',"L3":'L3: "Watch what we filmed today! Ready? Play! Ha ha ha! That\'s so funny!"'},
        ],
        },
        "bugs":{
            "rule":'说 "Lights, camera, action" 得3分；说 "documentary" 得2分；说 "embarrassing" 得1分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'camera → film → record → action → documentary → embarrassing → playback → director'},
            {"level":'L2 (句)',"text":'Daddy got a camera. He filmed everyone all day. Everyone got tired of it. They watched the playback together.'},
            {"level":'L3 (完整)',"text":'Daddy Pig got a new movie camera! He filmed everyone — Mummy cooking, Peppa playing, George with his dinosaur. Everyone! After a while, they said: stop filming us! But in the end, they all sat down to watch the playback... and laughed and laughed!'},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 era/ure → /ərə/ 轻读结尾',
            "examples":['camera', 'nature', 'picture', 'creature', 'adventure'],
            "tongue_tip":'结尾 -era/-ure 都是轻读，快速带过。"The camera captures every creature!"',
        },
        "next_script":'"今天的冒险结束了！下一集是 EP52 School Play（学校演出）——" 故意停顿制造悬念',
        "next_a":'EP52 School Play',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Lights, camera, action!',"zh":'灯光，摄像，开拍！',"usage":'任何游戏开始时'},
        {"sentence":"I'm making a documentary!","zh":'我在拍纪录片！',"usage":'记录日常的趣味方式'},
        {"sentence":"Let's watch the playback!","zh":'我们来看回放！',"usage":'事后一起笑'},
        {"sentence":"Don't point that at me!","zh":'不要对着我！',"usage":'假装抗议'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# EP 52 · School Play 学校演出
# ═══════════════════════════════════════════════════════════════════════════════
EP52 = _ep(
    num=52, title_en='School Play', title_zh='学校演出', color='yellow',
    synopsis='幼儿园要演出了！Madame Gazelle 安排大家扮演不同角色。Peppa 想演主角，但被分配了其他角色。最后演出大获成功，每个角色都同样重要！',
    vocab=[        {"word":'play',"phonetic":'pleɪ',"pos":'n.',"zh":'戏剧演出',"action":'鞠躬，"The play！ A school play!"'},        {"word":'performance',"phonetic":'pəˈfɔːməns',"pos":'n.',"zh":'表演',"action":'做演出的姿态'},        {"word":'role',"phonetic":'rəʊl',"pos":'n.',"zh":'角色',"action":'指自己，"I have an important role!"'},        {"word":'rehearse',"phonetic":'rɪˈhɜːs',"pos":'v.',"zh":'排练',"action":'认真重复动作，"Rehearse again!"'},        {"word":'nervous',"phonetic":'ˈnɜːvəs',"pos":'adj.',"zh":'紧张的',"action":'假装蝴蝶在肚子里，"Nervous!"'},        {"word":'audience',"phonetic":'ˈɔːdiəns',"pos":'n.',"zh":'观众',"action":'做出观看的姿势'},        {"word":'curtain call',"phonetic":'ˈkɜːtn kɔːl',"pos":'n.',"zh":'谢幕',"action":'鞠躬，"Curtain call！"'},        {"word":'applause',"phonetic":'əˈplɔːz',"pos":'n.',"zh":'掌声',"action":'鼓掌，"Applause！ Bravo！"'},    ],
    patterns=[        {"pattern":'Every part is important.',"zh":'每个角色都很重要',"example":'Every role matters, big or small!'},        {"pattern":'The show must go on!',"zh":'演出必须继续！',"example":'No matter what, the show goes on!'},        {"pattern":'Are you ready for the big performance?',"zh":'你准备好大型演出了吗？',"example":'Ready for the show?'},        {"pattern":'Take a bow!',"zh":'谢幕！',"example":'Bow to the audience!'},    ],
    goals={
        "min":"孩子能说出 3 个核心词汇",
        "mid":"孩子能用英文说一句完整的句子",
        "ideal":"孩子主动用 <strong>本集核心句</strong> 引用到真实场景",
    },
    phase1={
        "review_intro":'回顾第51集的核心词汇，用搞怪方式重温：',
        "review_script":'（夸张说错上集的关键词，等孩子纠正）',
        "review_response":'孩子一定会纠正——家长惊喜地接着说：「对！你记得！」',
        "preview_intro":'给孩子一个预告悬念：',
        "preview_script":'"Today — something amazing happens to Peppa. Watch carefully and tell me: what is the KEY moment?"',
        "preview_mission":'"Your mission: count how many times the magic word appears. Ready? Go."',
    },
    phase2={
        "settings":"英文音轨 + 英文字幕",
        "actions":[
            {"emoji":'🎭',"bg":'gold',"trigger":'幼儿园准备演出',"action":'假装排练，认真表演'},
            {"emoji":'😰',"bg":'yellow',"trigger":'演出前紧张',"action":'假装肚子里有蝴蝶，"Nervous!"'},
            {"emoji":'👏',"bg":'gold',"trigger":'演出成功，观众鼓掌',"action":'鼓掌，"Bravo！ Applause！"'},
        ],
    },
    phase3={
        "intro":"全程聊天，不是考试。读孩子的脸：眼神亮 → 继续；眼神空 → 降级。",
        "q1":{
            "type_label":"Yes/No 兜底",
            "script":'"What were the children putting on?"',
            "note":"家长做出等待的手势",
            "rows":[
                {"child":'"A school play!"',"parent":'"YES！ A school play! Everyone had a role!"'},
                {"child":'说不知道',"parent":'"A school play! A performance at the playgroup!"'},
                {"child":'不说话',"parent":'鞠躬，"Take a bow！ What is this for?"'},
            ],
        },
        "q2":{
            "type_label":"二选一",
            "script":'"Were the children nervous before the performance?"',
            "note":"配合手势示意两个选项",
            "rows":[
                {"child":'"Yes!"',"parent":'"YES！ Butterflies in the tummy! But once they started, it was wonderful!"'},
                {"child":'说不知道',"parent":'"Nervous before... then brilliant during! The show must go on!"'},
                {"child":'不说话',"parent":'假装肚子里有蝴蝶，"Nervous..." 然后深呼吸，"Ready!"'},
            ],
        },
        "q3":{
            "type_label":"开放式",
            "script":'"If you were in a school play, what role would you want?"',
            "note":"指着孩子，等待",
            "rows":[
                {"child":'说角色',"parent":'"[Role]！ Would you rehearse every day?"'},
                {"child":'说主角',"parent":'"The main part！ Like Peppa wanted! But every part is important!"'},
                {"child":'不说话',"parent":'"Me — I\'d want to be the NARRATOR. I just explain what happens!"'},
            ],
        },
        "personal":{
            "intro":"把故事跟孩子的真实生活挂钩。",
            "script_lines":['"Have you ever performed in front of an audience?"'],
            "rows":[
                {"child":'说过',"parent":'"Were you nervous？ Did you take a bow?"'},
                {"child":'摇头',"parent":'"Never？ One day you will！ And it will be wonderful!"'},
                {"child":'笑了',"parent":'"The applause at the end makes all the nervousness worth it!"'},
            ],
        },
        "role_play":{
            "intro":"让孩子扮演角色，用第一人称说出本集词汇。",
            "script_lines":['"The school play is about to begin！ Are you ready？"'],
            "rows":[
                {"child":'说 ready',"parent":'"Deep breath! The curtain rises! Break a leg!"'},
                {"child":'假装紧张',"parent":'"Nervous? Me too! But remember: the show must go on!"'},
                {"child":'说中文',"parent":'家长扮 Madame Gazelle："Places everyone！ The audience is ready!"'},
            ],
        },
        "recast":[
            {"term":'curtain call',"explanation":'"Curtain call = 谢幕，演出结束后演员出来谢谢观众"'},
            {"term":'every part is important',"explanation":'"Part = 角色。 Every part is important = 每个角色都重要"'},
        ],
    },
    phase4={
        "tpr":{
            "intro":"家长说指令，孩子用全身动作回应，不用开口。",
            "commands":[
            '"Places everyone！" — 各就各位',
            '"The curtain rises！" — 做拉幕布动作',
            '"Take a bow！" — 鞠躬',
            '"Applause！ Bravo！" — 鼓掌，"Bravo！"',
        ],
        },
        "dubbing":{
            "intro":"先看画面，后配音。家长示范 Level 1，孩子试 Level 2，挑战 Level 3。",
            "scenes":[
            {"scene":'排练',"L1":'L1: "Rehearse！"',"L2":'L2: "Let\'s rehearse the play！"',"L3":'L3: "Everyone practice your roles! The performance is soon!"'},
            {"scene":'演出前紧张',"L1":'L1: "Nervous！"',"L2":'L2: "I\'m a bit nervous！"',"L3":'L3: "My tummy has butterflies! But the show must go on!"'},
            {"scene":'演出成功，谢幕',"L1":'L1: "Bravo！ Bow！"',"L2":'L2: "Take a bow！ Bravo！"',"L3":'L3: "What a wonderful performance! Every role was brilliant! Take a bow, everyone!"'},
        ],
        },
        "bugs":{
            "rule":'说 "The show must go on" 得3分；说 "take a bow" 得2分；说 "every part is important" 得2分',
            "start_score":10,
        },
    },
    phase5={
        "story_levels":[
            {"level":'L1 (词)',"text":'play → performance → role → rehearse → nervous → audience → applause → bow'},
            {"level":'L2 (句)',"text":'The children put on a school play. Everyone had a role. They were nervous. The performance was a success.'},
            {"level":'L3 (完整)',"text":'It was time for the school play! Madame Gazelle gave everyone a role. Peppa wanted to be the star. But every part is important! They rehearsed and rehearsed. On the night, everyone was nervous — butterflies in the tummy! But the show went on. And it was wonderful! The audience applauded. Everyone took a bow!'},
        ],
        "scaffold":"家长指着手指计数，孩子每说一个词/句就竖一根手指，目标是用完5根手指。",
        "roleplay_outro":"最后用角色扮演收尾：让孩子扮演本集主角，家长扮配角，把故事重演一遍。",
    },
    phase6={
        "phonics":{
            "rule":'字母组合 ance/ence → /əns/ 轻读结尾',
            "examples":['performance', 'audience', 'confidence', 'entrance', 'distance'],
            "tongue_tip":'结尾 -ance/-ence 都是轻读 /əns/。"The performance needs confidence!"',
        },
        "next_script":'"第一季全部52集完成！太棒了！"',
        "next_a":'重温最喜欢的一集',
        "next_b":'重温本集最精彩的片段',
    },
    checklist=[
        "Phase 1：孩子喊出了上集的词汇",
        "Phase 2：孩子配合了至少一个场景动作",
        "Phase 3：孩子回答了至少1个问题",
        "Phase 4：TPR 至少跟做了2个指令 + 配音每个画面说过至少 Level 1",
        "Phase 5：孩子用英文说出了至少 3 个词讲故事",
        "Phase 6：孩子今天笑了 ✓",
    ],
    ammo=[
        {"sentence":'Every part is important.',"zh":'每个角色都很重要',"usage":'安慰没得到想要角色的孩子'},
        {"sentence":'The show must go on!',"zh":'演出必须继续！',"usage":'任何困难时的坚持'},
        {"sentence":'Take a bow!',"zh":'谢幕！',"usage":'完成任何任务时'},
        {"sentence":'Are you ready for the big performance?',"zh":'准备好大型表演了吗？',"usage":'重要活动前的鼓励'},
    ],
)



# ═══════════════════════════════════════════════════════════════════════════════
# 总目录 · 第1季全52集
# ═══════════════════════════════════════════════════════════════════════════════

EPISODES_LIST = [EP01, EP02, EP03, EP04, EP05, EP06, EP07, EP08, EP09, EP10, EP11, EP12, EP13, EP14, EP15, EP16, EP17, EP18, EP19, EP20, EP21, EP22, EP23, EP24, EP25, EP26, EP27, EP28, EP29, EP30, EP31, EP32, EP33, EP34, EP35, EP36, EP37, EP38, EP39, EP40, EP41, EP42, EP43, EP44, EP45, EP46, EP47, EP48, EP49, EP50, EP51, EP52]
EPISODES_BY_NUM = {ep["num"]: ep for ep in EPISODES_LIST}
