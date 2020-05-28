# iAccess Project 



Here I have mentioned some major tasks which I have implemented in iaccess project.


# New Features!


  - Lifetime Activity Dashboard.
  - User Rating & Review Api optimization.
  - Export Lifetime Activity Dashboard user data as a CSV file.
  - Advertisement ordering based on it’s rank.


### Description


* [Lifetime Activity Dashboard] - Lifetime achievement shall display the count of activities that a user has accumulated since he signed up on iAccess.!
* [Export CSV ] - This CSV shall consist of Lifetime activity counts for all users collectively.
* [API Optimization]- This api return user review & rating details.
* [ADs Ordering]- Ad cards the rank assigned to them shall be displayed on top right corner.and all Ads will be display based on rank order.



### Tech

- ##### Lifetime Activity Dashboard
  - Used google chart api for implementing same (https://developers.google.com/chart/interactive/docs)
  
- ##### API Optimization
   - Old code
        ```sh
          return $totalReviewAndRating = User::with(['ratings'=>function($q) use($id){
            $q->where('google_place_id', '=', $id)
              ->groupBy('user_id');
                },'reviews' =>function($q) use($id){
                    $q->where('google_place_id', '=', $id)
                    ->groupBy('user_id');
                }])
                ->orwhereHas('ratings',function($q) use($id){
                    $q->where('google_place_id', '=', $id);
                })
                ->orwhereHas('reviews',function($q) use($id){
                    $q->where('google_place_id', '=', $id);
                })->count();
        ```
    - New code 
         ```sh
              $rating = \DB::table("ratings")
                ->select("ratings.user_id")
                ->where('google_place_id', $id);

        return  $review = \DB::table("reviews")
                ->select("reviews.user_id")
                ->where('google_place_id', $id)
                ->union($rating)
                ->groupBy('user_id')
                ->count(); 
            ```
    
   In old code we used unnecessary join and also used laravel conditional Eloquent join on multiple tables which is usually slow.because it's create multiple sub query inside query for each record. It's one kind of laravel drawback. 







 










 
 

