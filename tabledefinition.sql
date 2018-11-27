CREATE TABLE `posts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `text` text COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin ROW_FORMAT=DYNAMIC;

-- Create syntax for TABLE 'terms'
CREATE TABLE `terms` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `term` varchar(255) NOT NULL DEFAULT '',
  `counter` bigint(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;

-- Create syntax for TABLE 'topics'
CREATE TABLE `topics` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `post_id` bigint(11) unsigned NOT NULL,
  `topic_number` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;