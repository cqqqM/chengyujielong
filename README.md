# chengyujielong
cy.json是成语字典，字段如下,收录了30895个成语
{
  "derivation":   //出处
  "example":      //例句
  "explanation":  //释义
  "pinyin":       //拼音
  "word":         //成语
  "abbreviation": //拼音缩写
}

.py文件定义了两个函数
chaci(str)
  参数为待查的成语，返回成语的释义
  
jielong(str)
  参数为一个成语，返回与其接龙的成语
