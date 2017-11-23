15011971 황다슬

감성분석 보고서

 감성분석은 텍스트에 나타난 사람들의 태도, 의견, 그리고 성향과 같은 주관적 데이터를 분석하는 자연어처리 (Natural Language Processing)의 한 분야입니다. 이 분야가 주목을 받는 이유는 전통적인 설문 조사나 다른 조사 기법에 비해 비용이나 노력이 적게 드는 반면에 얻을 수 있는 정보가 풍부하여 새로운 마케팅이나 고객관리 수단이 될 수 있고, 또 새로운 이슈를 예측분석 할 수 있기 때문입니다.  
 우리가 이 수업에서 배우는 감성분석이란 주어진 텍스트의 문맥 정보를 파악하여 문장이 긍정 혹은 부정적 의미를 판별하는 분석 기술입니다. 본인이 아직 많이 사용해보지는 않았지만 문장이 갖는 정보가 아닌 문맥을 파악해야하기 때문에 아직은 매우 어렵고 부족한 점이 많고, 또 많은 연구가 필요한 기술이라고 생각합니다. 본인이 이 감성분석기를 사용하며 세운 가설을 발표하겠습니다.

1. 감성분석은 순서에 연연하지 않는다.  

Ex1) I think this movie is awesome, outstanding, and horrific.
Ex2) I think this movie is awesome, terrible, and horrific.

 Ex1은 2개의 긍정적인 단어들 (awesome, outstanding)과 1개의 부정적인 (horrific) 단어를 포함하고 있습니다. 그 반면에 Ex2는 1개의 긍정적인 단어 (awesome)와 2개의 부정적인 (terrible, horrific) 단어들을 포함하고 있습니다. 
어떤 결과를 예상하시나요? 본인도 당연히 첫 번째 예시는 부정적인 단어보다 긍정적인 단어를 더 많이 포함하고 있기 때문에 positive, 두 번째 예시는 그 반대여서 negative라고 나올 것을 예상했지만, 그럼에도 불구하고 결과는 똑같이 두 개 다 0.54 negative였습니다. 과연 무엇이 문제였을까요? 순서였을까요? 그럼 그 반대로 돌려봅시다.

Ex3) I think this movie is horrific, outstanding, and awesome.
Ex4) I think this movie is horrific, terrible, and awesome.

 Ex3와 Ex4 모두 위에와 똑같이 코딩되었습니다. 그럼 과연 결과는 어땠을까요? 순서만 바꿨을 뿐인데 Ex3는 0.65 positive, 그리고 Ex4은 그 위의 결과와 똑같이 0.54 negative가 나왔습니다. 이때가지만 해도 본인은 감성분석이 마지막 단어의 영향을 더 많이 받고 그러므로 순서 때문에 결과가 다르게 나오는 것이라고 생각했습니다. 하지만,
Ex5) I think this movie is both horrific and awesome.
Ex6) I think this movie is both awesome and horrific.
 
 Ex5와 Ex6를 보고 순서가 문제가 아니라는 것을 깨달았습니다. 만약에 순서가 문제였고 제가 위에 언급한대로 감성분석이 마지막 단어의 영향을 더 많이 받는다면 Ex5는 positive, Ex6는 negative가 나와야 했지만, 결과는 달랐습니다: Ex5는 0.7 positive 그리고 Ex6는 0.75 positive, 즉 두 개 다 positive로 나왔습니다. 사실 본인은 아직까지도 긍정 단어와 부정 단어의 빈도수가 같음에도 불구하고  positive/negative의 결과가 다를 뿐만 아니라 probability까지 왜 다른지 아직 깨닫지 못했지만, 이 결과를 보며 감성분석에는 순서가 중요하지 않다고 가설을 세우게 되었습니다. 하지만 이 결과가 왜 이렇게 나오는지는 아직 파악하지 못해서, 이런 부분에서는 더 많은 연구가 필요하다고 생각합니다.

2. 감성분석은 문장 구조를 파악하여 문장의 문맥 정보를 읽어내는데 아직 많이 미숙하다.

Ex7) I am healthy.
     I am not sick.
     I am sick.
     I am not healthy.

 Ex7에서는 감성분석기가 문맥 정보를 파악하는데 얼마나 유능하고 지금의 감성분석기의 실력은 어떤지 판단하고자 조금 헷갈리는 문장들을 써봤습니다. 하지만 처음에 봤을 때 문장들이 조금 어려울 수 있지만, 읽어보면 healthy나 sick와 같은 아주 쉬운 단어들로 구성되어 있는 것을 알 수 있습니다. 이러한 쉬운 단어들은 당연히 데이터에 포함되어 있고 긍정단어와 부정단어를 판별할 수 있을 것이라고 기대했지만, 결과는 처참했습니다.  첫 번째 문장 ‘I am healthy’부터 0.53 negative라는 결과가 나왔고 나머지는 순서대로 0.55 negative, 0.56 negative, 그리고 0.52 negative였습니다. ‘I am healthy’는 not이라는 단어도 포함되어있지 않고 ‘healthy’라는 단어 자체가 긍정단어기 때문에 당연히 positive가 나올 것이라고 예상했지만, 예상과 달리 negative가 떴습니다. 두 번째 문장인 ‘I am not sick’또 한 sick라는 단어 자체가 부정단어이고, 그 앞에 not을 사용했기 때문에 이중부정문이 됩니다. 이러한 문법도 표준 영어에서 아주 기본적인 것이기 때문에 positive라고 뜰 것이라고 예상했지만 결과는 달랐습니다.

Ex8) I am happy.
     I am not unhappy.
   I am unhappy.
   I am not happy.

 혹시나 Ex7에서 썼던 단어들이 데이터에 포함되어있지 않았을 수도 있어서, Ex8에서는 조금 더 단순하고 모두가 알 수 있는 단어인 ‘happy’를 사용하여 코딩을 다시 해봤습니다. 첫 번째 문장인 ‘I am happy’는 0.52 positive가 떴습니다. 사실 굉장히 단순한 문장이고 이 문장에 중립단어(I, am)와 긍정단어(happy)밖에 뿐이라 positive의 probability가 조금 더 높을 것이라고 예상했지만, 그래도 positive가 떴다는 결과에 조금 안심했습니다. 두 번 째 문장도 아주 놀랍게도 0.5 positive가 나왔습니다. 그래서 위에 했던 코딩은 아마도 단어들이 데이터에 포함되어있지 않았다고 생각하게 됐습니다. 세 번 째에도 ‘unhappy’라는 단어를 부정단어로 받아들여 0.5 negative다 떴습니다. 하지만 문제는 마지막이었는데요, ‘I am not happy’ 라는 코딩에 결과로 0.52 positive가 나왔습니다. ‘Happy’는 분명 긍정단어이고 그 앞에 ‘not’가 붙음으로서 negative가 나와야하는 상황인데, 긍정이라고 뜬 것을 보고 문장의 문맥을 파악하는데 아직 많이 미숙하고, 이 부분에 대해 더 많은 발전이 필요하다고 생각하게 되었습니다.

3. 감정분석은 구두점 (./!/?...)의 영향을 많이 받는다.

Ex9) This movie is awesome and I want to watch it again
     This movie is awesome and I want to watch it again.
     This movie is awesome and I want to watch it again!
     This movie is awesome and I want to watch it again?

Ex10) I like tomato pasta
      I like tomato pasta.
      I like tomato pasta!
      I like tomato pasta?
      I like tomato pasta:
      I like tomato pasta;

 세 번째 가설은 개인적으로 흥미로웠습니다. 정말 토시 하나 안 틀리고 똑같은 문장이었지만 구두점에 의해 probability 뿐만 아니라 positive/negative 자체가 달라진 결과를 봤습니다. 가설에는 구두점이라고 써놨지만, 사실 구두점이 없는 문장만 구두점이 있는 문장보다 0.01 높았거나 낮게 나왔습니다. Ex9에서는 구두점이 없는 문장만 빼고 모두 0.67 positive였고, 구두점이 없는 문장 홀로 0.66 positive였습니다. Ex10에서는 좀 더 다양한 구두점을 사용해봤는데, 결과는 그만큼 더 흥미로웠습니다. 구두점이 없는 문장 빼고 모두 0.52 negative였고, 구두점이 없는 문장은 놀랍게도 0.74 positive가 나왔습니다. Ex10 같은 경우에는 애초에 긍정문장이기 때문에 negative가 나온 것도 놀라웠지만, 구두점이 없는 문장만 positive가 나왔다는 것이 매우 놀라웠습니다. 사실 이 원리가 어떻게 돌아가는지는 정확히 모르지만, 구두점에 의해 probability뿐만 아니라 positive/negative 결과 자체가 달라질 수 있다는 것을 깨달았습니다.
 이번 보고서를 쓰면서 감성분석기를 많이 써보고 또 감성분석 그 자체에 대해 많이 알게 되었습니다. 시간이 지나면서 이 기술이 더더욱 많이 사용되며 향후 발전가능성이나 전망이 매우 뛰어나다고 개인적으로 판단이 되는데, 제가 세운 가설들이 어떻게 보면 감성분석기의 한계점을 많이 담고 있어 이러한 점들을 더 보완된다면 향후에 더 많이 사용되고 더더욱 발전할 수 있을 것이라고 예상합니다.
