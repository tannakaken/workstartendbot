# 業務時間の最初と最後に簡単な定型のメッセージを送るボット

リモート勤務の最初によく上司が

- 皆さん、zoomとtoggleを忘れずに
- 〇〇さん、zoomをonにしてください
- 〇〇さん、toggleをonにするの忘れてますよ

とよく言っていて、実際僕も良く忘れる。
あと、業務時間が終わってもtoggleをonにしたままで、作業しっぱなしみたいに見えてるとかも良くある。
ついでに、作業記録（toggle）と勤怠管理（マネーフォワード）で別のアプリを使ってるものだから、そっちも忘れて後で修正したりする。
なので、簡単に、chatworkに平日の朝と夕方に簡単なメッセージを送るものを作った。

平日・週初め・週終わり・月末、等の判定は[holiday api](http://s-proj.com/utils/holiday.html)を使った。

VPS内でcronで動かしてもよかったのだが、せっかくだからのAWSのAmazon CloudWatch Eventsのcron式と
AWS Lambdaを使ってみた。

AWS Lambdaにpipを含んだpythonの関数を登録するのは少し面倒で、
ライブラリごとzipしてuploadしなくてはいけない。
そのzipにpython自体で書かれたものではなく、C言語などで書かれたビルドしなくてはいけない低レベルのライブラリが入っていると、
ビルドされた環境の違いが原因でLambdaで動かないことがある。
参考にした[『AWS Lambda実践ガイド』](https://book.impress.co.jp/books/1116101044)には
少し情報が古いのか「EC2でAmazon Linuxを起動して同じ環境でビルド＆テストしてアップロードする」と書いてあるが、
そんな大袈裟なことしたくないので、dockerの[lambci/lambda](https://hub.docker.com/r/lambci/lambda/)を使った。

これでLambdaが起動する環境と同じ環境でビルドしてzipできるので、それをアップロードすれば良い。

Amazon CloudWatch EventsとLambdaの設定は上記の参考書を読むか、Webで情報を探してもらいたい

## 使い方

これは私の業務体系に合わせて作られていて、
一切の一般化を施していない。
自分で改造するなり、メッセージを外部のファイルから取得するようにするなりして使って欲しい。

これはcronの設定でで平日の10時と19時に起動して、現在時刻でどちらかを判定するようになっているが、
より複雑なルールにするときは、cronを複数設定して起動するスクリプトを分けたほうがわかりやすいかもしれない。

chatworkへのメッセージ送信は自作ライブラリである[chatpywork](https://github.com/tannakaken/chatpywork)を使った。

chatworkのAPIキーなどは、AWS Lambdaの環境変数に登録している。

slackなどへの送信も他のライブラリを使えば簡単にできるであろう。

## ビルド

```
make
make zip
```

でbuildフォルダにdeploy\_package.zipという名前のファイルができるのでそれを、
アップロードすれば良い。

# Author
淡中☆圏 \<tannakaken@gmail.com\>

Twitter: @tannakaken
