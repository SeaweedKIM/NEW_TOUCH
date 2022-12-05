/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
      const $ = (el) => document.querySelector(el);

      const store = {
        texts: "",
        isRecognizing: true,
      };



      (() => {
        /* Speech API start */
        let SpeechRecognition =
          window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!("webkitSpeechRecognition" in window)) {
          alert("지원 안되는 브라우저 입니다. !");
        } else {
          const recognition = new SpeechRecognition();
          recognition.interimResults = true; // true면 음절을 연속적으로 인식하나 false면 한 음절만 기록함
          recognition.lang = "ko-KR"; // 값이 없으면 HTML의 <html lang="en">을 참고합니다. ko-KR, en-US
          recognition.continuous = false; //각 인식에 대해 연속 결과가 반환되는지 아니면 단일 결과만 반환되는지를 제어합니다. 기본값은 단일( false.)
          recognition.maxAlternatives = 20000; // maxAlternatives가 숫자가 작을수록 발음대로 적고, 크면 문장의 적합도에 따라 알맞은 단어로 대체합니다.

          recognition.onspeechend = function () {
            // 음성 감지가 끝날때 실행될 이벤트
            recognition.stop();
            $(".dictate").classList.remove("on");
            store.isRecognizing = true;
          };

          recognition.onresult = function (e) {
            //result이벤트는 음성 인식 서비스가 결과를 반환할 때 시작됩니다.
            store.texts = Array.from(e.results)
              .map((results) => results[0].transcript)
              .join("");

            console.log(store.texts);
            $("input").value = store.texts;
          };
          /* // Speech API END */

          const active = () => {
            $(".dictate").classList.add("on");
            recognition.start();
            store.isRecognizing = false;
          };

          const unactive = () => {
            $(".dictate").classList.remove("on");
            recognition.stop();
            store.isRecognizing = true;
          };

          $(".dictate").addEventListener("click", () => {
            if (store.isRecognizing) {
              active();
            } else {
              unactive();
            }
          });
                //서밋 버튼 클릭시 전송 addEventListener()는 document의 특정요소 event(ex - click하면 함수를 실행하라)를 등록할 때 사용 
          $(".submitbtn").addEventListener('click', ()=> {
          document.getElementById('kw').value = document.getElementById('search_kw').value;
          document.getElementById('searchForm').submit();
          });
        }
      }
      )();


            function modal(id) {
                var zIndex = 9999;
                var modal = document.getElementById(id);

                // 모달 div 뒤에 희끄무레한 레이어
                var bg = document.createElement('div');
                bg.setStyle({
                    position: 'fixed',
                    zIndex: zIndex,
                    left: '0px',
                    top: '0px',
                    width: '100%',
                    height: '100%',
                    overflow: 'auto',
                    // 레이어 색갈은 여기서 바꾸면 됨
                    backgroundColor: 'rgba(0,0,0,0.4)'
                });
                document.body.append(bg);

                // 닫기 버튼 처리, 시꺼먼 레이어와 모달 div 지우기
                modal.querySelector('.btn_close').addEventListener('click', function() {
                    bg.remove();
                    modal.style.display = 'none';
                });

                modal.setStyle({
                    position: 'fixed',
                    display: 'block',
                    boxShadow: '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)',

                    // 시꺼먼 레이어 보다 한칸 위에 보이기
                    zIndex: zIndex + 1,

                    // div center 정렬
                    top: '50%',
                    left: '50%',
                    transform: 'translate(-50%, -50%)',
                    msTransform: 'translate(-50%, -50%)',
                    webkitTransform: 'translate(-50%, -50%)'
                });
            }

            // Element 에 style 한번에 오브젝트로 설정하는 함수 추가
            Element.prototype.setStyle = function(styles) {
                for (var k in styles) this.style[k] = styles[k];
                return this;
            };

            document.getElementById('popup_open_btn').addEventListener('click', function() {
                // 모달창 띄우기
                modal('my_modal');
            });


function refresh()  {
  const element = document.getElementById('my_div');
  element.innerHTML = '';
}











