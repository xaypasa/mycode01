async function getFoods() {
    const url = 'https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood';
    const req = await fetch(url);
    const res = await req.json();
    const meals = res.meals;
    const list = document.getElementById('menu');
    list.innerHTML = meals
      .map(
        (x) => `<li>
                <img width="100" src="${x.strMealThumb}" alt="">
                <h2>${x.strMeal}</h2>
            <p>$4</p>
        </li>`
      )
      .join('');
  }
  getFoods();
  