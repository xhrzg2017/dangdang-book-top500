# dangdang-book-top500
本项目可将当当 2020 图书 top500 保存到csv<br>
功能说明:

    ✓代表保存
    ○✓如有保存
            '标题': title, ✓
            '评论量': comment,✓
            '推荐值': recommend,✓
            '作者': author,✓
            '出版日期': publicationDate,✓
            '出版社': press,✓
            '原价': price_r,✓
            '售价': price_n,✓
            '折扣': price_s,✓
            '电子书价格': price_e, ○✓
            '详情页地址': href,✓
        
 实现原理：
    
    1.对网页请求
    2.对网页切片
        2.1 提取大列表
        2.2 提取小列表
    3. 每次返回一个小列表
        3.1 按规则提取内容
            3.1.1 电子书 价格部分为空（不是所有书都有电子版）返回  none
    4. 保存到csv(电子书有则保存，没则空)

