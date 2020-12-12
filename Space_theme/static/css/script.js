@function alphaRandom(){
  @return random(1000)*.001;
}
@function stars($s, $max-area, $min-area : 0, $star-size : 0){
  $stars : #{$min-area + random($max-area)}px #{$min-area + random($max-area)}px 0 #{$star-size}px rgba(255,255,255, alphaRandom());
  @for $i from 1 to $s{
    $stars: '#{$stars} , #{$min-area + random($max-area)}px #{$min-area + random($max-area)}px 0 #{$star-size}px rgba(255,255,255, #{alphaRandom()})'
  }
  @return unquote($stars);
}






