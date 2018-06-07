def load_city_list():
    city_str='53772-T 太原-53772|53882-C 长治-53882|53487-D 大同-53487|53976-J 晋城-53976|71115-J 晋中-71115|53868-L 临汾-53868|71037-L 吕梁-71037|53578-S 朔州-53578|53674-X 忻州-53674|53782-Y 阳泉-53782|53959-Y 运城-53959'
    country_list=['53772-T 太原-53772|71263-G 古交-53772|70950-J 尖草坪区-53772|71264-X 小店区-53772|71640-J 晋源-53772|70667-L 娄烦-53772|70673-Q 清徐-53772|70951-T 太原古交区-53772|70952-T 太原南郊-53772|71639-W 万柏林-53772|71638-X 杏花岭-53772|70695-Y 阳曲-53772|71637-Y 迎泽-53772','53882-C 长治-53882|70647-C 长子-53882|70657-H 壶关-53882|70664-L 黎城-53882|60225-L 潞城-53882|70671-P 平顺-53882|61063-Q 沁县-53882|70674-Q 沁源-53882|70680-T 屯留-53882|60224-W 武乡-53882|60707-X 襄垣-53882','71266-L 灵丘-53487|53487-D 大同-53487|70650-D 大同县-53487|60781-G 广灵-53487|70658-H 浑源-53487|71641-K 矿区-53487|70665-L 灵邱-53487|71642-N 南郊-53487|60782-T 天镇-53487|71643-X 新荣-53487|60697-Y 阳高-53487|70694-Z 左云-53487','60696-G 高平-53976|53976-J 晋城-53976|60227-L 陵川-53976|60226-Q 沁水-53976|60228-Y 阳城-53976|71268-Z 泽州-53976','60785-H 和顺-71115|71115-J 晋中-71115|60241-J 介休-71115|60242-L 灵石-71115|70672-P 平遥-71115|60240-Q 祁县-71115|70679-S 寿阳-71115|60336-T 太谷-71115|70689-X 昔阳-71115|60239-Y 榆次-71115|60784-Y 榆社-71115|70693-Z 左权-71115','70646-A 安泽-53868|70649-D 大宁-53868|70653-F 汾西-53868|70654-F 浮山-53868|70655-G 古县-53868|70656-H 洪洞-53868|60229-H 霍州-53868|60708-H 侯马-53868|70662-J 吉县-53868|53868-L 临汾-53868|71036-P 蒲县-53868|60709-Q 曲沃-53868|60779-X 隰县-53868|60694-X 襄汾-53868|60780-X 乡宁-53868|70690-Y 永和-53868|60778-Y 翼城-53868|71645-Y 尧都-53868','70652-F 方山-71037|60233-F 汾阳-71037|70660-J 交口-71037|60620-J 交城-71037|71037-L 吕梁-71037|60231-L 离石-71037|60783-L 临县-71037|60232-L 岚县-71037|60648-L 柳林-71037|70678-S 石楼-71037|60619-W 文水-71037|70687-X 兴县-71037|60230-X 孝义-71037|60234-Z 中阳-71037','60243-H 怀仁-53578|70669-P 平鲁-53578|53578-S 朔州-53578|70676-S 山阴-53578|71647-S 朔城-53578|70691-Y 右玉-53578|60695-Y 应县-53578','60789-B 保德-53674|70651-D 定襄-53674|70648-D 代县-53674|60788-F 繁峙-53674|60685-H 河曲-53674|70661-J 静乐-53674|70663-K 岢岚-53674|61068-N 宁武-53674|61062-P 偏关-53674|70677-S 神池-53674|70953-W 五台县-53674|70683-W 五台山-53674|70685-W 五寨-53674|53674-X 忻州-53674|71648-X 忻府-53674|60067-Y 原平-53674','71644-J 郊区-53782|70668-P 平定-53782|53782-Y 阳泉-53782|60237-Y 盂县-53782','60236-H 河津-53959|61064-J 稷山-53959|70659-J 绛县-53959|70666-L 临猗-53959|70670-P 平陆-53959|70675-R 芮城-53959|70681-W 万荣-53959|70682-W 闻喜-53959|70688-X 新绛-53959|70686-X 夏县-53959|53959-Y 运城-53959|70692-Y 垣曲-53959|60235-Y 永济-53959|71646-Y 盐湖-53959']
    cities={}
    for item in city_str.split('|'):
        item=item.split(' ')[-1]
        code=item.split('-')[-1]
        name=item.split('-')[0]
        city={
            'pre_code':code,
            'pre_name':name
        }
        cities[code]=city
    f=open('city.txt','w')
    for country_str in country_list:
        for item in country_str.split('|'):
            code=item.split('-')[0]
            name=item.split(' ')[-1].split('-')[0]
            pre_code=item.split('-')[-1]
            city=cities[pre_code]
            city['name']=name
            city['code']=code
            f.write(json.dumps(city)+'\n')

load_city_list()